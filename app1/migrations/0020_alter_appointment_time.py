# Generated by Django 5.1.4 on 2024-12-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
