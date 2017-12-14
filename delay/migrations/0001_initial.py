# Generated by Django 2.0 on 2017-12-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('fahrt_bezeichner', models.CharField(max_length=20)),
                ('bpuic', models.IntegerField()),
                ('haltestellen_name', models.CharField(max_length=50)),
                ('linien_text', models.CharField(max_length=20)),
                ('betriebstag', models.DateTimeField()),
                ('ankunftszeit', models.DateTimeField()),
                ('an_prognose', models.DateTimeField(null=True)),
                ('an_prognose_status', models.CharField(max_length=20)),
                ('abfahrtszeit', models.DateTimeField()),
                ('ab_prognose', models.DateTimeField(null=True)),
                ('ab_prognose_status', models.CharField(max_length=20)),
                ('faellt_aus_tf', models.CharField(max_length=20)),
                ('ab_delay', models.CharField(max_length=20, null=True)),
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]