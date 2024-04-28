from random import choice
from typing import Literal
import lexicon


def randomize_choice() -> Literal[lexicon.LEXICON_RU.button_rock,
                                  lexicon.LEXICON_RU.button_paper,
                                  lexicon.LEXICON_RU.button_scissors]:
    return choice((lexicon.LEXICON_RU.button_rock,
                   lexicon.LEXICON_RU.button_paper,
                   lexicon.LEXICON_RU.button_scissors,
                   ))
