from django.contrib import admin
from .models import Doctor, Department, Patient, Staff, BloodPacket
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(BloodPacket)