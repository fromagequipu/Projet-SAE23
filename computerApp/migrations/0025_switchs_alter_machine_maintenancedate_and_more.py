# Generated by Django 4.0.3 on 2022-06-12 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0024_alter_machine_maintenancedate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Switchs',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('maintenanceDate', models.DateField(default=datetime.datetime(2022, 6, 12, 10, 39, 52, 511549))),
                ('mach', models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'Mac - Run MacOS'), ('Serveur', 'Serveur - Simple Serveur to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers'), ('Routeur', 'Routeur - Use to have Internet')], default='PC', max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 10, 39, 52, 484643)),
        ),
        migrations.AlterField(
            model_name='routeur',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 10, 39, 52, 511205)),
        ),
    ]
