from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response
from django.template.response import TemplateResponse
from django.conf import settings
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_patient(request):
    return render(request, 'add_patient.html')

