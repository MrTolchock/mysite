# Generated by Django 2.0 on 2017-12-25 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0008_auto_20171225_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='media_file',
            field=models.FileField(upload_to='fitness'),
        ),
    ]