# Generated by Django 3.2.16 on 2023-01-04 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
