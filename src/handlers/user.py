from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode

from src.utils.text import user as user_text
from src.utils.filters import IsAdmin
from src.utils.keyboards.inline import user as user_inline_keyboard


router = Router(name='users')


@router.message(~IsAdmin(), Command('start'))
async def user_start_command(message: Message) -> None:
    """
        User Start Command
    """
    buttons = await user_inline_keyboard.start_inline_keyboard()
    await message.answer(
        user_text.START_USER_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=buttons,
    )
