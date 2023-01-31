import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
import psutil
from testProjectServer.settings import WEATHER_BASE_URL, WEATHER_API_KEY


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def get_weather(request):
    data = request.data

    city = data.get('city', None)

    if city is None:
        return Response({'error': 'city required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get(url=f'{WEATHER_BASE_URL}/find',
                                params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': WEATHER_API_KEY})
        data = response.json()
        city_id = data['list'][0]['id']

        res = requests.get(f'{WEATHER_BASE_URL}/weather',
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': WEATHER_API_KEY})
        data = res.json()
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response(data, status=response.status_code)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_disk_usage(request):
    try:
        disk_usage = psutil.disk_usage('/')
        data = {
            'total': disk_usage.total,
            'used': disk_usage.used,
            'free': disk_usage.free,
            'percent': disk_usage.percent,
            'time': str(datetime.datetime.now())
        }
    except OSError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data, status=status.HTTP_200_OK)
