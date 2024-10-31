import sys
import os
import pytest

sys.path.append(os.path.abspath("../"))  
from hw4_lib.hw4_lib.hw4 import compute_distance, sum_general_int_list

# Tests for sum_general_int_list function
def test_sum_general_int_list_basic():
    test_list = [[2], 3, [[1, 2], 5]]
    assert sum_general_int_list(test_list) == 13

def test_sum_general_int_list_empty():
    assert sum_general_int_list([]) == 0

def test_sum_general_int_list_single_integer():
    assert sum_general_int_list([5]) == 5

def test_sum_general_int_list_nested_empty_lists():
    assert sum_general_int_list([[], [[]], []]) == 0

def test_sum_general_int_list_complex_nesting():
    test_list = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
    assert sum_general_int_list(test_list) == 48

def test_sum_general_int_list_negative_numbers():
    test_list = [[2], -3, [[1, -2], 5]]
    assert sum_general_int_list(test_list) == 3

def test_sum_general_int_list_zero():
    test_list = [[0], 0, [[0, 0], 0]]
    assert sum_general_int_list(test_list) == 0

def test_sum_general_int_list_single_nested_list():
    test_list = [[[[[1]]]]]
    assert sum_general_int_list(test_list) == 1
