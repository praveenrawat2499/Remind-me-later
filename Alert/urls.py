
from django.contrib import admin
from django.urls import path
from api import views

# Grouping
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alert/', views.AlertsLC.as_view()),
    path('alert/<int:pk>/', views.AlertsRUD.as_view()),
]
