# Generated by Django 2.2.6 on 2019-11-21 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsp_full_name', models.CharField(max_length=100)),
                ('dsp_tel_no', models.CharField(max_length=12)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('point_of_sale', models.CharField(max_length=50)),
                ('address_of_sale', models.CharField(max_length=50)),
                ('owner_full_name', models.CharField(max_length=100)),
                ('owner_tel_no', models.CharField(max_length=12)),
                ('owner_id_number', models.CharField(max_length=8)),
                ('business_no', models.CharField(max_length=30)),
                ('kra_pin', models.CharField(max_length=15)),
                ('sup_full_name', models.CharField(max_length=100)),
                ('sup_tel_no', models.CharField(max_length=12)),
                ('sup_id_number', models.CharField(max_length=8)),
                ('cashier_full_name', models.CharField(max_length=100)),
                ('cashier_tel_no', models.CharField(max_length=12)),
                ('cashier_id_number', models.CharField(max_length=8)),
                ('read', models.BooleanField(default=False)),
                ('products', models.CharField(max_length=1)),
            ],
        ),
    ]
