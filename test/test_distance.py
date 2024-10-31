import sys
import os
import pytest
from geopy.distance import geodesic

sys.path.append(os.path.abspath("../"))  
from hw4_lib.hw4_lib.hw4 import compute_distance, sum_general_int_list

# Tests for compute_distance function
def test_compute_distance_basic():
    pairs = [((41.23, 23.5), (41.5, 23.4))]
    result = compute_distance(pairs)
    assert len(result) == 1
    assert isinstance(result[0], float)
    # The actual distance should be approximately 31.5 km
    assert pytest.approx(result[0], rel=0.1) == 31.5

def test_compute_distance_multiple_pairs():
    pairs = [
        ((41.23, 23.5), (41.5, 23.4)),
        ((52.38, 20.1), (52.3, 17.8))
    ]
    result = compute_distance(pairs)
    assert len(result) == 2
    assert all(isinstance(x, float) for x in result)

def test_compute_distance_same_point():
    pairs = [((41.23, 23.5), (41.23, 23.5))]
    result = compute_distance(pairs)
    assert result[0] == 0

def test_compute_distance_empty_list():
    pairs = []
    result = compute_distance(pairs)
    assert result == []

def test_compute_distance_invalid_coordinates():
    # Testing with invalid latitude (>90)
    pairs = [((91.23, 23.5), (41.5, 23.4))]
    with pytest.raises(ValueError):
        compute_distance(pairs)

def test_sum_general_int_list_type_error():
    test_list = [[2], "3", [[1, 2], 5]]
    with pytest.raises(TypeError):
        sum_general_int_list(test_list)
