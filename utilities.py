import random
from time import sleep


def yes_no(func):
    def wrapper(*args, **kwargs):
        yes_no = 'n'
        while yes_no == 'n':
            data, verbiage = func(*args, **kwargs)
            yes_no = ask_yes_no(verbiage)
        return data
    return wrapper


def ask_yes_no(prompt):
    choice = None
    while choice not in ['y', 'n']:
        choice = input('\n{} (y/n) >>> '.format(prompt)).lower()
    return choice


def choose_from_selection(selection, title):
    while True:
        print('\nChoose A {}'.format(title))
        for idx, sel in enumerate(selection, 1):
            print(idx, sel.capitalize())
            # sleep(.5)
        # TODO: verifiy is integerable
        user_choice = int(input('>>> ')) - 1
        if user_choice >= 0 and user_choice < len(selection):
            return selection[user_choice]
        print('Invalid selection, dummy. Try again.')


def roll_dice(sides):
    return random.randint(1, sides)