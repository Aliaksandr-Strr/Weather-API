import requests
from django.core.management.base import BaseCommand
from django.conf import settings

from openweather.models import WeatherBase


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-c', '--city', type=str)

    def handle(self, *args, **kwargs):
        try:
            city = kwargs['city']
            url = "{}{}&APPID=447f8c8e9662b33ea7d21aceaed9c98e".format(settings.API_WEATHER, city)
        except ValueError:
            url = "{}{}&APPID=447f8c8e9662b33ea7d21aceaed9c98e".format(settings.API_WEATHER, 'Minsk')
        response = requests.get(url)
        result = response.json()
        w = WeatherBase(
            city=result['name'],
            temperature=result['main']['temp'] - 273.15,
            wind_speed=result['wind']['speed'],
            weather_condition=result['weather'][0]['description'],
            weather_icon=result['weather'][0]['icon'],
            weather_id=result['weather'][0]['id'])
        w.save()