from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ["status"]
