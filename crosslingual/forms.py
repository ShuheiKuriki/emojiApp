from django.forms import Form, ModelForm
from django import forms
from .models import Translate, FrequentTable
# from django.utils import timezone

class TranslateForm(ModelForm):
  class Meta:
    model = Translate
    fields = ['source','src_lang','tgt_lang']
    # widgets = {
    #   'done_date': forms.SelectDateWidget
    # }

class SimilarForm(forms.Form):
  word = forms.CharField(label='単語', max_length=100)
  lang = forms.fields.ChoiceField(
    choices = [
      ('ja', '日本語'),
      ('pt', 'ポルトガル語'),
      ('la', 'ラテン語'),
      ('eo', 'エスペラント語'),
      ('nl', 'オランダ語'),
      ('ru', 'ロシア語'),
      ('th', 'タイ語'),
      ('ko', '韓国語'),
      ('zh', '中国語'),
      ('en', '英語'),
      ('es', 'スペイン語'),
      ('es', 'フランス語'),
      ('it', 'イタリア語')
    ],
    required=True,
    widget=forms.widgets.Select
  )

class LangForm(ModelForm):
  class Meta:
    model = FrequentTable
    fields = ['src_lang','tgt_lang']
    # widgets = {
    #   'done_date': forms.SelectDateWidget
    # }

# class EditForm(Form, task):
#   name = CharField('タスク名', max_length=256, default=task.name)
#   deadline = models.DateField('期限', default=task.deadline)
