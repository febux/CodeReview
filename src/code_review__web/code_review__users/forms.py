from typing import Any

from django.forms import Form, CharField, PasswordInput


class LoginForm(Form):    # type: ignore
    username = CharField(max_length=65)
    password = CharField(max_length=65, widget=PasswordInput)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['id'] = 'password-field'
