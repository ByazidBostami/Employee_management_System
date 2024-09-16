from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required, permission_required

# View to list all employees (Homepage)
@login_required
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

# View to add a new employee
@login_required
@permission_required('employee.add_employee', raise_exception=True)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# View to update employee information
@login_required
@permission_required('employee.change_employee', raise_exception=True)
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            # Prevent updating salary and designation
            employee.name = form.cleaned_data.get('name')
            employee.address = form.cleaned_data.get('address')
            employee.phone = form.cleaned_data.get('phone')
            employee.description = form.cleaned_data.get('description')
            employee.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# View to delete an employee
@login_required
@permission_required('employee.delete_employee', raise_exception=True)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

# View to list employees for Update/Delete functionality (not homepage)
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
