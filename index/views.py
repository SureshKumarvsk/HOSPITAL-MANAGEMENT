from django.shortcuts import render, redirect
from app1.models import Patient,refcases,Appointment
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from app1.models import Accept_Model,Decline_Model
from datetime import datetime

def logindoc(request):
    return redirect('loginn')

def authen(name_data, password_data):
    try:
        patient = Patient.objects.get(name=name_data)
        if check_password(password_data, patient.password):
            return patient
    except Patient.DoesNotExist:
        return None


def loginpat(request):
    if request.method == "POST":
        name_data = request.POST['username']
        password_data = request.POST['password']

        # Authenticate the patient
        patient = authen(name_data, password_data)

        if patient is not None:
            # Set session data
            request.session['patient_id'] = patient.id
            request.session['patient_name'] = patient.name
            print("Session Created:", request.session['patient_id'])
            return redirect('report')  # Redirect to patient page
        else:
            return render(request, 'patwrong.html', {'loginname': name_data})

    return render(request, 'patientloginn.html')


# View for patient registration
def reginpat(request):
    if request.method == "POST":
        name_data = request.POST['username']
        password_data = request.POST['password']
        email_data = request.POST['email']
        key_data = request.POST['key']
        hashed_password = make_password(password_data)  # Ensure password is hashed
        a = User.objects.get(first_name=key_data)
        doc_name = a.username
        print(doc_name)

        # Create a new Patient
        Patient.objects.create(name=name_data, password=hashed_password, email=email_data, host=a)
        refcases.objects.create(name=name_data, doctor=doc_name)

        return redirect('loginpat')  # Redirect to login after registration

    return render(request, 'patientregister.html')


def patabout(request):
    return render(request,'patabout.html')
# View for patient page
 # Redirect to login if no patient_id in session


def patlogout(request):
    request.session.flush() 
    return redirect('index') 


def index(request):
    return render(request,'index.html')

def report(request):
    patient_id = request.session.get('patient_id')
    a= Patient.objects.get(id=patient_id)
    return render(request,'report.html',{'data':a})

def addpatdetials(request):
    patient_id = request.session.get('patient_id')
    patient = Patient.objects.get(id=patient_id)
    if request.method =='POST':
        a=Patient.objects.get(name=request.POST['name'])
        b=refcases.objects.get(name = request.POST['name'])
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
        b.age = request.POST.get('age')
        b.gender = request.POST.get('gender')
        b.contact = request.POST.get('contact')
        b.address = request.POST.get('address')
        b.date = request.POST.get('date')
        b.save()
        return redirect('report')
    return render(request,'addpatientdetials.html',{'patient':patient})

def appointments(request):
    patient_id = request.session.get('patient_id')
    patient = Patient.objects.get(id=patient_id)
    doc_id = patient.host
    User.objects.get(username=doc_id)
    docter_id=doc_id.id
    if patient.Appointment_confirmation == "0":
        if request.method == "POST":
            name_data = request.POST['name']
            disease_data = request.POST['disease_diagnosed']
            date_data = request.POST['date']
            time_data = request.POST['time']
            desc_data = request.POST['desc']
            docid_data = request.POST['doc_id']
            Appointment.objects.create(
                patient_name=name_data,
                disease_diagnosed=disease_data,
                date=date_data,
                time=time_data,
                message_to_doctor=desc_data,
                doctor=docid_data
            )
            return redirect('loginpat')
    elif patient.Appointment_confirmation == "1":
        return redirect('appaccc')
    elif patient.Appointment_confirmation == "2":
        return redirect('appdecc')

    return render(request,'appointments.html',{'patient':patient,'doc_id':docter_id})



def appacc(request):
    patientid = request.session.get('patient_id')
    print(patientid)
    try:
        patient = Patient.objects.get(id=patientid)
        print('name', patient.name)

        accepts = Accept_Model.objects.filter(patient_name=patient.name)
        if accepts.exists():
            most_recent_accept = max(accepts, key=lambda x: datetime.strptime(x.date, "%d/%m/%Y"))

            return render(request, 'appacc.html', {'data': most_recent_accept})
        else:
            return render(request, 'appacc.html', {'data': None, 'message': 'No accepted data found for the patient.'})
    except Patient.DoesNotExist:
        return render(request, 'appacc.html', {'data': None, 'message': 'Patient does not exist.'})
    except ValueError as e:
        return render(request, 'appacc.html', {'data': None, 'message': f'Date format error: {e}'})



def appdec(request):
    patientid = request.session.get('patient_id')
    print(patientid)
    try:
        patient = Patient.objects.get(id=patientid)
        print('name', patient.name)

        # Fetch all entries for the patient
        declines = Decline_Model.objects.filter(patient_name=patient.name)

        # Convert string dates to datetime objects for sorting
        if declines.exists():
            most_recent_decline = max(declines, key=lambda x: datetime.strptime(x.date, "%d/%m/%Y"))

            return render(request, 'appdec.html', {'data': most_recent_decline})
        else:
            return render(request, 'appdec.html', {'data': None, 'message': 'No declined data found for the patient.'})
    except Patient.DoesNotExist:
        return render(request, 'appdec.html', {'data': None, 'message': 'Patient does not exist.'})
    except ValueError as e:
        return render(request, 'appdec.html', {'data': None, 'message': f'Date format error: {e}'})


def newappointment(request):
    patientid= request.session.get('patient_id')
    print(patientid)
    patient= Patient.objects.get(id=patientid)
    patient.Appointment_confirmation ="0"
    patient.save()
    return redirect('appointments')
    
