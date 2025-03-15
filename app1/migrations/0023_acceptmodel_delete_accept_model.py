# Generated by Django 5.1.4 on 2024-12-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_accept_model_rename_decline_decline_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('disease_diagnosed', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=100)),
                ('message_to_doctor', models.TextField()),
                ('doctor', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Accept_Model',
        ),
    ]
