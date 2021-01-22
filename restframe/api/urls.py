from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('studentapi/', views.StudentModelViewSet.as_view()),

]