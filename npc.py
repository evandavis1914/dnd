from utilities import *
from races import races
from roles import roles


class Character(object):

    def __init__(self, name=None, race=None, abilities=None, role=None):
        self.name = name or self.get_name()
        self.race = race or self.get_race()
        self.abilities = abilities or self.get_abilities()
        self.role = role or self.get_role()

    @yes_no
    def get_name(self):
        name = input('Choose a Name for your Adventurer! >>> ')
        verbiage = 'You Have Chosen {}. Are you sure?'.format(name)
        return name, verbiage

    @yes_no
    def get_role(self):
        role = choose_from_selection(sorted(roles.keys()), 'Class')
        verbiage = 'You Have Chosen {}. Are you sure?'.format(role)
        return role, verbiage

    @yes_no
    def get_race(self):
        race = choose_from_selection(sorted(races.keys()), 'Race')
        verbiage = 'You Have Chosen {}. Are you sure?'.format(race)
        return race, verbiage

    @yes_no
    def get_abilities(self):
        stats = self.set_attribute_scores()
        print(self.display_attributes(stats))
        verbiage = 'Do You Wish to Keep these Scores?'
        return stats, verbiage

    def set_attribute_scores(self):
        stats = dict(
            intelligence = self.roll_attribute(),
            strength = self.roll_attribute(),
            charisma = self.roll_attribute(),
            wisdom = self.roll_attribute(),
            dexterity = self.roll_attribute(),
            constitution = self.roll_attribute()
        )
        modifiers = races[self.race]
        for stat, modifier in modifiers.items():
            stats[stat] += modifier
        return stats

    def display_attributes(self, stats):
        display = ''
        for stat, value in stats.items():
            display += '{:>15} = {:>2}\n'.format(stat.capitalize(), value)
        return display

    def roll_attribute(self):
        return sum(sorted([roll_dice(6) for _ in range(4)])[1:])

    def __str__(self):
        return '{} the {} {}\n{}'.format(
            self.name,
            self.race.title(),
            self.role.title(),
            self.display_attributes(self.abilities)
        )
