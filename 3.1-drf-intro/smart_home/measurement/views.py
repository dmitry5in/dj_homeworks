from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class AllSensorsView(ListCreateAPIView):
    sensor = Sensor.objects.all()
    serializer_class = SensorSerializer


class OneSensorView(RetrieveUpdateAPIView):
    sensor = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    measure = Measurement.objects.all()
    serializer_class = MeasurementSerializer
