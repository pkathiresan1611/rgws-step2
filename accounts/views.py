from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm, PasswordChangeForm
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

# from .forms import SignUpForm

def home(request):
	try:
		user_is_authenticated = request.user.is_authenticated()
	except TypeError:
		user_is_authenticated = request.user.is_authenticated

	if user_is_authenticated:
		return HttpResponseRedirect(reverse('dashboard'))
	else:
		if request.POST:        
			email                                   =   request.POST.get('email','')
			password                                =   request.POST.get('password','')
			user                                    =   auth.authenticate(email=email,password=password)
			if user is not None:
				if user.active:
					auth.login(request,user)
					return HttpResponseRedirect('/dashboard/')
				else:
					return HttpResponseRedirect('/inactive/')
			messages.warning(request,"Sorry, invalid login!")
	return TemplateResponse(request, 'home.html')

# def dashboard(request):
#     return render(request, 'dashboard.html')

def inactive(request):
	return TemplateResponse(request, 'inactive.html')

def logout(request):
	auth.logout(request)
	return TemplateResponse(request, 'logout.html')

# def inactive(request, template_name="inactive.html"):
# 	return TemplateResponse(request, template_name)

# def logout(request, template_name='logout.html'):
#     auth.logout(request)
#     return TemplateResponse(request, template_name)


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('dashboard')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})