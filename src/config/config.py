import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class MongoDb:
    url: str
    db_name: str
    db_collection: str


@dataclass
class TestDB:
    test: bool


@dataclass
class Config:
    db: MongoDb
    test: TestDB


def load_config(path: str | None = None) -> Config:
    load_dotenv(path)
    return Config(
        db=MongoDb(
            url=os.getenv('DB_URL'),
            db_name=os.getenv('DB_NAME'),
            db_collection=os.getenv('DB_COLLECTION')
        ),
        test=TestDB(
            test=os.getenv('TEST_DB').lower() in (1, 'true')
        )

    )


templates = [
    {"name": "MyForm", "user_name": "text", "order_date": "date"},
    {"name": "OrderForm", "user_name": "text", "lead_email": "email"},
    {"name": "FeedbackForm", "user_name": "text", "email": "email", "phone": "phone"},
    {"name": "SurveyForm", "user_name": "text", "age": "text", "feedback": "text"}
]
