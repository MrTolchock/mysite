# Generated by Django 2.0 on 2017-12-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delay', '0002_auto_20171222_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='ab_delay',
            field=models.IntegerField(null=True),
        ),
    ]
