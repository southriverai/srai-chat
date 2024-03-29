from typing import List, Optional

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from srai_chat.dao.store_document_base import StoreDocumentBase


class StoreDocumentMongo(StoreDocumentBase):
    def __init__(self, connection_string: str, database_name: str, collection_name: str):
        self.client = MongoClient(connection_string, server_api=ServerApi("1"))
        self.db = self.client.get_database(database_name)
        self.collection = self.db.get_collection(collection_name)

    def delete_all(self) -> int:
        delete_result = self.collection.delete_many({})
        return delete_result.deleted_count

    def count(self) -> int:
        return self.collection.count_documents({})

    def insert_one(self, message: dict) -> None:
        self.collection.insert_one(message)

    def find_one(self, query: dict) -> Optional[dict]:
        return self.collection.find_one(query)

    def find(self, query: dict) -> List[dict]:
        # TODO fix cursoring
        return self.collection.find(query)  # type: ignore

    def update_one(self, query: dict, update: dict, upsert=False) -> None:
        self.collection.update_one(query, update, upsert)
        # example:
        # {"$set": {"scedule_state": scedule_state}
