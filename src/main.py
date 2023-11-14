from fastapi import FastAPI
from src.database.mongodb import dump_test_base, get_base
from src.schemas.schemas import FormInput
from src.services.services import get_field_type

app = FastAPI()

@app.on_event('startup')
async def on_startup():
    await dump_test_base()


@app.post("/get_form")
async def get_form(data: FormInput):
    form_data_dict = dict(data.data)
    db_collection = await get_base()
    for template in db_collection.find():
        template_fields = set(template.keys()) - {'_id', 'name'}
        if template_fields.issubset(form_data_dict.keys()):
            return {"form_name": template['name']}
    field_types = {field: get_field_type(form_data_dict[field]) for field in form_data_dict}
    return field_types
