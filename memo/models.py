from django.db import models
from django.utils.timezone import now

class Memo(models.Model):
    date = models.DateField('日付', default=now)
    memo = models.TextField('メモ')

    def __str__(self):
        return self.date

# Create your models here.

# Create your models here.
