from django.db import models

# Create your models here.
from django.utils import timezone
from time import time
from datetime import datetime

import apps.apps_gv as gv

SALUTATION_CHOICE  = (
	("Mr", "Mr" ),
	("Mrs","Mrs" ),
	("Miss","Miss" ),
	("Ms", "Ms"),
	("Dr", "Dr"),
	("Baby", "Baby"),
	("Master", "Master"),
	("Sister", "Sister"),
	("Brother", "Brother"),
	("Father", "Father"),
	)


GENDER_CHOICE  = (
	("Male", "Male" ),
	("Female","Female" ),
	("Transgender","Transgender" ),
	)

OCCP_CHOICE  = (
	("Self", "Self" ),
	("Salaried","Salaried" ),
	("Student","Student" ),
	("Professional", "Professional"),
	("House wife", "House wife"),
	("Retired", "Retired"),
	("Unemployed", "Unemployed"),
	)

EDU_CHOICE  = (
	("Illiterate", "Illiterate" ),
	("Schooling","Schooling" ),
	("UG","UG" ),
	("PG", "PG"),
	)

INCOME_CHOICE  = (
	("Lower(<10,000/m)", "Lower(<10,000/m)" ),
	("Middle(10,000-30,000/m)","Middle(10,000-30,000/m)" ),
	("Higher(>30,000/m)","Higher(>30,000/m)" ),
	)



class PatientData(models.Model):
	date_of_reg            	= models.DateField(blank=True, null=True)
	salutation             	= models.CharField(max_length=50,blank=True, null=True, choices=SALUTATION_CHOICE)
	name                   	= models.CharField(max_length=255, blank=True, null=True)
	date_of_birth          	= models.DateField(blank=True, null=True)
	age                    	= models.CharField(max_length=255,blank=True, null=True)
	gender                 	= models.CharField(max_length=50,blank=True, null=True, choices=GENDER_CHOICE)
	birth_place            	= models.CharField(max_length=255, blank=True, null=True)
	country_of_birth       	= models.CharField(max_length=50,blank=True, null=True, choices=gv.COUNTRY_CHOICE)
	education              	= models.CharField(max_length=50,blank=True, null=True, choices=EDU_CHOICE)
	occupation             	= models.CharField(max_length=50,blank=True, null=True, choices=OCCP_CHOICE)
	ocp_history            	= models.CharField(max_length=255, blank=True, null=True)
	income                 	= models.CharField(max_length=50,blank=True, null=True, choices=INCOME_CHOICE)
	mobile_no        		= models.CharField(max_length=255,blank=True, null=True)
	email            		= models.CharField(max_length=255, blank=True, null=True)
	pa_address_detail     	= models.TextField(max_length=255,blank=True, null=True)
	pa_city                	= models.CharField(max_length=50,blank=True, null=True, choices=gv.CITY_CHOICE)
	pa_state               	= models.CharField(max_length=50,blank=True, null=True, choices=gv.STATE_CHOICE)
	pa_country             	= models.CharField(max_length=50,blank=True, null=True, choices=gv.COUNTRY_CHOICE)
	ta_address_detail     	= models.TextField(max_length=255,blank=True, null=True)
	ta_city                	= models.CharField(max_length=50,blank=True, null=True, choices=gv.CITY_CHOICE)
	ta_state               	= models.CharField(max_length=50,blank=True, null=True, choices=gv.STATE_CHOICE)
	ta_country             	= models.CharField(max_length=50,blank=True, null=True, choices=gv.COUNTRY_CHOICE)
	rf_salutation  			= models.CharField(max_length=50,blank=True, null=True, choices=SALUTATION_CHOICE)
	rf_name         		= models.CharField(max_length=255, blank=True, null=True)
	specialization         	= models.CharField(max_length=255, blank=True, null=True)
	contact                	= models.CharField(max_length=255,blank=True, null=True)
	address                	= models.TextField(max_length=255, blank=True, null=True)
	upload_file 			= models.ImageField(upload_to='upload_files',blank=True)
	# image                  	= models.FileField(upload_to=image_upload, blank=True)
	notes     				= models.TextField(max_length=255, blank=True, null=True)    

	def __str__(self):
		return u'%s %s %s %s' % (self.name, self.age, self.gender, self.date_of_reg)

	class Meta:
		verbose_name_plural = "Patient Data"