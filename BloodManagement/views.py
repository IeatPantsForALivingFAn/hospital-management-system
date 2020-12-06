from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from .models import Doctor,Department, Patient, BloodPacket, Staff
from .forms import CreateDoctorForm, CreateDepartmentForm, CreatePatientForm, CreateBloodForm, CreateStaffForm
# Views Here

def index(request):
    """
    renders the home page
    """
    return render(request,'index.html')

def doctor_create(request):
    """
    renders the form on GET, adds a row to Doctor table on POST
    """
    if request.method == 'POST':
        # get the form data
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
            # redirects to detail page of the doctor
            return redirect('bloodmanagement:doctor-detail',pk=doctor.pk)

    else:
        # get the form
        form = CreateDoctorForm()
        return render(request,'doctor_create.html',context={'form':form})

def doctor_detail(request,pk):
    """
    render the detail page
    """
    # get the doctor object
    doctor = get_object_or_404(Doctor,pk=pk)
    return render(request,'doctor_detail.html',context={'doctor':doctor})

def doctor_update(request,pk):
    """
    reders the Update page on get, Updates the data 
    on doctor object on POST
    """
    # get the required doctor object
    doctor = get_object_or_404(Doctor,pk=pk)
    if request.method == 'POST':
        # get the input form
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            # get valid data
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            specialization = form.cleaned_data.get('specialization')
            # update the doctor row
            Doctor.objects.filter(pk=pk).update(
                name=name,
                address= address,
                phone= phone,
                specialization= specialization,
            )
            # get the updated doctor object
            doctor = Doctor.objects.get(pk=pk)
            # redirect to the detail page
            return redirect('bloodmanagement:doctor-detail',pk=doctor.pk)
    else:
        # set the form with initial data of the 
        # required doctor object
        form = CreateDoctorForm(initial={
            'name':doctor.name,
            'address':doctor.address,
            'phone':doctor.phone,
            'specialization':doctor.specialization,
        })
        return render(request,'doctor_create.html',context={'form':form})

def doctor_list(request):
    """
    renders the doctor list page
    """
    # get all the doctor objects
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',context={"doctors":doctors})

def doctor_delete(request,pk):
    """deletes the doctor object"""
    if request.method == 'POST':
        # get the required doctor object
        doctor = Doctor.objects.get(pk=pk)
        # delete the doctor
        doctor.delete()
        # redirect to doctor list page
        return redirect('bloodmanagement:doctor-list')
    
def department_create(request):
    """
    Renders the Department create page on GET
    Gets the valid form data on POST and creates a new Department
    """
    if request.method == 'POST':
        # get the form
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            # get the cleaned data
            name = form.cleaned_data.get('name')
            dept_type = form.cleaned_data.get('department_type')
            capacity = form.cleaned_data.get('capacity')
            # create the Department object
            department = Department.objects.create(
                name = name,
                dept_type = dept_type,
                capacity = capacity,
            )
            # save
            department.save()
            # redirect to detail page
            return redirect('bloodmanagement:department-detail',pk=department.pk)
    else:
        # render the form
        form = CreateDepartmentForm()
        return render(request,'department_create.html',context={"form":form})
    
def department_update(request,pk):
    """
    renders the form initialized with selected department data on GET
    On POST validates the data and updates the department object
    """
    if request.method == 'POST':
        # get the form
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            # get the validated data
            name = form.cleaned_data.get('name')
            dept_type = form.cleaned_data.get('department_type')
            capacity = form.cleaned_data.get('capacity')
            # update the department data
            Department.objects.filter(pk=pk).update(
                name = name,
                dept_type = dept_type,
                capacity = capacity,
            )
            # get the updated department object
            department=Department.objects.get(pk=pk)
            # redirect to the detail page
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
    """renders the detail page"""
    # get the requested department object
    department = get_object_or_404(Department,pk=pk)
    return render(request,'department_detail.html',context={'department':department})

def department_list(request):
    """renders the department list page"""
    # get all the department objects
    departments = Department.objects.all()
    return render(request,'department_list.html',context={"departments":departments})

def department_delete(request,pk):
    """Deletes the department object on POST"""
    if request.method == 'POST':
        # get the department object
        deparment = Department.objects.get(pk=pk)
        deparment.delete()
        return redirect('bloodmanagement:department-list')

def patient_create(request):
    """
    Renders the Patient create form on GET,
    on POST validates the input data and creates a new Patient
    """
    if request.method == 'POST':
        # get the form data
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            # get the cleaned data
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            condition = form.cleaned_data.get('condition')
            blood_type = form.cleaned_data.get('blood_type'),
            department = form.cleaned_data.get('department')
            # reduce the capacity as patient is added
            department.capacity -=1
            # save the dept.
            department.save()
            doctor = form.cleaned_data.get('doctor')
            # create the new patient
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
            # save the patient object
            patient.save()
            # redirect to detail page
            return redirect('bloodmanagement:patient-detail',pk=patient.pk)

    else:
        # render the form
        form = CreatePatientForm()
        return render(request,'patient_create.html',context={'form':form})

