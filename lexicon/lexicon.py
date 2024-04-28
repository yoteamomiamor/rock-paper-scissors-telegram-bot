from enum import Enum


class LEXICON_RU(Enum):
    command_start: str = 'hii^^ wanna play rock-paper-scissors? :3'
    command_help: str = ('in this bot you can play rock-paper-scissors with me ^^ '
                         'you and i choose one of the items (rock-paper-scissors) '
                         'and someone wins according to the rules!!')

    button_yes: str = 'sure!!'
    button_no: str = 'not now'

    reply_to_agreement: str = 'yaaayy!! now make your choice ^^'
    reply_to_rejection: str = 'okie ;( maybe later.. right?'

    reply_to_victory: str = 'wow!! you won!!! O_o'
    reply_to_loss: str = 'yayy i won!! ehehehe >.<'
    reply_to_draw: str = 'we both won!!! hehe <3'

    ask_new_game: str = 'well, wanna play again??^^'

    button_rock: str = '🗿 rock'
    button_paper: str = '📜 paper'
    button_scissors: str = '✂️ scissors'

    no_reply: str = 'w-w-what did you mean by that...?'
    reaction: str = '🤯'
