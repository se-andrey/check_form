from typing import Any, Dict

from fastapi import FastAPI

from src.database.mongodb import dump_test_base, get_base
from src.services.services import get_field_type

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await dump_test_base()


@app.post("/get_form")
async def get_form(data: Dict[str, Any]):
    form_data_dict = data
    db_collection = await get_base()

    # Словарь для подсчета совпадений
    matching_counts = {}

    for template in db_collection.find():
        template_fields = set(template.keys()) - {'_id', 'name'}

        # Суммируем все совпадения полей, при этом валидируем получаемое значение
        matching_count = sum(
            1 for field in template_fields if field in form_data_dict and
            get_field_type(form_data_dict[field]) == template[field]
        )
        # Добавляем в словарь только, если совпали все поля
        if matching_count == len(template_fields):
            matching_counts[template['name']] = matching_count

    if matching_counts:
        max_matching_template = max(matching_counts, key=matching_counts.get)
        return max_matching_template

    # Валидируем типы в запросе
    field_types = {field: get_field_type(form_data_dict[field]) for field in form_data_dict}
    return field_types
