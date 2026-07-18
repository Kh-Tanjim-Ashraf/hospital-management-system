from django.contrib import admin
from doctor.models import Doctor, Department, Specialization


admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Specialization)