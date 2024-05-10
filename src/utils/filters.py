from aiogram.types import Message
from aiogram.filters import BaseFilter

from src.config import settings


class IsAdmin(BaseFilter):
    """
        Filter to Check Is Admin User
    """
    async def __call__(self, message: Message):
        return message.from_user.id in settings.ADMINS_ID
