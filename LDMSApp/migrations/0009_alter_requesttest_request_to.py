# Generated by Django 4.1.6 on 2023-03-12 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LDMSApp', '0008_alter_requesttest_facility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttest',
            name='request_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LDMSApp.laboratory'),
        ),
    ]
