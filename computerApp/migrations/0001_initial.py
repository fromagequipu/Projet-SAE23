# Generated by Django 4.0.3 on 2022-05-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('ip_address', models.CharField(max_length=20)),
                ('mac', models.CharField(max_length=20)),
                ('famille', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
