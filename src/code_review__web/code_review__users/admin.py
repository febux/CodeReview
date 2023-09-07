from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.code_review__web.code_review__users.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
