# Generated by Django 4.1.6 on 2023-03-25 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LDMSApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='time_issued',
            field=models.DateField(verbose_name=datetime.datetime(2023, 3, 25, 11, 4, 14, 903831, tzinfo=datetime.timezone.utc)),
        ),
    ]
