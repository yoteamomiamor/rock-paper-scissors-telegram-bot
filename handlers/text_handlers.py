from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from asyncio import sleep

from lexicon import LEXICON_RU
from keyboards import keyboard_choice, keyboard_start
from tools import randomize_choice, get_winner


router = Router()
router.message.filter(F.text)


choices = [
    LEXICON_RU.button_rock.value,
    LEXICON_RU.button_paper.value,
    LEXICON_RU.button_scissors.value,
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
        text=LEXICON_RU.reply_to_rejection.value,
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(F.text.in_(choices))
async def process_game_reply(message: Message):
    reply = randomize_choice()

    await message.answer(
        text=reply,
        reply_markup=ReplyKeyboardRemove(),
        )

    await sleep(0.3)

    await message.answer(text=get_winner(message.text, reply))
    await message.answer(
        text=LEXICON_RU.ask_new_game.value,
        reply_markup=keyboard_start,
        )
