from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'salary', 'designation', 'description']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # If instance.pk is None, the form is for creating a new employee
        if self.instance.pk:  # Updating an existing employee
            self.fields['salary'].widget.attrs['readonly'] = True
            self.fields['designation'].widget.attrs['readonly'] = True

        # Adding placeholder text for better user experience
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter phone number'})
        self.fields['salary'].widget.attrs.update({'placeholder': 'Enter salary'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Add a brief description'})

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        if len(phone) != 10:  # Optional: Check for specific length, e.g., 10 digits
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")
        return salary

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name should have at least 3 characters.")
        return name
