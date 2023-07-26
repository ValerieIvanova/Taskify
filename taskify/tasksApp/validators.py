from django.utils import timezone


def date_in_the_past(input_date):
    today = timezone.now().date()
    return input_date >= today
