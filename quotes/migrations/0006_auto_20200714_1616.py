# Generated by Django 3.0.7 on 2020-07-14 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20200713_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='date_modified',
        ),
    ]