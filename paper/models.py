from django.db import models
from django.utils.timezone import now

class Paper(models.Model):
    field_lis = ["研究"]
    fields=[(i,i) for i in field_lis]

    title = models.CharField('タイトル', max_length=128)
    field = models.CharField('分野', choices=fields, default ='研究',max_length=32)
    author = models.CharField('著者', max_length=32, blank=True, null=True)
    conference = models.CharField('会議名', max_length=32, blank=True, null=True)
    year = models.IntegerField('年', default=2020)
    deadline = models.DateField('期限', default=now, blank=True, null=True)
    expired = models.BooleanField('期限切れ', default=False)
    memo = models.TextField('感想', blank=True, null=True)

    read_or_not = models.BooleanField(default=False)
    read_date = models.DateField('読んだ日', default=now, blank=True, null=True)
    order = models.IntegerField('順番', default=0)

    def __str__(self):
        return self.title

# Create your models here.
