# Generated by Django 3.2.16 on 2023-01-04 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articles_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='publish',
        ),
    ]
