from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User

class UserCreationForm(forms.ModelForm):
    email               =   forms.CharField(label='email', widget=forms.TextInput)
    password1           =   forms.CharField(label='Password', widget=forms.PasswordInput)
    password2           =   forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model           =   User
        fields          =   ('username','email','active')

    def clean_password2(self):
        password1       =   self.cleaned_data.get("password1")
        password2       =   self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user            =   super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password            =   ReadOnlyPasswordHashField()
    class Meta:
        model           =   User
        fields          =   ('username','email','password','is_admin', 'active',)

    def clean_password(self):
        return self.initial["password"]

class MyUserAdmin(UserAdmin):
    form                = UserChangeForm
    add_form            = UserCreationForm
    list_display        = ('username','email','is_admin','active',)
    list_filter         = ('is_admin',)
    fieldsets           = (
                            ('User', {'fields': ('username','email','password','created_by', 'updated_by', )}),
                            ('Permissions', {'fields': ('is_admin','active',)}),
                            )
    add_fieldsets       = (
                            (None, {
                                'classes': ('wide',),
                                'fields': ('username','email','password1', 'password2', 'active','created_by', 'updated_by', )}
                                ),
                            )
    search_fields       = ('username','email',)
    ordering            = ('username','email',)
    filter_horizontal   = ()


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)