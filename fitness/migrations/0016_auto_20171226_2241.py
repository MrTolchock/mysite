# Generated by Django 2.0 on 2017-12-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0015_auto_20171226_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['the_order'], 'verbose_name': 'My Sortable Class', 'verbose_name_plural': 'My Sortable Classes'},
        ),
        migrations.AddField(
            model_name='exercise',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]