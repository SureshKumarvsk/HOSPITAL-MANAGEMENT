from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import Patientforms
from django.contrib.auth.decorators import login_required
from .models import Patient, refcases,Profile,Appointment,Accept_Model,Decline_Model
from django.db.models import Q
from django.contrib.auth.models import User


@login_required(login_url='loginn')
def addcases(request):
    doctor_id = str(request.user.id)  
    appointments = Appointment.objects.filter(doctor=doctor_id)
    return render(request, 'addcases.html',{'data':appointments})

@login_required(login_url='loginn')
def mycases(request):
    a = Patient.objects.filter(host=request.user)
    r = len(a)
    d= Profile.objects.get(name = request.user)
    d.NoOfCasesattended = r
    d.save()
    context = {'data': a}
    return render(request, 'mycases.html',context)

@login_required(login_url='loginn')
def editformycases(request,id):
    a = Patient.objects.get(id =id)
    b= refcases.objects.get(name = a.name)
    if request.method =='POST':
        a.name = request.POST.get('name')
        a.age = request.POST.get('age')
        a.gender = request.POST.get('gender')
        a.contact = request.POST.get('contact')
        a.address = request.POST.get('address')
        a.date = request.POST.get('date')
        a.disease_diagnosed = request.POST.get('disease_diagnosed')
        a.case_details = request.POST.get('case_details')
        a.medications = request.POST.get('medications')
        a.save()
        b.name = request.POST.get('name')
        b.age = request.POST.get('age')
        b.gender = request.POST.get('gender')
        b.contact = request.POST.get('contact')
        b.address = request.POST.get('address')
        b.date = request.POST.get('date')
        b.disease_diagnosed = request.POST.get('disease_diagnosed')
        b.case_details = request.POST.get('case_details')
        b.medications = request.POST.get('medications')
        b.save()
        return redirect('mycases')


    return render(request,'editcases.html',{'data':a})

@login_required(login_url='loginn')
def delformycases(request,id):
    a = Patient.objects.get(id =id)
    print(id)
    b = refcases.objects.get(name = a.name)
    a.delete()
    b.delete()
    return redirect('mycases')


@login_required(login_url='loginn')
def referencecases(request):
    nomatch = False
    if request.method == "GET":
        if "search" in request.GET:
            search_data = request.GET['search']
            a= refcases.objects.filter(Q(disease_diagnosed__icontains = search_data) | Q(medications__icontains = search_data))
            if len(a) == 0:
                nomatch =True
        else:
            a =refcases.objects.all()
    context ={'data':a,'match':nomatch}
    return render(request, 'referencecases.html', context)

@login_required(login_url='loginn')
def profile(request):
    s = Profile.objects.get(name = request.user)
    return render(request, 'profile.html',{'data':s})


@login_required(login_url='loginn')
def AddDetials(request, id):
    if request.method == "POST":
        name_data = request.POST['name']
        age_data = request.POST['age']
        gender_data = request.POST['gender']
        dob_data = request.POST['DateOfBirth']
        contact_data = request.POST['contact']
        address_data = request.POST['address']
        designation_data = request.POST['Designation']
        experience_data = request.POST['experience']
        cases_attended_data = request.POST['NoOfCasesattended']
        image_data = request.FILES['image']


        s = Profile.objects.get(name=name_data)
        

        s.age = age_data
        s.gender = gender_data
        s.DateOfBirth = dob_data
        s.contact = contact_data
        s.address = address_data
        s.Designation = designation_data
        s.experience = experience_data
        s.NoOfCasesattended = cases_attended_data
        s.image = image_data


        s.save()

        return redirect('profile')
    
    s = Profile.objects.get(id=id)
    return render(request, 'addDetials.html', {'data': s})

        


@login_required(login_url='loginn')
def logoutt(request):
    logout(request)
    return redirect('index')


@login_required(login_url='loginn')
def Accept(request):
    doctor_id = str(request.user.id)  
    appointments = Appointment.objects.filter(doctor=doctor_id)
    
    for appointment in appointments:
        try:
            patient = Patient.objects.get(name=appointment.patient_name)
            patient.Appointment_confirmation = '1'  
            patient.save()
            a = User.objects.get(username=request.user)
            a.last_name =0
            a.save()
            
            Accept_Model.objects.create(
                patient_name=appointment.patient_name,
                disease_diagnosed=appointment.disease_diagnosed,
                date=appointment.date,
                time=appointment.time,
                message_to_doctor=appointment.message_to_doctor,
                doctor=appointment.doctor
            )
        except Patient.DoesNotExist:
           
            pass
    
    appointments.delete()
    return redirect('Accepted')

@login_required(login_url='loginn')
def Decline(request):
    doctor_id = str(request.user.id)  
    appointments = Appointment.objects.filter(doctor=doctor_id)
    decline_ids = []  # To store IDs of newly created Decline_Model records

    for appointment in appointments:
        try:
            patient = Patient.objects.get(name=appointment.patient_name)
            patient.Appointment_confirmation = '2'  # Assuming '2' means Declined
            patient.save()

            a = User.objects.get(username=request.user)
            a.last_name = 0
            a.save()

            decline = Decline_Model.objects.create(
                patient_name=appointment.patient_name,
                disease_diagnosed=appointment.disease_diagnosed,
                date=appointment.date,
                time=appointment.time,
                message_to_doctor=appointment.message_to_doctor,
                doctor=appointment.doctor
            )
            decline_ids.append(decline.id)
        except Patient.DoesNotExist:
            pass

    # Delete the appointments after processing
    appointments.delete()

    # Redirect with IDs of filtered Decline_Model records
    return redirect('reason_to_all', decline_ids=','.join(map(str, decline_ids)))






@login_required(login_url='loginn')
def smallAccept(request,id):
    a = User.objects.get(username=request.user)
    s = a.last_name 
    number = int(s)-1
    print(s)
    a.last_name = number
    a.save()
    b= Appointment.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 1
    z.save()
    Accept_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('Accepted')


@login_required(login_url='loginn')
def smalldecline(request,id):
    a = User.objects.get(username=request.user)
    s = a.last_name
    number = int(s) - 1
    a.last_name = number
    a.save()
    b= Appointment.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 2
    z.save()
    c=Decline_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('reason',c.id)
    

def recover_Accept(request,id):
    b=Decline_Model.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 1
    z.save()
    Accept_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('Accepted')

def recover_decline(request,id):
    b=Accept_Model.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 2
    z.save()
    c=Decline_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('reason',c.id)

def Accepted(request):
    a=Accept_Model.objects.all()
    return render(request,'Accepted.html',{'data':a})

def Declined(request):
    a = Decline_Model.objects.all()
    return render(request,'declined.html', {'data':a})

def reason(request, id):
    a = Decline_Model.objects.get(id=id)
    if request.method == "POST":
        message = request.POST.get('desc')
        if message:
            a.message_to_doctor = message
            a.save()
            return redirect('Declined')
        
    
    return render(request, 'reason.html', {'patient': a})

@login_required(login_url='loginn')
def reason_to_all(request, decline_ids):
    decline_ids = list(map(int, decline_ids.split(',')))  # Convert comma-separated string to list of integers
    declines = Decline_Model.objects.filter(id__in=decline_ids)

    if request.method == "POST":
        message = request.POST.get('desc')
        if message:
            for decline in declines:
                decline.message_to_doctor = message
                decline.save()
            return redirect('Declined') 

    return render(request, 'reason_to_all.html', {'declines': declines})

