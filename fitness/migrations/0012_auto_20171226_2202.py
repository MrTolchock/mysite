# Generated by Django 2.0 on 2017-12-26 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0011_exercise_in_prog'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='exercise',
            order_with_respect_to='media_file',
        ),
    ]
