# Generated by Django 3.1 on 2020-08-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSVdata', '0003_auto_20200827_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='file_name',
            field=models.FileField(upload_to='%Y/%m/%d'),
        ),
    ]
