# Generated by Django 2.2 on 2020-08-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('un_app', '0009_remove_aseancountry_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bricscountry',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='g4country',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='g7country',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='saarccountry',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
