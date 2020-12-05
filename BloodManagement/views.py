from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from .models import Doctor,Department, Patient, BloodPacket, Staff
from .forms import CreateDoctorForm, CreateDepartmentForm, CreatePatientForm, CreateBloodForm, CreateStaffForm
# Views Here

def index(request):
    return render(request,'index.html')

def doctor_create(request):
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            specialization = form.cleaned_data.get('specialization')
            doctor = Doctor.objects.create(
                name=name,
                address= address,
                phone= phone,
                specialization= specialization,
            )
            doctor.save()
            return redirect('bloodmanagement:doctor-detail',pk=doctor.pk)

    else:
        form = CreateDoctorForm()
        return render(request,'doctor_create.html',context={'form':form})

def doctor_detail(request,pk):
    doctor = get_object_or_404(Doctor,pk=pk)
    return render(request,'doctor_detail.html',context={'doctor':doctor})

def doctor_update(request,pk):
    doctor = get_object_or_404(Doctor,pk=pk)
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            specialization = form.cleaned_data.get('specialization')
            Doctor.objects.filter(pk=pk).update(
                name=name,
                address= address,
                phone= phone,
                specialization= specialization,
            )
            doctor = Doctor.objects.get(pk=pk)
            return redirect('bloodmanagement:doctor-detail',pk=doctor.pk)
    else:
        form = CreateDoctorForm(initial={
            'name':doctor.name,
            'address':doctor.address,
            'phone':doctor.phone,
            'specialization':doctor.specialization,
        })
        return render(request,'doctor_create.html',context={'form':form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',context={"doctors":doctors})

def doctor_delete(request,pk):
    if request.method == 'POST':
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return redirect('bloodmanagement:doctor-list')
    
def department_create(request):
    if request.method == 'POST':
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            dept_type = form.cleaned_data.get('department_type')
            capacity = form.cleaned_data.get('capacity')

            department = Department.objects.create(
                name = name,
                dept_type = dept_type,
                capacity = capacity,
            )
            department.save()
            return redirect('bloodmanagement:department-detail',pk=department.pk)
    else:
        form = CreateDepartmentForm()
        return render(request,'department_create.html',context={"form":form})
    
def department_update(request,pk):
    if request.method == 'POST':
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            dept_type = form.cleaned_data.get('department_type')
            capacity = form.cleaned_data.get('capacity')
            Department.objects.filter(pk=pk).update(
                name = name,
                dept_type = dept_type,
                capacity = capacity,
            )
            department=Department.objects.get(pk=pk)
            return redirect('bloodmanagement:department-detail',pk=department.pk)
    else:
        department = Department.objects.get(pk=pk)
        form = CreateDepartmentForm(initial={
            "name":department.name,
            "department_type":department.dept_type,
            "capacity":department.capacity
        })
        return render(request,'department_create.html',context={"form":form})

def department_detail(request,pk):
    department = get_object_or_404(Department,pk=pk)
    return render(request,'department_detail.html',context={'department':department})

def department_list(request):
    departments = Department.objects.all()
    return render(request,'department_list.html',context={"departments":departments})

def department_delete(request,pk):
    if request.method == 'POST':
        deparment = Department.objects.get(pk=pk)
        deparment.delete()
        return redirect('bloodmanagement:department-list')

def patient_create(request):
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            condition = form.cleaned_data.get('condition')
            blood_type = form.cleaned_data.get('blood_type'),
            department = form.cleaned_data.get('department')
            department.capacity -=1
            department.save()
            doctor = form.cleaned_data.get('doctor')
            # doctor = Doctor.objects.get(pk=doctor_id)
            # department = Department.objects.get(pk=department_id)
            patient = Patient.objects.create(
                name=name,
                address= address,
                phone= phone,
                gender = gender,
                condition = condition,
                blood_type = blood_type,
                department = department,
                doctor = doctor,
            )
            patient.save()
            return redirect('bloodmanagement:patient-detail',pk=patient.pk)

    else:
        form = CreatePatientForm()
        return render(request,'patient_create.html',context={'form':form})

def patient_update(request,pk):
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            condition = form.cleaned_data.get('condition')
            blood_type = form.cleaned_data.get('blood_type'),
            department = form.cleaned_data.get('department')
            department.capacity -=1
            department.save()
            doctor = form.cleaned_data.get('doctor')
            Patient.objects.filter(pk=pk).update(
                name=name,
                address= address,
                phone= phone,
                gender = gender,
                condition = condition,
                blood_type = blood_type,
                department = department,
                doctor = doctor,
            )
            patient = Patient.objects.get(pk=pk)
            return redirect('bloodmanagement:patient-detail',pk=patient.pk)

    else:
        patient = Patient.objects.get(pk=pk)
        form = CreatePatientForm(initial={
            "name":patient.name,
            "gender":patient.gender,
            "address":patient.address,
            "phone":patient.phone,
            "condition":patient.condition,
            "department":patient.department,
            "doctor":patient.doctor
        })
        return render(request,'patient_create.html',context={'form':form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request,'patient_list.html',context={"patients":patients})

def patient_detail(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    return render(request,'patient_detail.html',context={'patient':patient})

def patient_delete(request,pk):
    if request.method == 'POST':
        patient = get_object_or_404(Patient,pk=pk)
        department = Department.objects.get(patient=patient)
        department.capacity +=1
        department.save()
        patient.delete()
        return redirect('bloodmanagement:patient-list')

def blood_create(request):
    if request.method == 'POST':
        form = CreateBloodForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data.get('patient')
            donor = form.cleaned_data.get('donor')
            location = form.cleaned_data.get('location')
            blood_type = form.cleaned_data.get('blood_type')
            blood = BloodPacket.objects.create(
                patient=patient,
                donor=donor,
                location=location,
                blood_type=blood_type
            )
            blood.save()
            return redirect('bloodmanagement:blood-detail',pk=blood.pk)

    else:
        form = CreateBloodForm()
        return render(request,'blood_create.html',context={'form':form})
    
def blood_update(request,pk):
    if request.method == 'POST':
        form = CreateBloodForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data.get('patient')
            donor = form.cleaned_data.get('donor')
            location = form.cleaned_data.get('location')
            blood_type = form.cleaned_data.get('blood_type')
            BloodPacket.objects.filter(pk=pk).update(
                patient=patient,
                donor=donor,
                location=location,
                blood_type=blood_type
            )
            blood = BloodPacket.objects.get(pk=pk)
            return redirect('bloodmanagement:blood-detail',pk=blood.pk)

    else:
        blood = BloodPacket.objects.get(pk=pk)
        form = CreateBloodForm(initial={
            "patient":blood.patient,
            "donor":blood.donor,
            "location":blood.location,
            "blood_type":blood.blood_type,
        })
        return render(request,'blood_create.html',context={'form':form})
    
def blood_list(request):
    bloods= BloodPacket.objects.all()
    return render(request,'blood_list.html',context={"bloods":bloods})

def blood_detail(request,pk):
    blood = get_object_or_404(BloodPacket,pk=pk)
    return render(request,'blood_detail.html',context={"blood":blood})

def blood_delete(request,pk):
    if request.method == 'POST':
        blood = get_object_or_404(BloodPacket,pk=pk)
        blood.delete()
        return redirect('bloodmanagement:blood-list')

def staff_create(request):
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            staff = Staff.objects.create(
                name=name,
                phone=phone,
                address=address,
                job=job,
                department=department,
            )
            staff.save()
            return redirect('bloodmanagement:staff-detail',pk=staff.pk)

    else:
        form = CreateStaffForm()
        return render(request,'staff_create.html',context={'form':form})
    
def staff_detail(request,pk):
    staff = Staff.objects.get(pk=pk)
    return render(request,'staff_detail.html',context={"staff":staff})

def staff_list(request):
    staffs = Staff.objects.all()
    return render(request,'staff_list.html',context={"staffs":staffs})

def staff_delete(request,pk):
    if request.method == 'POST':
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('bloodmanagement:staff-list')

def staff_update(request,pk):
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            Staff.objects.filter(pk=pk).update(
                name=name,
                phone=phone,
                address=address,
                job=job,
                department=department,
            )
            staff = Staff.objects.get(pk=pk)
            return redirect('bloodmanagement:staff-detail',pk=staff.pk)

    else:
        staff = Staff.objects.get(pk=pk)
        form = CreateStaffForm(initial={
            "name":staff.name,
            "phone":staff.phone,
            "job":staff.job,
            "address":staff.address,
            "department":staff.department,
        })
        return render(request,'staff_create.html',context={'form':form})
    