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


keyboard_choice = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=LEXICON_RU.button_rock),
        KeyboardButton(text=LEXICON_RU.button_paper),
        KeyboardButton(text=LEXICON_RU.button_scissors),
    ]],
    resize_keyboard=True,
)
