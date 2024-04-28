from random import choice
from lexicon import LEXICON_RU


def randomize_choice() -> str:
    return choice((LEXICON_RU.button_rock,
                   LEXICON_RU.button_paper,
                   LEXICON_RU.button_scissors,
                   ))

def get_winner() -> str:
    return LEXICON_RU.reply_to_draw.value
