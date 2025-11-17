from django.shortcuts import render, redirect


from .models import Employee, Department


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})



def add_employee(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('date_of_birth')
        dept=request.POST.get('dept')
        salary=request.POST.get('salary')
        bonus=request.POST.get('bonus')
        role=request.POST.get('role')
        hire_date=request.POST.get(' hire_date')
        status=request.POST.get('status')


        # try:
        #     department =Department.objects.get(id=dept_id)
        #     role = Role.objects.get(id=role_id)
        #
        #
        #     Employee.objects.create(
        #         first_name=first_name,
        #         last_name=last_name,
        #         gender=gender,
        #         email=email,
        #         phone=phone,
        #         address=address,
        #         date_of_birth=date_of_birth,
        #         dept=dept,
        #         salary=salary,
        #         bonus=bonus,
        #         role=role,
        #         hire_date=hire_date,
        #         status=status,
        #
        #
        #     )

        #     try:
        #         messages.success(request, 'Employee record added')
        #         return redirect('add_employees')
        #     except Department.DoesNotExist:
        #         messages.error(request, 'Invalid department')
        #     except Role.DoesNotExist:
        #         messages.error(request, 'Invalid role')
        #
        #     except Exception as e:
        #         messages.error(request,'error:{str(e)}')
        #
        # department=Department.objects.all()
        # role=Role.objects.all()
        # return  render(request, template_name:'add_employee.html', context={'department': department,'roles':roles)