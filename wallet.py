from helpers import pretty_print, intercept_keyboard_interrupts
from account import Account
import config
from manage import Manage
from messages import wallet as console_messages


def main(account):
    # intercept keyboard interrupts for forcefully killing wallet
    # Would help us gracefully exiting the wallet upon user confirmation
    intercept_keyboard_interrupts(main)
    execute = 1

    while execute:
        Manage(account)


def init():
    pretty_print(console_messages['welcome'])
    initial_settings = config.settings
    account = Account(initial_settings)

    return main(account)


if __name__ == '__main__':
    init()
