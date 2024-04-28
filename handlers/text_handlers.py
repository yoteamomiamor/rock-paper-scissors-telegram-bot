from aiogram import Router, F
from aiogram.types import Message

from lexicon import LEXICON_RU
from keyboards import keyboard_choice


router = Router()
router.message.filter(F.text)


@router.message(F.text == LEXICON_RU.button_yes.value)
async def process_agreement(message: Message):
    await message.answer(
        text=LEXICON_RU.reply_to_agreement.value,
        reply_markup=keyboard_choice,
    )


@router.message(F.text == LEXICON_RU.button_no.value)
async def process_rejection(message: Message):
    await message.answer(
        text=LEXICON_RU.reply_to_rejection.value
    )