# Generated by Django 4.0.3 on 2022-06-11 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0014_remove_machine_maintenancedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 17, 2, 43, 626315)),
        ),
    ]
