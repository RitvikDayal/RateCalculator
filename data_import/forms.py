from django import forms
from .models import excelFile

class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    class Meta:
        model = excelFile
        fields = '__all__'