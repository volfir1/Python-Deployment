# Generated by Django 4.0.4 on 2022-04-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_timetable_instructor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='instructor',
            new_name='teacher',
        ),
    ]