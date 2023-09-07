from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):    # type: ignore
    email = models.EmailField(_('email address'), unique=True)
