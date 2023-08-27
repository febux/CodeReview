from datetime import datetime
import uuid

from django.db.models import Model, ForeignKey, CASCADE, UUIDField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import User


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    class Meta:
        abstract = True


class File(BaseModel):
    path = TextField()

    is_reviewed = BooleanField(default=False)

    def __str__(self):
        return str(self)

    class Meta:
        app_label = 'code_review__app'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ('-created_at',)


class UserFile(BaseModel):
    fk_user = ForeignKey(User, on_delete=CASCADE)
    fk_file = ForeignKey(File, on_delete=CASCADE)

    def __str__(self):
        return str(self)

    class Meta:
        app_label = 'code_review__app'
        verbose_name = 'UserFile'
        verbose_name_plural = 'UserFiles'
        ordering = ('-created_at',)
