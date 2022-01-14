from django.db.models import Case, When, Value
from django.utils.timezone import localtime, datetime
from django_filters.rest_framework import filters, FilterSet, DateTimeFilter

from shops.models import Shops


class ShopPropertyFilter(FilterSet):
    open = filters.BooleanFilter(method='filter_open')

    class Meta:
        model = Shops
        fields = ['city', 'street', 'open']

    def filter_open(self, queryset, name, value):
        qs = queryset.annotate(
            opening=Case(
                When(
                    opening_time__lt=datetime.now().time(),
                    closing_time__gt=datetime.now().time(),
                    then=Value(1)),
                default=Value(0)
            )
        ).filter(opening=value)
        return qs
