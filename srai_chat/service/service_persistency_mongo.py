from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from srai_chat.dao.dao_chat_message import DaoChatMessage
from srai_chat.dao.dao_prompt_config import DaoPromptConfig
from srai_chat.dao.store_document_mongo import StoreDocumentMongo
from srai_chat.service.context_manager import ContextManager
from srai_chat.service.service_base import ServiceBase


class ServicePersistencyMongo(ServiceBase):
    def __init__(self, context: ContextManager, connection_string: str, database_name: str):
        super().__init__(context)
        # Create a new client and connect to the server
        self.client = MongoClient(connection_string, server_api=ServerApi("1"))
        self.mongo_database = self.client.get_database(database_name)
        # daos

        self.dao_message = DaoChatMessage(StoreDocumentMongo(connection_string, database_name, "chat_message"))
        self.dao_prompt_config = DaoPromptConfig(StoreDocumentMongo(connection_string, database_name, "prompt_config"))
        self.dao_skill_state = DaoChatMessage(StoreDocumentMongo(connection_string, database_name, "skill_state"))
        self.dao_mode_state = DaoChatMessage(StoreDocumentMongo(connection_string, database_name, "mode_state"))

    def initialize(self):
        return super().initialize()
