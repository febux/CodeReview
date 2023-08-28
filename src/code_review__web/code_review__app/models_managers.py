from typing import Any

from django.db.models import QuerySet

from .models import UserFile


def get_user_files_by_user_id(user_id: Any) -> QuerySet:
    return UserFile.objects.filter(fk_user__id=user_id)
