# Generated by Django 3.2.16 on 2023-01-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_articles_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publish',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
