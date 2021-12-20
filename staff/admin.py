from django.contrib import admin

# Register your models here.
from .models import Department, Staff, Specialities


admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Specialities)


