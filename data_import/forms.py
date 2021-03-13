# Utility imports
from django import forms
from django.core.validators import FileExtensionValidator

# Local import
from .models import excelFile

class UploadFileForm(forms.ModelForm):
    '''
    Creates a form instance with a file field used in html template to upload files.
    '''
    class Meta:
        '''
        Connected the model to save the uploaded files through the form.
        '''
        model = excelFile #1 reference to models.py
        widgets = {'file': forms.FileInput(attrs={'accept': 'application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})}
        fields = ['file'] # fields to render as form