from uuid import UUID

from django.db.models import QuerySet

from src.code_review__web.code_review__app.models import File


def get_files_by_user_id(user_id: UUID) -> QuerySet:
    return File.objects.filter(fk_user__id=user_id)


def get_file_by_id(file_id: UUID) -> File:
    return File.objects.filter(id=file_id).first()  # type: ignore


def get_not_reviewed_files() -> QuerySet:
    return File.objects.filter(is_reviewed__in=['not_reviewed_new', 'not_reviewed_updated'])
