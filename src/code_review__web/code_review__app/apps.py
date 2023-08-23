from django.apps import AppConfig


class CodeReviewAppConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'code_review__app'
