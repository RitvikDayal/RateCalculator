from django import forms
from django.core.validators import FileExtensionValidator
from .models import excelFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = excelFile
        widgets = {'file': forms.FileInput(attrs={'accept': 'application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})}
        fields = ['file']