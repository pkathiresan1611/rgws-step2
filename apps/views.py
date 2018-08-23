from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template.response import TemplateResponse
from django.conf import settings
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from apps.models import PatientData, SALUTATION_CHOICE, GENDER_CHOICE, PatientFiles, Diagnosis, Prescription

from django.utils import timezone
from time import time
from datetime import datetime
import apps.apps_gv as gv

@login_required
def dashboard(request):
	args = {}

	patient_list = PatientData.objects.all().order_by('-id')
	args['patient_list'] = patient_list
	return render(request, 'dashboard.html', args)


@login_required
def add_patient(request):
	args = {}

	salutation_list = []
	for sal in SALUTATION_CHOICE:
		salutation_list.append(sal[0])
	args['salutation_list'] = salutation_list

	gender_list = []
	for gen in GENDER_CHOICE:
		gender_list.append(gen[0])
	args['gender_list'] = gender_list


	city_list = []
	for cty in gv.CITY_CHOICE:
		city_list.append(cty[0])
	args['city_list'] = city_list


	if request.POST.get('save'):
		salutation = request.POST.get('salutation')
		name = request.POST.get('name')
		date_of_reg = request.POST.get('date_of_reg')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		mobile_no = request.POST.get('mobile_no')
		email = request.POST.get('email')
		pa_address_detail = request.POST.get('pa_address_detail')
		pa_city = request.POST.get('pa_city')
		address = request.POST.get('address')
		notes = request.POST.get('notes')
		date_of_reg = datetime.strptime(date_of_reg, '%d-%m-%Y').strftime('%Y-%m-%d')


		patient_create = PatientData.objects.create(salutation=salutation, name=name, date_of_reg=date_of_reg, age=age, gender=gender, mobile_no=mobile_no, 
			email=email, pa_address_detail=pa_address_detail, pa_city=pa_city, address=address, notes=notes,)
		messages.success(request, "Successfully created the patient data's!")

		upload_files = request.FILES.getlist('upload_files')
		if upload_files !=[]:
			for upf in upload_files:
				patientfiles = PatientFiles.objects.create(patient=PatientData.objects.get(id=patient_create.id), upload_files=upf,)
				print(patientfiles.upload_files)

	return render(request, 'add_patient.html', args)


@login_required
def edit_patient(request, patient_id):
	args = {}

	salutation_list = []
	for sal in SALUTATION_CHOICE:
		salutation_list.append(sal[0])
	args['salutation_list'] = salutation_list

	gender_list = []
	for gen in GENDER_CHOICE:
		gender_list.append(gen[0])
	args['gender_list'] = gender_list


	city_list = []
	for cty in gv.CITY_CHOICE:
		city_list.append(cty[0])
	args['city_list'] = city_list


	patient_id = get_object_or_404(PatientData, id=patient_id)
	args['patient_id'] = patient_id

	pfiles_list = PatientFiles.objects.filter(patient=patient_id).order_by('-id')
	args['pfiles_list'] = pfiles_list

	if request.POST.get('save'):
		salutation = request.POST.get('salutation')
		name = request.POST.get('name')
		date_of_reg = request.POST.get('date_of_reg')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		mobile_no = request.POST.get('mobile_no')
		email = request.POST.get('email')
		pa_address_detail = request.POST.get('pa_address_detail')
		pa_city = request.POST.get('pa_city')
		address = request.POST.get('address')
		notes = request.POST.get('notes')
		date_of_reg = datetime.strptime(date_of_reg, '%d-%m-%Y').strftime('%Y-%m-%d')

		
		patient_id.salutation = salutation
		patient_id.name = name
		patient_id.date_of_reg = date_of_reg
		patient_id.age = age
		patient_id.gender = gender
		patient_id.mobile_no = mobile_no
		patient_id.email = email
		patient_id.pa_address_detail = pa_address_detail
		patient_id.pa_city = pa_city
		patient_id.address = address
		patient_id.notes = notes
		patient_id.save()

		upload_files = request.FILES.getlist('upload_files')
		if upload_files !=[]:
			for upf in upload_files:
				patientfiles = PatientFiles.objects.create(patient=patient_id, upload_files=upf,)
				print(patientfiles.upload_files)
		messages.success(request, "Successfully Updated the patient data's!")

	return render(request, 'edit_patient.html', args)


