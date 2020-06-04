from rest_framework import serializers
from .models import WeatherBase


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherBase
        fields = ('date_today', 'city', 'temperature', 'wind_speed', 'weather_condition', 'weather_icon', 'weather_id')
