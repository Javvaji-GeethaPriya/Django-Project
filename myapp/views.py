from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm

# View to display the home page
def home(request):
    return render(request, 'myapp/home.html')

# Department Views
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'myapp/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'myapp/department_form.html', {'form': form})

#update  department
def department_update(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'myapp/department_form.html', {'form': form})

#delete a dept
def department_delete(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'myapp/department_confirm_delete.html', {'department': department})

# Employee Views

#View to list all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'myapp/employee_list.html', {'employees': employees})

# create a new Employee 
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'myapp/employee_form.html', {'form': form})

# update a new employee
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'myapp/employee_form.html', {'form': form})

# delete employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'myapp/employee_confirm_delete.html', {'employee': employee})
