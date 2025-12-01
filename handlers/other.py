from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

other_router = Router()

# Хендлер для сообщений, которые не попали в другие хендлеры
@other_router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU["other_answer"])