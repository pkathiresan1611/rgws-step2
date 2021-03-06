# Generated by Django 2.0.7 on 2018-08-18 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField(blank=True, max_length=255, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.PatientData', verbose_name='Patient')),
            ],
            options={
                'verbose_name_plural': 'Diagnosis',
            },
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient',
        ),
        migrations.AddField(
            model_name='prescription',
            name='pateint_diagnosis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Diagnosis', verbose_name='Diagnosis'),
        ),
    ]
