# Generated by Django 2.0.7 on 2018-08-13 15:59

import apps.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20180810_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='upload_file',
            field=models.ImageField(blank=True, upload_to=apps.models.upload_files),
        ),
    ]
