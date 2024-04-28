from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon import LEXICON_RU


keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=LEXICON_RU.button_yes.value),
        KeyboardButton(text=LEXICON_RU.button_no.value),
        ]],
    resize_keyboard=True,
    )


keyboard_choice = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=LEXICON_RU.button_rock.value),
        KeyboardButton(text=LEXICON_RU.button_paper.value),
        KeyboardButton(text=LEXICON_RU.button_scissors.value),
    ]],
    resize_keyboard=True,
)
