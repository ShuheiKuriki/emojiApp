# Generated by Django 3.0.2 on 2020-04-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='field',
            field=models.CharField(choices=[('研究', '研究')], default='研究', max_length=32, verbose_name='分野'),
        ),
    ]