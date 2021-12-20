from django.contrib import admin

# Register your models here.
from .models import Patient, Tests, Meds, Bills
admin.site.register(Patient)
admin.site.register(Tests)
admin.site.register(Meds)
admin.site.register(Bills)
# admin.site.register(Rooms)

