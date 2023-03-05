# Generated by Django 4.1.6 on 2023-03-05 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LDMSApp', '0002_alter_patientinfo_time_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='time_issued',
            field=models.DateField(verbose_name=datetime.datetime(2023, 3, 5, 6, 40, 41, 735677, tzinfo=datetime.timezone.utc)),
        ),
    ]
