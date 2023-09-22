import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import src.code_review__web.code_review__app.models


class Migration(migrations.Migration):  # type: ignore

    dependencies = [
        ('code_review__app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_data',
            field=models.FileField(upload_to=src.code_review__web.code_review__app.models.user_directory_path,
                                   validators=[
                                       django.core.validators.FileExtensionValidator(
                                           allowed_extensions=['py'])
                                   ],
                                   verbose_name='File',
                                   ),
        ),
        migrations.AlterField(
            model_name='filelog',
            name='fk_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_review__app.file'),
        ),
    ]
