# Generated by Django 3.1 on 2020-08-27 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSVdata', '0002_auto_20200827_1440'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='CSVFile',
        ),
    ]
