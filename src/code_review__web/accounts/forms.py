from typing import Any

from allauth.account.forms import LoginForm, SignupForm


class CustomLoginForm(LoginForm):   # type: ignore
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['id'] = 'password-field'


class RegisterForm(SignupForm):   # type: ignore

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['id'] = 'password1-field'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        # self.fields['password2'].widget.attrs['id'] = 'password2-field'
