from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WeatherBase
from .serializer import WeatherSerializer


class WeatherView(APIView):
    serializer_class = WeatherSerializer

    def get(self, request):
        weather = WeatherBase.objects.latest('date_today')
        serializer = WeatherSerializer(weather)
        return Response(serializer.data)
