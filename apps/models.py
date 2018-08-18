from django.db import models

# Create your models here.
from django.utils.text import slugify
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




# def file_upload(instance,filename):
#     return "file_upload/%s_%s"%(str(time()).replace('.','_'),filename)

def file_upload(instance, filename):
    title = instance.id
    slug = slugify(title)
    return "file_upload/%s-%s" % (slug, filename)


class PatientData(models.Model):
	date_of_reg            	= models.DateField(blank=True, null=True)
	salutation             	= models.CharField(max_length=50,blank=True, null=True, choices=SALUTATION_CHOICE)
	name                   	= models.CharField(max_length=255, blank=True, null=True)
	age                    	= models.CharField(max_length=255,blank=True, null=True)
	gender                 	= models.CharField(max_length=50,blank=True, null=True, choices=GENDER_CHOICE)
	mobile_no        		= models.CharField(max_length=255,blank=True, null=True)
	email            		= models.CharField(max_length=255, blank=True, null=True)
	pa_address_detail     	= models.TextField(max_length=255,blank=True, null=True)
	pa_city                	= models.CharField(max_length=50,blank=True, null=True, choices=gv.CITY_CHOICE)
	address                	= models.TextField(max_length=255, blank=True, null=True)
	notes     				= models.TextField(max_length=255, blank=True, null=True)    

	def __str__(self):
		return u'%s-%s-%s-%s' % (self.name, self.age, self.gender, self.date_of_reg)

	class Meta:
		verbose_name_plural = "Patient Data"


class PatientFiles(models.Model):
	patient		   		   = models.ForeignKey(PatientData, verbose_name='Patient',on_delete=models.CASCADE,blank=True, null=True)
	upload_files           = models.FileField(upload_to=file_upload, blank=True, null=True)

	def __str__(self):
		return u'%s---%s' % (self.patient.name, self.upload_files)

	class Meta:
		verbose_name_plural = "Patient Files"


class Diagnosis(models.Model):
	patient		   		   	= models.ForeignKey(PatientData, verbose_name='Patient',on_delete=models.CASCADE,blank=True, null=True)
	diagnosis             	= models.TextField(max_length=255,blank=True,null=True)

	def __str__(self):
		return u'%s-%s' % (self.patient.name, self.diagnosis)

	class Meta:
		verbose_name_plural = "Diagnosis"


class Prescription(models.Model):
	pateint_diagnosis		= models.ForeignKey(Diagnosis, verbose_name='Diagnosis',on_delete=models.CASCADE,blank=True, null=True)
	tablet                  = models.CharField(max_length=255,blank=True,null=True)
	mrg_count               = models.CharField(max_length=255,blank=True,null=True)
	aft_count               = models.CharField(max_length=255,blank=True,null=True)
	nit_count        		= models.CharField(max_length=255,blank=True,null=True)
	tab_qty            		= models.CharField(max_length=255,blank=True,null=True)
	
	def __str__(self):
		return u'%s-%s-%s' % (self.pateint_diagnosis.patient.name, self.pateint_diagnosis.diagnosis, self.tablet)

	class Meta:
		verbose_name_plural = "Prescription"

