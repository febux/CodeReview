from typing import Any

from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, CharField, PasswordInput

from src.code_review__web.code_review__users.models import CustomUser


class LoginForm(Form):    # type: ignore
    username = CharField(label='Email / Username', validators=[validators.EmailValidator(message="Invalid Email")])
    password = CharField(max_length=65, widget=PasswordInput)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['id'] = 'password-field'


class RegisterForm(UserCreationForm):    # type: ignore

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['id'] = 'password1-field'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['id'] = 'password2-field'

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
