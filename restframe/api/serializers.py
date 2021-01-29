from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.ModelSerializer):
 class Meta:
  model = Market
  fields = ['product', 'name', 'notified_person', 'notification_status', 'size', 'address']
