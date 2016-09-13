import random
from time import sleep



def ask_yes_no(prompt):
	choice = None
	while choice not in ['y', 'n']:
		choice = input('{} (y/n) >>> '.format(prompt)).lower()
	return choice

def choose_race(races):
	print('Choose A Race')
	for idx, race in enumerate(races, 1):
		print(idx, race)
		sleep(.5)
	user_choice = int(input('>>> ')) - 1
	return races[user_choice]

def roll_dice(sides):
	return random.randint(1, sides)

def roll_attribute():
	return sum(sorted([roll_dice(6) for _ in range(4)])[1:])



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

races = sorted(['Elf', 'Human', 'Dwarf', 'Halfling', 'Gnome', 'Half-orc', 'Half-Elf'])

yes_no = 'n'
while yes_no == 'n':
	user_race = choose_race(races)
	yes_no = ask_yes_no('You Have Chosen {}. Are you sure?'.format(user_race))	

intelligence = roll_attribute()

if race.lower() == 'elf':
	intelligence += 2

print(intelligence)