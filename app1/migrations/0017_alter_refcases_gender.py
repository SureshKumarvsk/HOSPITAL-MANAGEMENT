# Generated by Django 5.1.4 on 2024-12-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_refcases_address_alter_refcases_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refcases',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]
