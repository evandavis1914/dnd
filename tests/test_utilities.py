from contextlib import redirect_stdout
from io import StringIO
from unittest import mock
import unittest

from utilities import ask_yes_no


class UtilitiesTests(unittest.TestCase):

    @mock.patch('builtins.input')
    def test_ask_yes_no_retries_if_input_is_not_valid(self, inp):
        inp.side_effect = ['x', 'y']
        ask_yes_no('')
        self.assertEqual(inp.call_count, 2)
        inp.side_effect = ['x', 'n']
        ask_yes_no('')
        self.assertEqual(inp.call_count, 4)

    @mock.patch('builtins.input')
    def test_ask_yes_no_accepts_Y_or_y(self, inp):
        inp.return_value = 'y'
        ask_yes_no('')
        self.assertEqual(inp.call_count, 1)
        inp.return_value = 'Y'
        ask_yes_no('')
        self.assertEqual(inp.call_count, 2)

    @mock.patch('builtins.input')
    def test_ask_yes_no_accepts_N_or_n(self, inp):
        inp.return_value = 'n'
        ask_yes_no('')
        self.assertEqual(inp.call_count, 1)
        inp.return_value = 'N'
        ask_yes_no('')
        self.assertEqual(inp.call_count, 2)


