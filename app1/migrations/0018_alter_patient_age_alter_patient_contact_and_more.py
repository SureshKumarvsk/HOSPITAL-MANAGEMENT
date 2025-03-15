# Generated by Django 5.1.4 on 2024-12-29 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_refcases_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.CharField(default=datetime.date.today, max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='refcases',
            name='date',
            field=models.CharField(default=datetime.date.today, max_length=200),
        ),
    ]
