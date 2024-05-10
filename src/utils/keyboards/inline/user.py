from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.config import settings


async def start_inline_keyboard() -> InlineKeyboardMarkup:
    """
        Start Inline Keyboard User
    """
    url: str = settings.WEB_APP_URL
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Order Food', web_app=WebAppInfo(url=url))],
        ]
    )

