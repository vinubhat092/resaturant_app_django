# Generated by Django 3.2.16 on 2023-01-04 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230104_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
