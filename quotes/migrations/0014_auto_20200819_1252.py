# Generated by Django 3.0.7 on 2020-08-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0013_auto_20200819_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awningbrackettype',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningcordlength',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningcranksize',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awninghoodcover',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningmotortype',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningmount',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningoperation',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningremote',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningtype',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='awningvalance',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]