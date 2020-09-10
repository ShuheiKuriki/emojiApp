from django.forms import Form, ModelForm
from django import forms
from .models import Translate, FrequentTable
# from django.utils import timezone

class TranslateForm(ModelForm):
    class Meta:
        model = Translate
        exclude = ['target_sup','target_unsup', 'target_joint']
        # widgets = {
        #     'done_date': forms.SelectDateWidget
        # }

class LangForm(ModelForm):
    class Meta:
        model = FrequentTable
        fields = ['src_lang','tgt_lang']
        # widgets = {
        #     'done_date': forms.SelectDateWidget
        # }

# class EditForm(Form, task):
#     name = CharField('タスク名', max_length=256, default=task.name)
#     deadline = models.DateField('期限', default=task.deadline)
