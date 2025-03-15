from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('logindoc',views.logindoc,name='logindoc'),
    path('loginpat',views.loginpat,name='loginpat'),
    path('reginpat',views.reginpat,name='reginpat'),
    path('patlogout',views.patlogout,name='patlogout'),
    path('report',views.report,name='report'),
    path('addpatdetials',views.addpatdetials,name='addpatdetials'),
    path('appointments',views.appointments,name='appointments'),
    path('appacc',views.appacc,name='appaccc'),
    path('appdec',views.appdec,name='appdecc'),
    path("patabout",views.patabout,name='patabout'),
    path('newappointment',views.newappointment,name='newappointment'),
]