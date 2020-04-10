from django.forms import ModelForm
from django import forms
from .models import Paper
# from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class PaperForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = Paper
        fields = ['title','field','author','conference','year','memo']
        widgets = {
            'deadline': DateInput(),
            }

class SortForm(forms.Form):
    keys = [("field",'分野'),("year",'年'),("conference",'会議'),("edit_date",'最終編集日')]
    key = forms.ChoiceField(choices=keys,required=True)