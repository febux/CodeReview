# Generated by Django 4.2.4 on 2023-09-04 19:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid

from src.code_review__web.code_review__app.models import user_directory_path


class Migration(migrations.Migration):  # type: ignore

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('file_name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('file_data', models.FileField(upload_to=user_directory_path, verbose_name='File')),
                ('is_reviewed', models.CharField(choices=[('reviewed_ok', 'Reviewed successfully'),
                                                          ('reviewed_not_ok', 'Reviewed with errors'),
                                                          ('not_reviewed_new', 'Not reviewed (New)'),
                                                          ('not_reviewed_updated', 'Not reviewed (Updated)'),
                                                          ('in_review', 'In review')],
                                                 default='not_reviewed_new', verbose_name='Review state')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FileLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('date', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('review_result', models.TextField(default='', verbose_name='Review result')),
                ('fk_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='File')),
                ('user_notified', models.BooleanField(default=False, verbose_name='Email notification was sent')),
            ],
            options={
                'verbose_name': 'FileLog',
                'verbose_name_plural': 'FileLogs',
                'ordering': ('-created_at',),
            },
        ),
    ]
