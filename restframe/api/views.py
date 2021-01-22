from .models import Student
from .serializers import StudentSerializer
#from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


# Create your views here.
def index(request):
    return render(request,'index.html')

class StudentModelViewSet(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes=[BasicAuthentication]
  permission_classes=[IsAuthenticated]
  # permission_classes=[AllowAny]
  # permission_classes=[IsAdminUser]