@login_required
def delete_patient(request, patient_id):
	patient_id = get_object_or_404(PatientData, id=patient_id)
	patient_id.delete()
	messages.success(request, "Successfully Delete the patient data")
	return HttpResponseRedirect(reverse('dashboard'))


@login_required
def delete_pfile(request,patient_id,file_id):
    patient_id = get_object_or_404(PatientData, id=patient_id)
    file_id = get_object_or_404(PatientFiles, id=file_id)
    file_id.delete()
    messages.success(request, "Successfully delete the patient file")
    return HttpResponseRedirect('/edit_patient/%s/'%(patient_id.id))



@login_required
def add_prescription(request, patient_id):
	args = {}

	patient_id = get_object_or_404(PatientData, id=patient_id)
	args['patient_id'] = patient_id
	diagnosis_list = Diagnosis.objects.filter(patient=patient_id)
	prescription_list = Prescription.objects.filter(pateint_diagnosis__in=diagnosis_list).order_by('-pateint_diagnosis')
	args['prescription_list'] = prescription_list
	try:
		diagnosis_lat_list = Diagnosis.objects.filter(patient=patient_id).latest('id')
		args['diagnosis_lat_list'] = diagnosis_lat_list
		prescription_lat_list = Prescription.objects.filter(pateint_diagnosis=diagnosis_lat_list)
		args['prescription_lat_list'] = prescription_lat_list
	except:
		pass
	
	if request.POST.get('save'):
		diagnosis = request.POST.getlist('diagnosis')
		tablet = request.POST.getlist('tablet')
		mrg_count = request.POST.getlist('mrg_count')
		aft_count = request.POST.getlist('aft_count')
		nit_count = request.POST.getlist('nit_count')
		tab_qty = request.POST.getlist('tab_qty')

		if diagnosis != []:
			for d in diagnosis:
				diagnosis_create = Diagnosis.objects.create(patient=patient_id, diagnosis=d,)

		if tablet != []:
			for t, m, a, n, tq in zip(tablet, mrg_count, aft_count, nit_count, tab_qty):
				prescription = Prescription.objects.create(pateint_diagnosis=Diagnosis.objects.get(id=diagnosis_create.id), tablet=t, mrg_count=m, aft_count=a, 
					nit_count=n, tab_qty=tq,)
		messages.success(request, "Successfully prescription added")
	
	return render(request, 'add_prescription.html', args)


@login_required
def delete_prescription(request,patient_id,prescription_id):
    patient_id = get_object_or_404(PatientData, id=patient_id)
    prescription_id = get_object_or_404(Prescription, id=prescription_id)
    prescription_id.delete()
    messages.success(request, "Successfully delete the prescription")
    return HttpResponseRedirect('/add_prescription/%s/'%(patient_id.id))


@login_required
def certificates(request):
	args = {}

	return render(request, 'certificates.html', args)


@login_required
def medical_certificate(request):
	args = {}
	
	return render(request, 'medical_certificate.html', args)


@login_required
def fitness_certificate(request):
	args = {}
	
	return render(request, 'fitness_certificate.html', args)


@login_required
def med_fitness_certificate(request):
	args = {}
	
	return render(request, 'med_fitness_certificate.html', args)

@login_required
def certificate_of_physical(request):
	args = {}
	
	return render(request, 'certificate_of_physical.html', args)

@login_required
def physical_fitness(request):
	args = {}
	
	return render(request, 'physical_fitness.html', args)


@login_required
def life_certificate(request):
	args = {}
	
	return render(request, 'life_certificate.html', args)



