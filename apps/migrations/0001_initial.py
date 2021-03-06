# Generated by Django 2.0.7 on 2018-08-16 13:09

import apps.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_reg', models.DateField(blank=True, null=True)),
                ('salutation', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr'), ('Baby', 'Baby'), ('Master', 'Master'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Father', 'Father')], max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=50, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('pa_address_detail', models.TextField(blank=True, max_length=255, null=True)),
                ('pa_city', models.CharField(blank=True, choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bengaluru', 'Bengaluru'), ('Ahmedabad', 'Ahmedabad'), ('Hyderabad', 'Hyderabad'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata'), ('Pune', 'Pune'), ('Jaipur', 'Jaipur'), ('Surat', 'Surat'), ('Lucknow', 'Lucknow'), ('Kanpur', 'Kanpur'), ('Nagpur', 'Nagpur'), ('Patna', 'Patna'), ('Indore', 'Indore'), ('Thane', 'Thane'), ('Bhopal', 'Bhopal'), ('Visakhapatnam', 'Visakhapatnam'), ('Vadodara', 'Vadodara'), ('Firozabad', 'Firozabad'), ('Ludhiana', 'Ludhiana'), ('Rajkot', 'Rajkot'), ('Agra', 'Agra'), ('Siliguri', 'Siliguri'), ('Nashik', 'Nashik'), ('Faridabad', 'Faridabad'), ('Patiala', 'Patiala'), ('Meerut', 'Meerut'), ('Kalyan-Dombivali', 'Kalyan-Dombivali'), ('Vasai-Virar', 'Vasai-Virar'), ('Varanasi', 'Varanasi'), ('Srinagar', 'Srinagar'), ('Dhanbad', 'Dhanbad'), ('Jodhpur', 'Jodhpur'), ('Amritsar', 'Amritsar'), ('Raipur', 'Raipur'), ('Allahabad', 'Allahabad'), ('Coimbatore', 'Coimbatore'), ('Jabalpur', 'Jabalpur'), ('Gwalior', 'Gwalior'), ('Vijayawada', 'Vijayawada'), ('Madurai', 'Madurai'), ('Guwahati', 'Guwahati'), ('Chandigarh', 'Chandigarh'), ('Hubli-Dharwad', 'Hubli-Dharwad'), ('Amroha', 'Amroha'), ('Moradabad', 'Moradabad'), ('Gurgaon', 'Gurgaon'), ('Aligarh', 'Aligarh'), ('Solapur', 'Solapur'), ('Ranchi', 'Ranchi'), ('Jalandhar', 'Jalandhar'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Bhubaneswar', 'Bhubaneswar'), ('Salem', 'Salem'), ('Warangal', 'Warangal'), ('Mira-Bhayandar', 'Mira-Bhayandar'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Bhiwandi', 'Bhiwandi'), ('Saharanpur', 'Saharanpur')], max_length=50, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Data',
            },
        ),
        migrations.CreateModel(
            name='PatientFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_files', models.FileField(blank=True, null=True, upload_to=apps.models.file_upload)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.PatientData', verbose_name='Patient')),
            ],
            options={
                'verbose_name_plural': 'Patient Files',
            },
        ),
    ]
