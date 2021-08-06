import django_filters
from .models import college, shop


class shopFilters():

    class Meta:
        model = shop
        fields = ('distance', 'rating', 'AveragePrice')
