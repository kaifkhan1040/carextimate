# Generated by Django 5.2 on 2025-05-10 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0010_servicecategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tyre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.carmodel')),
            ],
        ),
    ]
