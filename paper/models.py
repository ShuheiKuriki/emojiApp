from django.db import models
from django.utils.timezone import now

class Paper(models.Model):
    field_lis = ["RVSML","文類似性尺度","Cross lingual"]
    fields=[(i,i) for i in field_lis]

    title = models.CharField('タイトル', max_length=128)
    field = models.CharField('分野', choices=fields, default ='研究',max_length=32)
    author = models.CharField('著者', max_length=32, blank=True, null=True)
    conference = models.CharField('会議名', max_length=32, blank=True, null=True)
    url = models.CharField('URL', max_length=128, blank=True, null=True)
    year = models.IntegerField('年', default=2020)
    memo = models.TextField('感想', blank=True, null=True)

    read_or_not = models.BooleanField(default=False)
    edit_date = models.DateField('最終編集日', default=now)

    def __str__(self):
        return self.title

# Create your models here.
