# Generated by Django 5.0.1 on 2024-01-10 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('patient_name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('disease', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='visited_dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', to_field='phone_number')),
            ],
        ),
    ]
