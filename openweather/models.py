from django.db import models


class WeatherBase(models.Model):
    date_today = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=10, decimal_places=1)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=1)
    weather_condition = models.CharField(max_length=30)
    weather_icon = models.CharField(max_length=10)
    weather_id = models.IntegerField()
