import requests

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

isetsyvalidator = RegexValidator(regex="^http(s)?://(www\.)?etsy\.com/uk/listing/[0-9]+(/[a-z-]+)?$",
                                 message="Must be an Etsy item listing link",
                                 code="Invalid key")


def validate_link_exists(value):
    if requests.head(value).status_code != 200:
        raise ValidationError(
            _('%(value)s is not an existing link'),
            params={'value': value},
        )
