# Generated by Django 3.0.2 on 2020-01-29 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosslingual', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translate',
            name='model',
        ),
    ]
