from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.index,name="index"),
    path('About',views.about,name="about"),
    path('Contacts',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('reg',views.reg,name="reg"),
    path('Success',views.success,name="success"),
    path('edit',views.edit, name="edit"),
    path('Logout',views.logout,name="logout"),
    path('edit2',views.edit2,name="edit2"),
    path('delete',views.delete,name="delete"),
    path('home',views.home,name="home")
]