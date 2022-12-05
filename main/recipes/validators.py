import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        _ = ureg[value.lower()]
    except UndefinedUnitError as e:
        raise ValidationError(f"'{value}' is not a valid unit of measure")
    except:
        raise ValidationError(f"'{value}' is invalid. Unknown error.")