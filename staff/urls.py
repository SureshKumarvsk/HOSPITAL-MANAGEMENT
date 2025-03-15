from django.urls import path
from . import views

urlpatterns =[
    path('login_staff',views.login_staff,name='login_staff'),
    path('register_staff',views.register_staff,name='register_staff'),
    path('staffpro',views.staffpro,name='staffpro'),
    path('staff_appo',views.staff_appo,name='staff_appo'),
    path('staff_logout',views.logout_staff,name='logout_staff'),
    path('staff_about',views.staff_about,name='staff_about'),
    path('staffaddDetials/<int:id>',views.staffaddDetials,name='staffaddDetials'),
    path('staff_id/<int:id>',views.staff_id,name='staff_id'),
    path('smallaccept/<int:id>', views.smallAccept, name='smallAcceptd'),
    path('smalldecline/<int:id>', views.smalldecline, name='smalldeclined'),
    path('Accpet/<int:id>',views.Accept,name='Acceptd'),
    path('Decline/<int:id>',views.Decline,name='Declined'),
    path('recoverAccept/<int:id>',views.recover_Accept,name='recover_Acceptd'),
    path('recoverdecline/<int:id>',views.recover_decline,name='recover_declinedd'),
    path('Accepted',views.Accepted,name='Acceptedd'),
    path('Declined',views.Declined,name='Declinedd'),
    path('reason/<int:id>',views.reason,name='reasond'),
    path('reason_to_all/<str:decline_ids>/', views.reason_to_all, name='reason_to_alld'),
]