import pytest

from src.services.services import get_field_type


@pytest.mark.parametrize(
    'value, expected',
    [
        ('test@example.com', 'email'),
        ('test@', 'text'),
        ('test@examply.', 'text'),
        ('+7 800 800 80 80', 'phone'),
        ('+7 800 000 00 000', 'text'),
        ('719891284', 'text'),
        ('01.01.2023', 'date'),
        ('50.01.2023', 'text'),
        ('2022-01-01', 'date'),
        ('2022-13-01', 'text'),
    ]
)
def test_services(value, expected):
    result = get_field_type(value)
    assert result == expected
