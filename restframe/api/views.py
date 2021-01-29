from django.shortcuts import render
from .serializers import MarketSerializer
from rest_framework.generics import ListAPIView
from .models import Market
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

class MarketList(ListAPIView):
 queryset = Market.objects.all()
 serializer_class = MarketSerializer
 filter_backends = [SearchFilter]
 #search_fields = ['name']
 #search_fields = ['product','name']
 #search_fields = ['^name']
 search_fields = ['=name','product']

 #filter_backends = [OrderingFilter]
 #ordering_fields = ['name']







