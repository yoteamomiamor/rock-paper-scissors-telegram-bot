from random import choice
from typing import Literal
from lexicon import LEXICON_RU


def randomize_choice() -> str:
    return choice((LEXICON_RU.Choice.button_rock,
                   LEXICON_RU.Choice.button_paper,
                   LEXICON_RU.Choice.button_scissors,
                   ))
