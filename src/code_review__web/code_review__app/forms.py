from typing import Any

from django.forms import Form, CharField, FileField


class FileForm(Form):    # type: ignore
    file_name = CharField(max_length=120)
    file_data = FileField()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['file_name'].widget.attrs['class'] = 'form-control'
        self.fields['file_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['file_data'].widget.attrs['class'] = 'form-control-file'
        self.fields['file_data'].widget.attrs['placeholder'] = 'File'
