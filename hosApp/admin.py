from django.contrib import admin

from .models import Hospital, Report, Patient, Bank

admin.site.register(Hospital)
admin.site.register(Report)
admin.site.register(Patient)
admin.site.register(Bank)