def patient_update(request,pk):
    """
    Renders the update form on GET, Updates the 
    Patient data on POST
    """
    if request.method == 'POST':
        # get the form data
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            condition = form.cleaned_data.get('condition')
            blood_type = form.cleaned_data.get('blood_type'),
            department = form.cleaned_data.get('department')
            doctor = form.cleaned_data.get('doctor')
            # update the Patient
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
            # get the updated patient data
            patient = Patient.objects.get(pk=pk)
            # redirect to patient detail page
            return redirect('bloodmanagement:patient-detail',pk=patient.pk)

    else:
        # get the requested patient object
        patient = Patient.objects.get(pk=pk)
        # initialize the patient form with old data
        form = CreatePatientForm(initial={
            "name":patient.name,
            "gender":patient.gender,
            "address":patient.address,
            "phone":patient.phone,
            "condition":patient.condition,
            "department":patient.department,
            "doctor":patient.doctor
        })
        # render the update page
        return render(request,'patient_create.html',context={'form':form})

def patient_list(request):
    """
    list all the patients
    """
    patients = Patient.objects.all()
    return render(request,'patient_list.html',context={"patients":patients})

def patient_detail(request,pk):
    """
    render the detail page
    """
    # get the requested patient
    patient = get_object_or_404(Patient,pk=pk)
    return render(request,'patient_detail.html',context={'patient':patient})

def patient_delete(request,pk):
    """
    on POST delete the requested patient 
    """
    if request.method == 'POST':
        # get the patient
        patient = get_object_or_404(Patient,pk=pk)
        # get the department
        department = Department.objects.get(patient=patient)
        # increase the capacity as patient has left
        department.capacity +=1
        # save the department
        department.save()
        # delete the patient
        patient.delete()
        return redirect('bloodmanagement:patient-list')

def blood_create(request):
    """
    Render the blood create form on GET,
    On POST get the form data and create a new blood row
    """
    if request.method == 'POST':
        # get the form data
        form = CreateBloodForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data.get('patient')
            donor = form.cleaned_data.get('donor')
            location = form.cleaned_data.get('location')
            blood_type = form.cleaned_data.get('blood_type')
            # create the new blood row
            blood = BloodPacket.objects.create(
                patient=patient,
                donor=donor,
                location=location,
                blood_type=blood_type
            )
            # save the blood row
            blood.save()
            # redirect to detail page
            return redirect('bloodmanagement:blood-detail',pk=blood.pk)

    else:
        # render the blood create form
        form = CreateBloodForm()
        return render(request,'blood_create.html',context={'form':form})
    
def blood_update(request,pk):
    """
    Renders the Blood Update form on GET,
    Updates the blood row on POST
    """
    if request.method == 'POST':
        # get the form data
        form = CreateBloodForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data.get('patient')
            donor = form.cleaned_data.get('donor')
            location = form.cleaned_data.get('location')
            blood_type = form.cleaned_data.get('blood_type')
            # update the blood row
            BloodPacket.objects.filter(pk=pk).update(
                patient=patient,
                donor=donor,
                location=location,
                blood_type=blood_type
            )
            # get the updated blood row
            blood = BloodPacket.objects.get(pk=pk)
            return redirect('bloodmanagement:blood-detail',pk=blood.pk)

    else:
        # get the old blood row
        blood = BloodPacket.objects.get(pk=pk)
        # initialize the form with old blood data
        form = CreateBloodForm(initial={
            "patient":blood.patient,
            "donor":blood.donor,
            "location":blood.location,
            "blood_type":blood.blood_type,
        })
        return render(request,'blood_create.html',context={'form':form})
    
def blood_list(request):
    """Get all the blood row"""
    bloods= BloodPacket.objects.all()
    return render(request,'blood_list.html',context={"bloods":bloods})

def blood_detail(request,pk):
    """render the requested blood details"""
    blood = get_object_or_404(BloodPacket,pk=pk)
    return render(request,'blood_detail.html',context={"blood":blood})

def blood_delete(request,pk):
    """Delete the requested blood row"""
    if request.method == 'POST':
        blood = get_object_or_404(BloodPacket,pk=pk)
        blood.delete()
        return redirect('bloodmanagement:blood-list')

def staff_create(request):
    """
    Render the staff create form on GET,
    get the form data and create a new staff row on POST
    """
    if request.method == 'POST':
        # get the form data
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            # create new staff row
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
        # render the create form
        form = CreateStaffForm()
        return render(request,'staff_create.html',context={'form':form})
    
def staff_detail(request,pk):
    """render the requested staff details"""
    staff = Staff.objects.get(pk=pk)
    return render(request,'staff_detail.html',context={"staff":staff})

def staff_list(request):
    """render all staff rows"""
    staffs = Staff.objects.all()
    return render(request,'staff_list.html',context={"staffs":staffs})

def staff_delete(request,pk):
    """delete the requested staff row"""
    if request.method == 'POST':
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        # redirect to staff list page
        return redirect('bloodmanagement:staff-list')

def staff_update(request,pk):
    """
    render the Update form on GET initialized old staff data,
    on POST get the form data and update the staff row.
    """
    if request.method == 'POST':
        # get the form data
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            # update the staff row
            Staff.objects.filter(pk=pk).update(
                name=name,
                phone=phone,
                address=address,
                job=job,
                department=department,
            )
            # get the updated staff row
            staff = Staff.objects.get(pk=pk)
            # redirect to detail page
            return redirect('bloodmanagement:staff-detail',pk=staff.pk)

    else:
        # get the old staff row
        staff = Staff.objects.get(pk=pk)
        # initialize form with old staff data
        form = CreateStaffForm(initial={
            "name":staff.name,
            "phone":staff.phone,
            "job":staff.job,
            "address":staff.address,
            "department":staff.department,
        })
        # render the form
        return render(request,'staff_create.html',context={'form':form})
    