from django.urls import path
from . import views
urlpatterns = [
    #path('',views.index,name="index"),
    path('get/', views.get.as_view()),
    path('create/', views.create.as_view()),
    path('update/', views.update.as_view()),
    path('delete/<int:pk>/', views.delete.as_view())

]