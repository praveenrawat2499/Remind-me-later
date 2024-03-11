from django.urls import path
from .views import AlertsLC, AlertsRUD

urlpatterns = [
    path('create/', AlertsLC.as_view(), name='create_reminder'),
    path('alrud/', AlertsRUD.as_view(), name='rud_reminder'),
]