import random
from time import sleep

races = {
	'Elf':
	{
		'dexterity': 2,
		'constitution': -2		
	},
	'Human': {},
	'Dwarf':
	{	
		'constitution': 2,
		'charisma': -2
	},
	'Gnome':
	{
		'constitution': 2,
		'strength': -2
	},
	'Half-Elf': {},
	'Half-Orc':
	{
		'strength': 2,
		'intelligence' : -2,
		'charisma': -2
	},
	'Halfling':
	{
		'dexterity': 2,
		'strength': -2
	},

}


roles = {
	'Wizard': {},
	'Rogue' : {},
}


def ask_yes_no(prompt):
	choice = None
	while choice not in ['y', 'n']:
		choice = input('\n{} (y/n) >>> '.format(prompt)).lower()
	return choice


def choose_race(races):
	print('\nChoose A Race')
	for idx, race in enumerate(races, 1):
		print(idx, race)
		sleep(.5)
	user_choice = int(input('>>> ')) - 1
	return races[user_choice]


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

def choose_class():
	pass


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

yes_no = 'n'
while yes_no == 'n':
	user_race = choose_race(sorted(races.keys()))
	yes_no = ask_yes_no('You Have Chosen {}. Are you sure?'.format(user_race))	

yes_no = 'n'
while yes_no == 'n':
	stats = set_attribute_scores(user_race)
	display_attributes(stats)
	yes_no = ask_yes_no('Do You Wish to Keep these Scores?')


# yes_no = 'n'
# while yes_no == 'n':

	