from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('patient-reg', views.patient_reg, name='patient-reg'),
    path('register', views.register, name='register'),
    path('details', views.details, name='details'),
    path('api', views.api, name='api'),
]
