from django.db import models
from django.contrib.postgres.fields import ArrayField

class Translate(models.Model):
  source = models.CharField('元の単語', max_length=16)
  target_sup = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
  target_unsup = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
  target_joint = ArrayField(models.CharField(max_length=32),size=5, max_length=(32 * 5), null=True)
  # id = models.AutoField(primary_key=True)
  src_lang = models.CharField('入力言語', 
    choices=[('en',"英語"),('es', "スペイン語"),('fr', "フランス語"),('it', "イタリア語"),('ja', '日本語')],
    max_length=256
  )
  tgt_lang = models.CharField('出力言語', 
    choices=[('en',"英語"),('es', "スペイン語"),('fr', "フランス語"),('it', "イタリア語"),('ja', '日本語')],
    max_length=256
  )

choice = [
  ('en', '英語'),
  ('es', 'スペイン語'),
  ('es', 'フランス語'),
  ('it', 'イタリア語'),
  ('ja', '日本語'),
  ('pt', 'ポルトガル語'),
  ('la', 'ラテン語'),
  ('eo', 'エスペラント語'),
  ('nl', 'オランダ語'),
  ('ru', 'ロシア語'),
  ('th', 'タイ語'),
  ('ko', '韓国語'),
  ('zh', '中国語')
]

class FrequentTable(models.Model):
  source = models.CharField('元の単語', max_length=16)
  words = ArrayField(models.CharField(max_length=32), size=10, max_length=(32 * 10), null=True)
  dists = ArrayField(models.CharField(max_length=32), size=10, max_length=(32 * 10), null=True)
  num = models.IntegerField(default=0, null=False)
  src_lang = models.CharField('入力言語', choices=choice, max_length=256)
  tgt_lang = models.CharField('出力言語', choices=choice, max_length=256)


# class Done(models.Model):
#   name = models.CharField(max_length=256)
#   id = models.AutoField(primary_key=True)
# Create your models here.
