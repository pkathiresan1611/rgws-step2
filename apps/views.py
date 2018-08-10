from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template.response import TemplateResponse
from django.conf import settings
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from apps.models import PatientData, SALUTATION_CHOICE, GENDER_CHOICE, EDU_CHOICE, OCCP_CHOICE, INCOME_CHOICE

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

	edu_list = []
	for edu in EDU_CHOICE:
		edu_list.append(edu[0])
	args['edu_list'] = edu_list

	occp_list = []
	for occp in OCCP_CHOICE:
		occp_list.append(occp[0])
	args['occp_list'] = occp_list

	income_list = []
	for inc in INCOME_CHOICE:
		income_list.append(inc[0])
	args['income_list'] = income_list


	city_list = []
	for cty in gv.CITY_CHOICE:
		city_list.append(cty[0])
	args['city_list'] = city_list

	state_list = []
	for st in gv.STATE_CHOICE:
		state_list.append(st[0])
	args['state_list'] = state_list

	country_list = []
	for ctry in gv.COUNTRY_CHOICE:
		country_list.append(ctry[0])
	args['country_list'] = country_list

	if request.POST.get('save'):
		salutation = request.POST.get('salutation')
		name = request.POST.get('name')
		date_of_reg = request.POST.get('date_of_reg')
		date_of_birth = request.POST.get('date_of_birth')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		birth_place = request.POST.get('birth_place')
		country_of_birth = request.POST.get('country_of_birth')
		education = request.POST.get('education')
		occupation = request.POST.get('occupation')
		ocp_history = request.POST.get('ocp_history')
		income = request.POST.get('income')
		mobile_no = request.POST.get('mobile_no')
		email = request.POST.get('email')
		pa_address_detail = request.POST.get('pa_address_detail')
		pa_city = request.POST.get('pa_city')
		pa_state = request.POST.get('pa_state')
		pa_country = request.POST.get('pa_country')
		ta_address_detail = request.POST.get('ta_address_detail')
		ta_city = request.POST.get('ta_city')
		ta_state = request.POST.get('ta_state')
		ta_country = request.POST.get('ta_country')
		rf_salutation = request.POST.get('rf_salutation')
		rf_name = request.POST.get('rf_name')
		specialization = request.POST.get('specialization')
		contact = request.POST.get('contact')
		address = request.POST.get('address')
		# upload_file = request.POST.get('upload_file')
		upload_file = request.FILES.get('upload_files')
		notes = request.POST.get('notes')

		# date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
		date_of_reg = datetime.strptime(date_of_reg, '%d-%m-%Y').strftime('%Y-%m-%d')
		date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y').strftime('%Y-%m-%d')
		# print(salutation)
		# print(name)
		# print(date_of_reg)
		# print(date_of_birth)
		# print(age)
		# print(gender)
		# print(birth_place)
		# print(country_of_birth)
		# print(education)
		# print(occupation)
		# print(ocp_history)
		# print(income)
		# print(mobile_no)
		# print(email)

		# print(pa_address_detail)
		# print(pa_city)
		# print(pa_state)
		# print(pa_country)
		# print(ta_address_detail)
		# print(ta_city)
		# print(ta_state)
		# print(ta_country)
		# print(rf_salutation)
		# print(rf_name)
		# print(specialization)
		# print(contact)
		# print(address)
		# print(upload_file)
		# print(notes)

		patient_create = PatientData.objects.create(salutation=salutation, name=name, date_of_reg=date_of_reg, date_of_birth=date_of_birth, age=age, 
			gender=gender, birth_place=birth_place, country_of_birth=country_of_birth, education=education, occupation=occupation, ocp_history=ocp_history, income=income,
			mobile_no=mobile_no, email=email, pa_address_detail=pa_address_detail, pa_city=pa_city, pa_state=pa_state, pa_country=pa_country, 
			ta_address_detail=ta_address_detail, ta_city=ta_city, ta_state=ta_state, ta_country=ta_country, rf_salutation=rf_salutation, rf_name=rf_name, 
			specialization=specialization, contact=contact, address=address, upload_file=upload_file, notes=notes,)
		messages.success(request, "Successfully created the patient data's!")

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

	edu_list = []
	for edu in EDU_CHOICE:
		edu_list.append(edu[0])
	args['edu_list'] = edu_list

	occp_list = []
	for occp in OCCP_CHOICE:
		occp_list.append(occp[0])
	args['occp_list'] = occp_list

	income_list = []
	for inc in INCOME_CHOICE:
		income_list.append(inc[0])
	args['income_list'] = income_list


	city_list = []
	for cty in gv.CITY_CHOICE:
		city_list.append(cty[0])
	args['city_list'] = city_list

	state_list = []
	for st in gv.STATE_CHOICE:
		state_list.append(st[0])
	args['state_list'] = state_list

	country_list = []
	for ctry in gv.COUNTRY_CHOICE:
		country_list.append(ctry[0])
	args['country_list'] = country_list

	patient_id = get_object_or_404(PatientData, id=patient_id)
	args['patient_id'] = patient_id

	if request.POST.get('save'):
		salutation = request.POST.get('salutation')
		name = request.POST.get('name')
		date_of_reg = request.POST.get('date_of_reg')
		date_of_birth = request.POST.get('date_of_birth')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		birth_place = request.POST.get('birth_place')
		country_of_birth = request.POST.get('country_of_birth')
		education = request.POST.get('education')
		occupation = request.POST.get('occupation')
		ocp_history = request.POST.get('ocp_history')
		income = request.POST.get('income')
		mobile_no = request.POST.get('mobile_no')
		email = request.POST.get('email')
		pa_address_detail = request.POST.get('pa_address_detail')
		pa_city = request.POST.get('pa_city')
		pa_state = request.POST.get('pa_state')
		pa_country = request.POST.get('pa_country')
		ta_address_detail = request.POST.get('ta_address_detail')
		ta_city = request.POST.get('ta_city')
		ta_state = request.POST.get('ta_state')
		ta_country = request.POST.get('ta_country')
		rf_salutation = request.POST.get('rf_salutation')
		rf_name = request.POST.get('rf_name')
		specialization = request.POST.get('specialization')
		contact = request.POST.get('contact')
		address = request.POST.get('address')
		# upload_file = request.POST.get('upload_file')
		upload_file = request.FILES.get('upload_files')
		notes = request.POST.get('notes')

		# date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
		date_of_reg = datetime.strptime(date_of_reg, '%d-%m-%Y').strftime('%Y-%m-%d')
		date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y').strftime('%Y-%m-%d')

		
		patient_id.salutation = salutation
		patient_id.name = name
		patient_id.date_of_reg = date_of_reg
		patient_id.date_of_birth = date_of_birth
		patient_id.age = age
		patient_id.gender = gender
		patient_id.birth_place = birth_place

		patient_id.country_of_birth = country_of_birth
		patient_id.education = education
		patient_id.occupation = occupation
		patient_id.ocp_history = ocp_history
		patient_id.mobile_no = mobile_no
		patient_id.email = email
		patient_id.pa_address_detail = pa_address_detail
		patient_id.pa_city = pa_city
		patient_id.pa_state = pa_state
		patient_id.pa_country = pa_country
		patient_id.ta_address_detail = ta_address_detail
		patient_id.ta_city = ta_city
		patient_id.ta_state = ta_state
		patient_id.ta_country = ta_country

		patient_id.rf_salutation = rf_salutation
		patient_id.rf_name = rf_name
		patient_id.specialization = specialization
		patient_id.contact = contact
		patient_id.address = address
		patient_id.upload_file = upload_file
		patient_id.notes = notes
		patient_id.save()
        # return HttpResponseRedirect(reverse('dashboard'))
		messages.success(request, "Successfully Updated the patient data's!")

	return render(request, 'edit_patient.html', args)


@login_required
def delete_patient(request, patient_id):
	patient_id = get_object_or_404(PatientData, id=patient_id)
	patient_id.delete()
	return HttpResponseRedirect(reverse('dashboard'))
