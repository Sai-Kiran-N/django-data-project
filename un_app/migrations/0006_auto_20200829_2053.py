# Generated by Django 2.2 on 2020-08-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('un_app', '0005_auto_20200829_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aseancountry',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aseancountry',
            name='short_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='regiondata',
            name='region',
            field=models.CharField(max_length=50),
        ),
    ]
