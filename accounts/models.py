import os

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self,username, email,password=None, active=True):
        if not email:
            raise ValueError('Users must have an email address')

        user            = self.model(username=username, email=email, active = active)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,password):
        user            = self.create_user(username=username, email=email, password=password)
        user.is_admin   = True
        user.active     = True
        user.save(using=self._db)
        return user

        
class User(AbstractBaseUser):
	username            =   models.CharField(verbose_name='Username',max_length=255, blank=True, null=True)
	email 		        = 	models.EmailField(verbose_name='Email',max_length=255,unique=True,)
	created_at 	        = 	models.DateTimeField(verbose_name='Created_at',auto_now_add=True)
	created_by 	        = 	models.ForeignKey('User',related_name='+',on_delete=models.CASCADE, blank=True, null=True)
	updated_at 	        = 	models.DateTimeField(verbose_name='Updated_at',auto_now=True)
	updated_by 	        = 	models.ForeignKey('User',verbose_name='Updated_by',on_delete=models.CASCADE, blank=True, null=True)
	active		        =	models.BooleanField(verbose_name='Active',default =True) 
	is_admin 	        = 	models.BooleanField(default=False)
	objects 	        = 	MyUserManager()

	class Meta:
	    verbose_name_plural = u'User'

	USERNAME_FIELD      = 'email'

	REQUIRED_FIELDS     = ['username',]


	def get_full_name(self):
	    return self.email

	def get_short_name(self):
	    return self.email

	def __str__(self):
	    return self.email

	def has_perm(self, perm, obj=None):
	    return True

	def has_module_perms(self, app_label):
	    return True

	@property
	def is_staff(self):
	    return self.is_admin

	def __str__(self):
	    return self.email