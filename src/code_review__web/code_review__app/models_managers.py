from uuid import UUID

from django.db.models import QuerySet

from src.code_review__web.code_review__app.models import FileLog, File


def get_files_by_user_id(user_id: UUID) -> QuerySet[File]:
    return File.objects.filter(fk_user__id=user_id)


def get_file_by_id(file_id: UUID) -> File | None:
    return File.objects.filter(id=file_id).first()


def get_file_log_by_file_id(file_id: UUID) -> FileLog | None:
    return FileLog.objects.filter(fk_file__id=file_id).first()


def get_not_reviewed_files() -> QuerySet[File]:
    return File.objects.filter(is_reviewed__in=['not_reviewed_new', 'not_reviewed_updated'])
