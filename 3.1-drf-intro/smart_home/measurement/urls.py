from django.urls import path
from .views import AllSensorsView, OneSensorView, MeasurementView

urlpatterns = [
    path('sensors/', AllSensorsView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
