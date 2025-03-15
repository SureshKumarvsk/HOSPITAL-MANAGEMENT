from django.shortcuts import render,redirect
from .models import Staff_Profile
from django.contrib.auth.models import User
from app1.models import Appointment,Accept_Model,Decline_Model,Patient
from django.contrib.auth.hashers import make_password, check_password

def authen(name_data, password_data):
    try:
        staff = Staff_Profile.objects.get(name=name_data)
        if check_password(password_data, staff.password):
            return staff
    except Staff_Profile.DoesNotExist:
        return None


def login_staff(request):
    if request.method == "POST":
        name_data = request.POST['username']
        password_data = request.POST['password']

        # Authenticate the patient
        staff = authen(name_data, password_data)

        if staff is not None:
            # Set session data
            request.session['staff_id'] = staff.id
            request.session['staff_name'] = staff.name
            print("Session Created:", request.session['staff_id'])
            return redirect('staff_appo')  # Redirect to staff page
        else:
            return render(request, 'staffwrong.html', {'loginname': name_data})

    return render(request, 'login_staff.html')

def register_staff(request):
        if request.method == "POST":
            org_key = "1234"
            key_data = request.POST['key']
            if key_data == org_key:
                name_data = request.POST['username']
                password_data = request.POST['password']
                email_data = request.POST['email']
                hashed_password = make_password(password_data) 
                
                
                Staff_Profile.objects.create(name = name_data,password=hashed_password,email = email_data) 
                
                return redirect('login_staff')

            else:
                 return render(request,'staffwrongreg.html')

        return render(request,'register_staff.html')

def staff_about(request):
    return render(request,'staff_about.html')

def staffpro(request):
    staff_name = request.session.get('staff_name')
    s = Staff_Profile.objects.get(name = staff_name)
    return render(request,'staffpro.html',{'data':s}) 
      
def staffaddDetials(request,id):
    a=Staff_Profile.objects.get(id=id)
    if request.method == "POST":
        name_data = request.POST['name']
        age_data = request.POST['age']
        gender_data = request.POST['gender']
        dob_data = request.POST['DateOfBirth']
        contact_data = request.POST['contact']
        address_data = request.POST['address']
        designation_data = request.POST['Designation']
        experience_data = request.POST['experience']
        image_data = request.FILES['image']


        s = Staff_Profile.objects.get(name=name_data)
        

        s.age = age_data
        s.gender = gender_data
        s.DateOfBirth = dob_data
        s.contact = contact_data
        s.address = address_data
        s.Designation = designation_data
        s.experience = experience_data
        s.image = image_data


        s.save()

        return redirect('staffpro')
     
    return render(request,'staffaddDetials.html',{'data':a})

def staff_appo(request):
    a=User.objects.all()
    return render(request,'staff_appo.html',{'data':a})

def staff_id(request, id):
    j=id
    a = Appointment.objects.filter(doctor=id)  # Get all appointments for the given doctor ID
    doctor = None 
    print('doctor',id)
    doctor = j

    return render(request, 'staff_id.html',{'data':a,'doctor':doctor})






def Accept(request,id):
    appointments = Appointment.objects.filter(doctor=id)
    print("appointments", appointments)
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
    return redirect('Acceptedd')


def Decline(request,id):
    appointments = Appointment.objects.filter(doctor=id)
    decline_ids = [] 
    for appointment in appointments:
        try:
            patient = Patient.objects.get(name=appointment.patient_name)
            patient.Appointment_confirmation = '2' 
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

   
    appointments.delete()

    
    return redirect('reason_to_alld', decline_ids=','.join(map(str, decline_ids)))







def smallAccept(request,id):
    m= Appointment.objects.get(id = id)
    doc_id=m.doctor
    a = User.objects.get(id=doc_id)
    user_name =a.username
    a = User.objects.get(username=user_name)
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
    return redirect('Acceptedd')



def smalldecline(request,id):
    m= Appointment.objects.get(id = id)
    doc_id=m.doctor
    a = User.objects.get(id=doc_id)
    user_name =a.username
    a = User.objects.get(username=user_name)
    s = a.last_name 
    number = int(s)-1
    print(s)
    a.last_name = number
    a.save()
    b= Appointment.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 2
    z.save()
    c=Decline_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('reasond',c.id)
    

def recover_Accept(request,id):
    b=Decline_Model.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 1
    z.save()
    Accept_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('Acceptedd')

def recover_decline(request,id):
    b=Accept_Model.objects.get(id = id)
    z=Patient.objects.get(name=b.patient_name)
    z.Appointment_confirmation = 2
    z.save()
    c=Decline_Model.objects.create(patient_name=b.patient_name,disease_diagnosed=b.disease_diagnosed,date=b.date,
time =b.time,message_to_doctor=b.message_to_doctor,doctor=b.doctor)
    b.delete()
    return redirect('reasond',c.id)

def Accepted(request):
    a=Accept_Model.objects.all()
    return render(request,'Accepted2.html',{'data':a})

def Declined(request):
    a = Decline_Model.objects.all()
    return render(request,'declined2.html', {'data':a})

def reason(request, id):
    a = Decline_Model.objects.get(id=id)
    if request.method == "POST":
        message = request.POST.get('desc')
        if message:
            a.message_to_doctor = message
            a.save()
            return redirect('Declinedd')
        
    
    return render(request, 'reason.html', {'patient': a})


def reason_to_all(request, decline_ids):
    decline_ids = list(map(int, decline_ids.split(',')))  # Convert comma-separated string to list of integers
    declines = Decline_Model.objects.filter(id__in=decline_ids)

    if request.method == "POST":
        message = request.POST.get('desc')
        if message:
            for decline in declines:
                decline.message_to_doctor = message
                decline.save()
            return redirect('Declinedd') 

    return render(request, 'reason_to_all.html', {'declines': declines})

def logout_staff(request):
    request.session.flush() 
    return redirect('index')