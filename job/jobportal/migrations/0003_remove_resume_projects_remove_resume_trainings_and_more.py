# Generated by Django 4.0.2 on 2022-07-05 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_remove_resume_date_remove_resume_locality_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='PROJECTS',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='TRAININGS',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='linkedin',
        ),
    ]
