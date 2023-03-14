import datetime

import django_filters

from .models.flight import Flight


class SearchFlightFilter(django_filters.FilterSet):
    """SearchFilter used to filter flights by multiple parameters

    Usage:
        '?date=&start_point=&end_point=&max_number_of_passengers='

    """
    date = django_filters.DateFilter(field_name='date_of_departure', method='filter_by_date')
    start_point = django_filters.UUIDFilter(field_name='route__start_point', lookup_expr='exact')
    end_point = django_filters.UUIDFilter(field_name='route__end_point', lookup_expr='exact')
    max_number_of_passengers = django_filters.NumberFilter(field_name='number_of_passengers', lookup_expr='lt')

    def filter_by_date(self, queryset, name, value):
        """Hack to filter datetime by date

        It's a little messy, but it works.
        It takes the date in search parameters and adds time to the end of the day (can be edited), and takes everything
        in-between those two dates
        """
        chosen_date_start = datetime.datetime.strptime(str(value), "%Y-%m-%d")
        chosen_date_end = chosen_date_start.replace(hour=23, minute=59, second=59)
        print(datetime.datetime.now().today())
        return queryset.filter(date_of_departure__lte=chosen_date_start).filter(date_of_departure__gte=chosen_date_end)

    class Meta:
        model = Flight
        fields = ['date', 'start_point', 'end_point', 'max_number_of_passengers']

