from aiogram import Router, F
from aiogram.types import Message, ReactionTypeEmoji

from lexicon import LEXICON_RU
from keyboards import keyboard_choice


router = Router()
router.message.filter(F.text)


choices = [
    LEXICON_RU.button_rock,
    LEXICON_RU.button_paper,
    LEXICON_RU.button_scissors
]


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


@router.message(F.text.in_([]))


@router.message()
async def process_empty_message(message: Message):
    await message.reply(text=LEXICON_RU.no_reply.value)
    await message.react(
        reaction=[ReactionTypeEmoji(emoji=LEXICON_RU.reaction.value)])
