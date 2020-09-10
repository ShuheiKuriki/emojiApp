# Generated by Django 3.0.2 on 2020-04-12 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0004_auto_20200410_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='url',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='edit_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='最終編集日'),
        ),
    ]