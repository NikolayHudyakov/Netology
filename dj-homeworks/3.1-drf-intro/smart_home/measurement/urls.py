from django.urls import path

from measurement.views import SensorCreateView, SensorUpdateView, MeasurementsAddView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementsAddView.as_view())
]
