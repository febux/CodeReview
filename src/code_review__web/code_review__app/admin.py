from django.contrib import admin

from src.code_review__web.code_review__app.models import File, FileLog

admin.site.register(File)
admin.site.register(FileLog)
