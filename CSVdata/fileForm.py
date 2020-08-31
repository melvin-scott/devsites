from django import forms
from .models import CSVFile

class FileForm(forms.ModelForm):
   class Meta:
        model = CSVFile
        fields = ["file_name", "file_path"]