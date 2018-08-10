import re
from socket import gethostbyname, gaierror

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
from django.core.mail import send_mail

from accounts.models import User

class UserCreationForm(forms.ModelForm):
    username                    =   forms.CharField(required=True)
    email                       =   forms.EmailField(required=True)
    password                    =   forms.CharField(widget=forms.PasswordInput(render_value=False))
    re_password                 =   forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model                   =   User
        fields                  =   ('username','email')
    
    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))

    def clean(self):
        if 'password' in self.cleaned_data and 're_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['re_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_("Email"), max_length=254)
    
    def save(self, domain_override=None,
             subject_template_name='userprofile/password_reset_subject.txt',
             email_template_name='userprofile/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        UserModel               =   get_user_model()
        email                   =   self.cleaned_data["email"]
        active_users            =   UserModel._default_manager.filter(email__iexact=email, active=True)
        for user in active_users:
            if not user.has_usable_password():
                continue
            if not domain_override:
                current_site    =   get_current_site(request)
                site_name       =   current_site.name
                domain          =   current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email'         :   user.email,
                'domain'        :   domain,
                'site_name'     :   site_name,
                'uid'           :   urlsafe_base64_encode(force_bytes(user.pk)),
                'user'          :   user,
                'token'         :   token_generator.make_token(user),
                'protocol'      :   'https' if use_https else 'http',
            }
            subject             =   loader.render_to_string(subject_template_name, c)
            subject             =   ''.join(subject.splitlines())
            email               =   loader.render_to_string(email_template_name, c)

            if html_email_template_name:
                html_email      =   loader.render_to_string(html_email_template_name, c)
            else:
                html_email      =   None
            try:
                send_mail(subject, email, from_email, [user.email], html_message=html_email)
            except gaierror:
                print ("Unable to connect the server")