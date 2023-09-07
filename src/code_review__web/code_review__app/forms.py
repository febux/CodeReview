from typing import Any

from django.forms import ModelForm

from src.code_review__web.code_review__app.models import File


class CreateFileForm(ModelForm):    # type: ignore

    class Meta:
        model = File
        fields = ['file_name', 'file_data']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['file_name'].widget.attrs['class'] = 'form-control'
        self.fields['file_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['file_data'].widget.attrs['class'] = 'form-control-file'
        self.fields['file_data'].widget.attrs['placeholder'] = 'File'
        self.fields['file_data'].widget.attrs['accept'] = '.py'
