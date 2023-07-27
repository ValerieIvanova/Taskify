from django.core.exceptions import ValidationError
from django.utils import timezone


def date_in_the_past(input_date):
    if input_date < timezone.now().date():
        raise ValidationError(
            'Date must not be in the past.'
        )