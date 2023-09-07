from django.urls import path

from src.code_review__web.code_review__users.views import sign_in, sign_out, sign_up

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/', sign_up, name='register'),
]
