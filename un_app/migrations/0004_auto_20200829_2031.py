# Generated by Django 2.2 on 2020-08-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('un_app', '0003_auto_20200829_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='BricsCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'brics_country',
            },
        ),
        migrations.CreateModel(
            name='G4Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'g4_country',
            },
        ),
        migrations.CreateModel(
            name='G7Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'g7_country',
            },
        ),
        migrations.RenameModel(
            old_name='RegionsData',
            new_name='RegionData',
        ),
        migrations.AlterModelTable(
            name='aseancountry',
            table='asean_country',
        ),
        migrations.AlterModelTable(
            name='regiondata',
            table='region_data',
        ),
        migrations.AlterModelTable(
            name='saarccountry',
            table='saarc_country',
        ),
    ]
