# Generated by Django 4.0.2 on 2022-07-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='sname',
        ),
    ]
