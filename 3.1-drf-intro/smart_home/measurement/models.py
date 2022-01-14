from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


