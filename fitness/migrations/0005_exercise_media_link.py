# Generated by Django 2.0 on 2017-12-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_auto_20171225_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='media_link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
