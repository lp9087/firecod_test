from django_filters.rest_framework import filters, FilterSet, DateTimeFilter

from firecod_test.shops.models import Shops


class ShopPropertyFilter(FilterSet):
    is_open = filters.BooleanFilter(method='filter_open')

    class Meta:
        model = Shops
        fields = ['city']

    def filter_open(self, queryset, value):
        if value:
            queryset = queryset.filter(is_open = value)
        return queryset