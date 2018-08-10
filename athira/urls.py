from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from apps import views

urlpatterns = [
	path('',accounts_views.home,name='home'),
 	path('inactive/', accounts_views.inactive, name="inactive"),
    path('logout/', accounts_views.logout, name="logout"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('admin/', admin.site.urls),
]
