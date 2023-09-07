from datetime import datetime
import uuid

from django.conf import settings
from django.db.models import Model, ForeignKey, CASCADE, UUIDField, DateTimeField, CharField, \
    FileField, TextField, BooleanField


def user_directory_path(instance: 'File', filename: str) -> str:
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user__{instance.fk_user.username}/{filename}'


REVIEW_CHOICES = [
    ("reviewed_ok", "Reviewed successfully"),
    ("reviewed_not_ok", "Reviewed with errors"),
    ("not_reviewed_new", "Not reviewed (New)"),
    ("not_reviewed_updated", "Not reviewed (Updated)"),
    ("in_review", "In review"),
]


class BaseModel(Model):   # type: ignore
    id = UUIDField(primary_key=True, default=uuid.uuid4)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    class Meta:
        abstract = True


class File(BaseModel):
    file_name = CharField(verbose_name="Name", max_length=120, unique=True)
    file_data = FileField(verbose_name="File", upload_to=user_directory_path)
    fk_user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    is_reviewed = CharField(verbose_name="Review state", default='not_reviewed_new', choices=REVIEW_CHOICES)
    review_result = TextField(verbose_name="Review result", default='')

    user_notified = BooleanField(verbose_name="Email notification was sent", default=False)

    def __str__(self) -> str:
        return f"{self.file_name}"

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ('-created_at',)
