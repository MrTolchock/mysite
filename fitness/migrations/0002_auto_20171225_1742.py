# Generated by Django 2.0 on 2017-12-25 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercises',
            new_name='Exercise',
        ),
    ]
