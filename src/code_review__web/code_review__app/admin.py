from django.contrib import admin

from .models import UserFile, File

admin.site.register(File)
admin.site.register(UserFile)
