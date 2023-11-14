from pydantic import BaseModel
from typing import Dict


class FormInput(BaseModel):
    data: Dict[str, str]
