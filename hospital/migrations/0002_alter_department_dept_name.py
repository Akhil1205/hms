# Generated by Django 5.0.1 on 2024-01-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=70),
        ),
    ]
