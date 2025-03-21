# Generated by Django 5.1.4 on 2024-12-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('date_of_visit', models.DateField(auto_now_add=True)),
                ('disease_diagnosed', models.CharField(max_length=255)),
                ('case_details', models.TextField()),
                ('medications', models.TextField()),
            ],
        ),
    ]
