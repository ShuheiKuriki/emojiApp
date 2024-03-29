# Generated by Django 3.0.2 on 2020-01-29 15:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosslingual', '0002_remove_translate_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translate',
            name='target',
        ),
        migrations.AddField(
            model_name='translate',
            name='target_sup',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), max_length=160, null=True, size=5),
        ),
        migrations.AddField(
            model_name='translate',
            name='target_unsup',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), max_length=160, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='translate',
            name='source',
            field=models.CharField(max_length=16, verbose_name='元の単語'),
        ),
    ]
