# Generated by Django 5.2 on 2025-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0009_country_symbole'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='image',
            field=models.ImageField(default=1, upload_to='service/'),
            preserve_default=False,
        ),
    ]
