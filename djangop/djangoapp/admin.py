from django.contrib import admin
from djangoapp.models import UserData
# Register your models here.
from djangoapp.models import Student

admin.site.register(Student)
admin.site.register(UserData)


