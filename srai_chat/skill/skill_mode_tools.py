import json

from srai_chat.command_base import CommandBase
from srai_chat.skill_base import SkillBase


class CommandModeReset(CommandBase):
    def __init__(self) -> None:
        super().__init__("mode_reset", "Resets the context of the chat")

    def execute_command(self, chat_id: str, command_message: str) -> dict:
        from srai_chat.service.context_manager import ContextManager

        context = ContextManager.get_instance()
        context.service_chat.message_chat(chat_id, f"Reseting chat history for {chat_id}")
        context.service_chat.mode_default.reset(chat_id)
        return {"message": "context was reset"}


class CommandModeHistory(CommandBase):
    def __init__(self) -> None:
        super().__init__("mode_history", "Prints the history to the chat")

    def execute_command(self, chat_id: str, command_message: str) -> dict:
        from srai_chat.service.context_manager import ContextManager

        context = ContextManager.get_instance()
        dao = context.service_persistency.dao_prompt_config
        context.service_chat.message_chat(chat_id, f"Loading chat history for {chat_id}")
        prompt_config_input = dao.load_prompt_config(chat_id)
        if prompt_config_input is None:
            context.service_chat.message_chat(chat_id, "No history found")
        else:
            message = json.dumps(prompt_config_input.to_dict(), indent=4)
            context.service_chat.message_chat(chat_id, message)
        return {"message": "history was prined"}


class SkillModeTools(SkillBase):
    def __init__(self):
        super().__init__()
        self.add_command(CommandModeHistory())
        self.add_command(CommandModeReset())
