from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id_no','name','salary','location')

admin.site.register(Employee,EmployeeAdmin)