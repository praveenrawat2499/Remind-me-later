from api.models import Alerts
from .serializers import AlertsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
  
# AlertsLC - method to create and list alert. 
class AlertsLC(ListCreateAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer

# AlertsRUD - method to Retrieve, Update and Delete alert.  
class AlertsRUD(RetrieveUpdateDestroyAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer