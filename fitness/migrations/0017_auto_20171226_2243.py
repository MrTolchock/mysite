# Generated by Django 2.0 on 2017-12-26 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0016_auto_20171226_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['prog_order'], 'verbose_name': 'My Exercise', 'verbose_name_plural': 'My Exercises'},
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='the_order',
            new_name='prog_order',
        ),
    ]
