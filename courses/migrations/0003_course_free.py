# Generated by Django 2.2.7 on 2019-11-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20191112_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]
