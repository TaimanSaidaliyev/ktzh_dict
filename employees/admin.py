from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Employee, Position, Department, EmployeeStatus, Division
from .forms import *
from django.forms import widgets


class PositionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('serial_number', 'name')
    ordering = ('serial_number',)


class DepartmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('serial_number', 'name')
    ordering = ('serial_number',)


class EmployeeStatusAdminForm(forms.ModelForm):
    class Meta:
        model = EmployeeStatus
        fields = '__all__'
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }


class EmployeeStatusAdmin(admin.ModelAdmin):
    form = EmployeeStatusAdminForm
    list_display = ['name', 'color']
    ordering = ('serial_number',)


class EmployeeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('serial_number', 'first_name', 'last_name', 'position', 'department')
    form = EmployeeForm
    ordering = ('serial_number',)


class DivisionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'department')
    ordering = ('serial_number',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
