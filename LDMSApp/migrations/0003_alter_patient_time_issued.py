# Generated by Django 4.1.6 on 2023-03-27 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LDMSApp', '0002_alter_patient_time_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='time_issued',
            field=models.DateField(verbose_name=datetime.datetime(2023, 3, 27, 15, 34, 36, 624072, tzinfo=datetime.timezone.utc)),
        ),
    ]
