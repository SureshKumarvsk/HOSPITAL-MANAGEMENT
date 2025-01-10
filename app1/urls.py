from django.urls import path
from . import views

urlpatterns =[
    path('addcases',views.addcases,name='addcases'),
    path('mycases',views.mycases,name="mycases"),
    path('referencecases',views.referencecases,name='referencecases'),
    path('profile',views.profile,name='profile'),
    path('logoutt',views.logoutt,name='logoutt'),
    path('AddDetials/<int:id>',views.AddDetials,name='adddetials'),
    path('Editformycases/<int:id>',views.editformycases,name='editformycases'),
    path('Deleteformycases/<int:id>',views.delformycases,name='delformycases'),
    path('smallaccept/<int:id>', views.smallAccept, name='smallAccept'),
    path('smalldecline/<int:id>', views.smalldecline, name='smalldecline'),
    path('Accpetall',views.Accept,name='Accept'),
    path('Declineall',views.Decline,name='Decline'),
    path('recoverAccept/<int:id>',views.recover_Accept,name='recover_Accept'),
    path('recoverdecline/<int:id>',views.recover_decline,name='recover_decline'),
    path('Accepted',views.Accepted,name='Accepted'),
    path('Declined',views.Declined,name='Declined'),
    path('reason/<int:id>',views.reason,name='reason'),
    path('reason_to_all/<str:decline_ids>/', views.reason_to_all, name='reason_to_all'),

]