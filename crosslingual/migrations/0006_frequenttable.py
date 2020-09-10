# Generated by Django 3.0.2 on 2020-09-09 04:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosslingual', '0005_auto_20200214_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=16, verbose_name='元の単語')),
                ('words', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), max_length=320, null=True, size=10)),
                ('dists', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), max_length=320, null=True, size=10)),
                ('num', models.IntegerField(default=0)),
                ('src_lang', models.CharField(choices=[('en', '英語'), ('es', 'スペイン語'), ('it', 'イタリア語'), ('fr', 'フランス語')], default='en', max_length=256, verbose_name='入力言語')),
                ('tgt_lang', models.CharField(choices=[('en', '英語'), ('es', 'スペイン語'), ('it', 'イタリア語'), ('fr', 'フランス語')], default='es', max_length=256, verbose_name='出力言語')),
            ],
        ),
    ]
