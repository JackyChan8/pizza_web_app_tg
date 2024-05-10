from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.utils.filters import IsAdmin


router = Router(name='admin')


@router.message(IsAdmin(), Command('start'))
async def admin_start_command(message: Message, state: FSMContext):
    """
        Admin Start Command
    """
    pass
