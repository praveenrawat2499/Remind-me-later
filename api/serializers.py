from rest_framework import serializers
from .models import Alerts

# Model Serializers

class AlertsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alerts
        fields = ['id', 'alert_date', 'alert_time', 'alert_message']
