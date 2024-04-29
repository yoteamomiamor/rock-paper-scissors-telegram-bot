from random import choice
from lexicon import LEXICON_RU


def randomize_choice() -> str:
    return choice((LEXICON_RU.button_rock.value,
                   LEXICON_RU.button_paper.value,
                   LEXICON_RU.button_scissors.value,
                   ))

def get_winner(user_choice: str, bot_choice: str) -> str:
    choice_value = {
        LEXICON_RU.button_rock.value: 0,
        LEXICON_RU.button_paper.value: 1,
        LEXICON_RU.button_scissors.value: 2
    }

    result = (
        LEXICON_RU.reply_to_draw.value,
        LEXICON_RU.reply_to_victory.value,
        LEXICON_RU.reply_to_loss.value,
    )

    return result[choice_value[user_choice] - choice_value[bot_choice]]
