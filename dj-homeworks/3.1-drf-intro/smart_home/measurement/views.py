# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request: Request):

        return Response({'status': 'ok'})

