from django.contrib import admin

# Register your models here.
from apps.models import PatientData

class PatientDataAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender', 'date_of_reg')

admin.site.register(PatientData, PatientDataAdmin)

