import sys
import os
import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hw4_lib', 'hw4_lib')))
from hw4 import count_simba

def test_count_simba_three_times():
    list_of_strings = ["Simba is the king of the Pride Lands", "Simba is brave", "Simba"]
    word = "Simba"
    assert count_simba(list_of_strings, word) == 3, "The word 'Simba' is being counted should appear 3 times."