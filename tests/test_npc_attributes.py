from unittest import mock
import unittest

from npc import Character


@mock.patch('random.randint', return_value=3)
class NPCAttributeTests(unittest.TestCase):

    def test_roll_attribute_returns_sum_of_highest_of_three(self, random):
        random.side_effect = [1, 3, 5, 7]
        char = Character(name='Pippin', race='elf', abilities='x', role='wizard')
        attribute = char.roll_attribute()
        self.assertEqual(attribute, 15)

    def test_set_attribute_scores_for_elf(self, random):
        char = Character(name='Pippin', race='elf', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 9,
            'constitution': 7,
            'dexterity': 11,
            'intelligence': 9,
            'strength': 9,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_human(self, random):
        char = Character(name='Pippin', race='human', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 9,
            'constitution': 9,
            'dexterity': 9,
            'intelligence': 9,
            'strength': 9,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_dwarf(self, random):
        char = Character(name='Pippin', race='dwarf', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 7,
            'constitution': 11,
            'dexterity': 9,
            'intelligence': 9,
            'strength': 9,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_gnome(self, random):
        char = Character(name='Pippin', race='gnome', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 9,
            'constitution': 11,
            'dexterity': 9,
            'intelligence': 9,
            'strength': 7,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_half_elf(self, random):
        char = Character(name='Pippin', race='half-elf', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 9,
            'constitution': 9,
            'dexterity': 9,
            'intelligence': 9,
            'strength': 9,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_half_orc(self, random):
        char = Character(name='Pippin', race='half-orc', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 7,
            'constitution': 9,
            'dexterity': 9,
            'intelligence': 7,
            'strength': 11,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)

    def test_set_attribute_scores_for_halfling(self, random):
        char = Character(name='Pippin', race='halfling', abilities='x', role='wizard')
        scores = char.set_attribute_scores()
        expected = {
            'charisma': 9,
            'constitution': 9,
            'dexterity': 11,
            'intelligence': 9,
            'strength': 7,
            'wisdom': 9
        }
        self.assertEqual(scores, expected)
