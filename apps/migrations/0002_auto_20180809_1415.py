# Generated by Django 2.0.7 on 2018-08-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='patientdata',
            name='upload_file',
            field=models.ImageField(blank=True, upload_to='upload_files'),
        ),
    ]