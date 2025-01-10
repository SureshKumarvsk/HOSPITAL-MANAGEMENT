from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from app1.models import Profile,Appointment

import random
import string

def generate_unique_id():
    characters = string.ascii_uppercase + string.digits
    unique_id = ''.join(random.choices(characters, k=6))
    return unique_id




def loginn(request):
    if request.method == "POST":
        name_data = request.POST['username']
        password_data = request.POST['password']
        b =authenticate(username = name_data,password = password_data)
        print(b)
        if b is not None:
             login(request,b)   
             appointments = Appointment.objects.filter(doctor= request.user.id)
             r = len(appointments)   
             a=User.objects.get(username = request.user)
             a.last_name= r
             a.save()
             a.refresh_from_db()
             return redirect('mycases')
        else:
             return render(request,'wrong.html',{'loginname':name_data})
        
    return render(request,'loginn.html')

def register(request):
        if request.method == "POST":
            org_key = "1234"
            key_data = request.POST['key']
            if key_data == org_key:
                name_data = request.POST['username']
                password_data = request.POST['password']
                email_data = request.POST['email']
                doc_id = generate_unique_id()
                a = User.objects.create(username = name_data,email =email_data,first_name =doc_id)
                Profile.objects.create(name = name_data,email = email_data,docter_id=doc_id) 
                a.set_password(password_data)
                a.save()
                return redirect('loginn')

            else:
                 return render(request,'wrongreg.html')
        
        return render(request,'register.html')

def about(request):
    return render(request,'about.html')