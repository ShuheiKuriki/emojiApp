from django.forms import ModelForm
from django import forms
from .models import Memo
# from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class MemoForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = Memo
        fields = ['date','memo']
        widgets = {
            'date': DateInput(),
            }