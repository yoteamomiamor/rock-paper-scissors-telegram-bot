from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from lexicon import LEXICON_RU


keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=LEXICON_RU.button_yes),
        KeyboardButton(text=LEXICON_RU.button_no),
        ]],
    resize_keyboard=True,
    )
