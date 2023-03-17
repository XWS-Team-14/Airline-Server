from django.utils import timezone

import django_filters

from .models.flight import Flight


class SearchFlightFilter(django_filters.FilterSet):
    """SearchFilter used to filter flights by multiple parameters

    Usage:
        '?date=&start_point=&end_point=&space_needed='

    """
    date = django_filters.DateFilter(field_name='date_of_departure', method='filter_by_date')
    start_point = django_filters.UUIDFilter(field_name='route__start_point', lookup_expr='exact')
    end_point = django_filters.UUIDFilter(field_name='route__end_point', lookup_expr='exact')
    space_needed = django_filters.NumberFilter(field_name='number_of_free_spaces', lookup_expr='gte')

    def filter_by_date(self, queryset, name, value):
        """Hack to filter datetime by date

        It's a little messy, but it works.
        It takes the date in search parameters and adds time to the end of the day (can be edited), and takes everything
        in-between those two dates
        """
        converted_date = timezone.datetime.strptime(str(value), "%Y-%m-%d")
        chosen_date_start = timezone.now().replace(year=converted_date.year, month=converted_date.month,
                                                   day=converted_date.day, hour=converted_date.hour,
                                                   minute=converted_date.minute, second=converted_date.second)
        chosen_date_end = chosen_date_start.replace(hour=23, minute=59, second=59)
        return queryset.filter(date_of_departure__gte=chosen_date_start).filter(date_of_departure__lte=chosen_date_end)

    class Meta:
        model = Flight
        fields = ['date', 'start_point', 'end_point', 'space_needed']
