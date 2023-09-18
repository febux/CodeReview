from uuid import UUID

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from src.code_review__web.code_review__app.models import FileLog
from src.code_review__web.code_review_project import settings

from src.code_review__web.code_review__app.models_managers import get_not_reviewed_files, get_file_log_by_file_id, get_file_by_id
from src.code_review__web.code_review_project.epylint.epylint import py_run

logger = get_task_logger(__name__)


@shared_task  # type: ignore
def process_review(file_id: UUID) -> None:
    file = get_file_by_id(file_id)
    logger.info(f"file path - {file.file_data.path}")

    pylint_stdout, pylint_stderr = py_run(file.file_data.path, return_std=True)
    logger.info(f"Result {pylint_stdout.getvalue(), pylint_stderr.getvalue()}")
    review_result = FileLog(review_result=pylint_stdout.getvalue(), fk_file=file)
    review_result.save()
    file.is_reviewed = "reviewed_ok" if pylint_stdout.getvalue() == '' else "reviewed_not_ok"
    file.save()

    review_done_mailing.delay(file_id)


@shared_task  # type: ignore
def check_new_files() -> None:
    not_reviewed_files = get_not_reviewed_files()
    logger.info(f"Not reviewed files: [{not_reviewed_files}]")
    for file in not_reviewed_files:
        file_obj = get_file_by_id(file.id)
        file_obj.is_reviewed = "in_review"
        file_obj.save()

        process_review.delay(file.id)


@shared_task  # type: ignore
def review_done_mailing(file_id: UUID) -> None:
    file_log = get_file_log_by_file_id(file_id)
    subject = 'Review result'
    message = f'{file_log.review_result}'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[file_log.fk_file.fk_user.email],
    )
    file_log.user_notified = True
    file_log.save()
