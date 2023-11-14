import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


@pytest.mark.parametrize("test_data, expected", [
    ({"user_name": "some_name", "order_date": "01.01.2021"}, "MyForm"),
    ({"user_name": "some_name", "order_date": "01.01.2021", "female": "man"}, "MyForm"),
    ({"user_name": "some_name", "lead_email": "test@example.com"}, "OrderForm"),
    ({"user_name": "some_name", "age": "2", "order_date": "01.01.2021"}, "MyFormMore"),
    ({"user_name": "some_name", "lead_email": "test@example.com"}, "OrderForm"),
    ({"user_name": "some_name", "lead_email": "test@example.com", "phone": "+7 909 900 90 90"}, "OrderForm"),
    ({"user_name": "some_name", "email": "test@example.com", "phone": "+7 909 900 90 90"}, "FeedbackForm"),
    ({"user_name": "some_name", "email": "test@example", "phone": "+7 909 900 90 90"},
     {"user_name": "text", "email": "text", "phone": "phone"}),
    ({"user_name": "some_name", "age": "18", "feedback": "Some feedback"}, "SurveyForm"),
    ({"user_name": "some_name", "order_date": "01.01.2021", "lead_email": "test@example.com"}, "MyForm"),
    ({"value1": "text", "value2": "01.01.2021", "value3": "2020-01-01", "value4": "50.50.5000",
      "value5": "+7 909 900 90 90", "value6": "88008008080", "value7": "test@example.com"},
     {"value1": "text", "value2": "date", "value3": "date", "value4": "text",
      "value5": "phone", "value6": "text", "value7": "email"}),
])
def test_get_form(test_data, expected):
    response = client.post("/get_form", json=test_data)
    assert response.status_code == 200

    if isinstance(expected, str):
        assert response.text.strip('"') == expected
    else:
        assert response.json() == expected
