import pymongo
from fastapi import HTTPException

from src.config.config import Config, load_config, templates

config: Config = load_config()

db_name = config.db.db_name
db_collection = config.db.db_collection


async def dump_test_base():
    """Если включен режим создания тестовай БД, то проверяем ее наличие и создаем, если ее нет"""
    if config.test.test:
        try:
            client = pymongo.MongoClient(config.db.url)
            if db_name not in client.list_database_names():
                db = client[db_name]
                collection = db[db_collection]
                collection.insert_many(templates)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")


async def get_base():
    """Получаем данные из БД"""
    try:
        client = pymongo.MongoClient(config.db.url)
        db = client[db_name]
        collection = db[db_collection]
        return collection
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")
