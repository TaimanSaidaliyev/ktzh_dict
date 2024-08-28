from dal import autocomplete
from .models import Division, Employee
from django import forms


class DivisionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Division.objects.none()

        queryset = Division.objects.all()

        department_id = self.forwarded.get('department', None)

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'division': autocomplete.ModelSelect2(url='division-autocomplete', forward=['department']),
        }

