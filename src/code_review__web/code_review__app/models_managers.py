from typing import Any

from django.db.models import QuerySet

from .models import File


def get_files_by_user_id(user_id: Any) -> QuerySet:
    return File.objects.filter(fk_user__id=user_id)
