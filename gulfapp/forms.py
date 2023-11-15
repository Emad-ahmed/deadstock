from django import forms
from .models import ExcelData

class ExcelDataForm(forms.ModelForm):
    class Meta:
        model = ExcelData
        fields = '__all__'


