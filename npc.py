import random
from time import sleep

races = {
    'elf':
    {
            'dexterity': 2,
            'constitution': -2
    },
    'human': {},
    'dwarf':
    {
            'constitution': 2,
            'charisma': -2
    },
    'gnome':
    {
            'constitution': 2,
            'strength': -2
    },
    'half-Elf': {},
    'half-Orc':
    {
            'strength': 2,
            'intelligence' : -2,
            'charisma': -2
    },
    'halfling':
    {
            'dexterity': 2,
            'strength': -2
    },

}


roles = {
    'wizard': {},
    'rogue' : {},
    'fighter': {},
    'sorcerer': {},
    'ranger':{},
    'cleric':{},
}


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
            sleep(.5)
        user_choice = int(input('>>> ')) - 1
        if user_choice > 0 and user_choice <= len(selection):
            return selection[user_choice]
        print('Invalid selection, dummy. Try again.')



def roll_dice(sides):
    return random.randint(1, sides)


def roll_attribute():
    return sum(sorted([roll_dice(6) for _ in range(4)])[1:])


def set_attribute_scores(race):
    stats = dict(
        intelligence = roll_attribute(),
        strength = roll_attribute(),
        charisma = roll_attribute(),
        wisdom = roll_attribute(),
        dexterity = roll_attribute(),
        constitution = roll_attribute()
    )
    modifiers = races[user_race]
    for stat, modifier in modifiers.items():
        stats[stat] += modifier
    return stats


def display_attributes(stats):
    for stat, value in stats.items():
        print('{:>15} = {:>2}'.format(stat.capitalize(), value))

def yes_no(func):
    def wrapper(*args, **kwargs):
        yes_no = 'n'
        while yes_no == 'n':
            data, verbiage = func(*args, **kwargs)
            yes_no = ask_yes_no(verbiage)
        return data
    return wrapper


@yes_no
def set_race(races):
    user_race = choose_from_selection(sorted(races.keys()), 'Race')
    verbiage = 'You Have Chosen {}. Are you sure?'.format(user_race)
    return user_race, verbiage


@yes_no
def set_attributes(user_race):
    stats = set_attribute_scores(user_race)
    display_attributes(stats)
    verbiage = 'Do You Wish to Keep these Scores?'
    return stats, verbiage


@yes_no
def set_class(roles):
    user_class = choose_from_selection(sorted(roles.keys()), 'Class')
    verbiage = 'You Have Chosen {}. Are you sure?'.format(user_class)
    return user_class, verbiage


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

user_race = set_race(races)
stats = set_attributes(user_race)
user_class = set_class(roles)
