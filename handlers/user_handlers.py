from aiogram import Router, F
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON_RU
from keyboards import keyboard_start
from . import text_handlers


router = Router()
router.include_router(text_handlers.router)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        LEXICON_RU.command_start.value,
        reply_markup=keyboard_start,
        )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU.command_help.value)


@router.message()
async def process_empty_message(message: Message):
    try:
        await message.reply(text=LEXICON_RU.no_reply.value)
        await message.react(
            reaction=[ReactionTypeEmoji(emoji=LEXICON_RU.reaction.value)]
            )
    except ValueError:
        await message.answer(text=LEXICON_RU.no_reply.value)
