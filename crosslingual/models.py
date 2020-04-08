from django.db import models
from django.contrib.postgres.fields import ArrayField

class Translate(models.Model):
    source = models.CharField('元の単語', max_length=16)
    target_sup = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
    target_unsup = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
    target_joint = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
    # id = models.AutoField(primary_key=True)
    src_tgt_lang = models.CharField('言語対',
                    choices=[('en-es',"英語→スペイン語"),('es-en', "スペイン語→英語"),
                             ('en-ja', "英語→日本語"),('ja-en', "日本語→英語"),
                             ('en-it', "英語→イタリア語"),('it-en', "イタリア語→英語"),
                             ('it-es',"イタリア語→スペイン語"),('es-it', "スペイン語→イタリア語")],
                    default ='en-es', max_length=256)


# class Done(models.Model):
#     name = models.CharField(max_length=256)
#     id = models.AutoField(primary_key=True)
# Create your models here.
