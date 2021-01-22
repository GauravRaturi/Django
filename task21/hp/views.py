from django.shortcuts import render
from rest_framework.response import Response
from .models import notification
from .serializers import notificationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.

class get(ListAPIView):

    queryset = notification.objects.all()
    serializer_class = notificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

  # permission_classes=[AllowAny]
  # permission_classes=[IsAdminUser]

    def get(self, request, pk=None, format=None):
        
        id = pk
        if id is not None:
            stu = notification.objects.get(id=id)
            serializer = notificationSerializer(stu)
            return Response(serializer.data)

        else:
            stu = notification.objects.all()
            serializer = notificationSerializer(stu,many=True)
            return Response(serializer.data)

class create(ListAPIView):

    queryset = notification.objects.all()
    serializer_class = notificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

  # permission_classes=[AllowAny]
  # permission_classes=[IsAdminUser]

    def post(self, request, format=None):
        serializer = notificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class update(ListAPIView):
    queryset = notification.objects.all()
    serializer_class = notificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def put(self, request, pk, format=None):
        id = pk
        stu = notification.objects.get(pk=id)
        serializer = notificationSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class delete(ListAPIView):
    queryset = notification.objects.all()
    serializer_class = notificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk, format=None):
        id = pk
        stu = notification.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    
