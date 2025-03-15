from django.urls import path
from . import views

urlpatterns =[
    path('loginn',views.loginn,name='loginn'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
  
]