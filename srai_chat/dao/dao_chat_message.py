from typing import List

from srai_chat.dao.dao_base import DaoBase
from srai_chat.dao.store_document_base import StoreDocumentBase


class ChatMessage:
    def __init__(self, message_id: str, channel_id: str, author_id: str, author_name: str, message_content: dict):
        self.message_id = message_id
        self.channel_id = channel_id
        self.author_id = author_id
        self.author_name = author_name
        self.message_content = message_content

    def to_dict(self) -> dict:
        return {
            "message_id": self.message_id,
            "channel_id": self.channel_id,
            "author_id": self.author_id,
            "author_name": self.author_name,
            "message_content": self.message_content,
        }

    @staticmethod
    def from_dict(dict_message: dict) -> "ChatMessage":
        message_id = dict_message["message_id"]
        chat_id = dict_message["channel_id"]
        author_id = dict_message["author_id"]
        author_name = dict_message["author_name"]
        message_content = dict_message["message_content"]
        return ChatMessage(message_id, chat_id, author_id, author_name, message_content)


class DaoChatMessage(DaoBase):
    def __init__(self, store_document: StoreDocumentBase) -> None:
        super().__init__(store_document)

    def save_message(self, message: ChatMessage) -> None:
        self.store_document.insert_one(message.to_dict())

    def load_messages(self, query: dict) -> List[dict]:
        return self.store_document.find(query)

    def load_messages_all(self) -> List[dict]:
        return self.store_document.find({})  # type: ignore
