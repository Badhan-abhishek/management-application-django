from django.contrib import admin
from .models import PersonData, Person
# Register your models here.

admin.site.register(Person)
admin.site.register(PersonData)
