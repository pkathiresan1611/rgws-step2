from django.db import models

# Create your models here.
from django.utils import timezone
from time import time
from datetime import datetime

class PatientData(models.Model):
	date_of_reg            	= models.DateField(blank=True, null=True)
	salutation             	= models.CharField(max_length=255,blank=True, null=True)
	
	name                   	= models.CharField(max_length=255, blank=True, null=True)
	date_of_birth          	= models.DateField(blank=True, null=True)
	age                    	= models.IntegerField(blank=True, null=True)
	gender                 	= models.CharField(max_length=255,blank=True, null=True)
	birth_place            	= models.CharField(max_length=255, blank=True, null=True)
	country_of_birth       	= models.CharField(max_length=255,blank=True, null=True)
	education              	= models.CharField(max_length=255,blank=True, null=True)
	occupation             	= models.CharField(max_length=255,blank=True, null=True)
	ocp_history            	= models.CharField(max_length=255, blank=True, null=True)
	income                 	= models.CharField(max_length=255, blank=True, null=True)
	mobile_no        		= models.CharField(max_length=255,blank=True, null=True)
	email            		= models.CharField(max_length=255, blank=True, null=True)
	pa_address_detail     	= models.TextField(max_length=255,blank=True, null=True)
	pa_city                	= models.CharField(max_length=255,blank=True, null=True)
	pa_state               	= models.CharField(max_length=255,blank=True, null=True)
	pa_country             	= models.CharField(max_length=255,blank=True, null=True)
	ta_address_detail     	= models.TextField(max_length=255,blank=True, null=True)
	ta_city                	= models.CharField(max_length=255,blank=True, null=True)
	ta_state               	= models.CharField(max_length=255,blank=True, null=True)
	ta_country             	= models.CharField(max_length=255, blank=True, null=True)
	rf_salutation  			= models.CharField(max_length=255,blank=True, null=True)
	rf_name         		= models.CharField(max_length=255, blank=True, null=True)
	specialization         	= models.CharField(max_length=255, blank=True, null=True)
	contact                	= models.CharField(max_length=255,blank=True, null=True)
	address                	= models.TextField(max_length=255, blank=True, null=True)
	upload_file 			= models.ImageField(upload_to='upload_files',blank=True)
	# image                  	= models.FileField(upload_to=image_upload, blank=True)
	notes     				= models.TextField(max_length=255, blank=True, null=True)    

	def __str__(self):
		return u'%s %s %s' % (self.date_of_reg, self.name, self.age, self.gender)

	class Meta:
		verbose_name_plural = "Patient Data"