# Generated by Django 3.0.2 on 2020-04-08 05:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('field', models.CharField(choices=[('研究', '研究')], default='研究', max_length=32, verbose_name='ジャンル')),
                ('author', models.CharField(blank=True, max_length=32, null=True, verbose_name='著者')),
                ('conference', models.CharField(blank=True, max_length=32, null=True, verbose_name='会議名')),
                ('year', models.IntegerField(default=2020, verbose_name='年')),
                ('deadline', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='期限')),
                ('expired', models.BooleanField(default=False, verbose_name='期限切れ')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='感想')),
                ('read_or_not', models.BooleanField(default=False)),
                ('read_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='読んだ日')),
                ('order', models.IntegerField(default=0, verbose_name='順番')),
            ],
        ),
    ]
