from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from apps import views
from django.conf import settings
import django.views.static as django_static_view


urlpatterns = [
	url(r'^site_media/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.MEDIA_ROOT }),
	url(r'^static/admin/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.STATIC_ROOT }),

	path('',accounts_views.home,name='home'),
 	path('inactive/', accounts_views.inactive, name="inactive"),
    path('logout/', accounts_views.logout, name="logout"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('edit_patient/<int:patient_id>/',views.edit_patient,name='edit_patient'),
    path('delete_patient/<int:patient_id>/',views.delete_patient,name='delete_patient'),
    path('edit_patient/<int:patient_id>/delete/<int:file_id>/',views.delete_pfile,name='delete_pfile'),
    path('add_prescription/<int:patient_id>/',views.add_prescription,name='add_prescription'),
    path('add_prescription/<int:patient_id>/delete_pres/<int:prescription_id>/',views.delete_prescription,name='delete_prescription'),
    path('certificates/',views.certificates,name='certificates'),
    path('medical_certificate/',views.medical_certificate,name='medical_certificate'),
    path('fitness_certificate/',views.fitness_certificate,name='fitness_certificate'),
    path('med_fitness_certificate/',views.med_fitness_certificate,name='med_fitness_certificate'),
    path('certificate_of_physical/',views.certificate_of_physical,name='certificate_of_physical'),
    path('physical_fitness/',views.physical_fitness,name='physical_fitness'),
    path('life_certificate/',views.life_certificate,name='life_certificate'),
    

    path('admin/', admin.site.urls),
]
