import pytest

from Recursion.ReverseString import Solution

@pytest.fixture
def sol():
    return Solution()

def test_empty_list(sol):
    input_list = []
    expected_output = []
    sol.reverseString(input_list)
    assert input_list == expected_output

def test_single_character(sol):
    input_list = ["a"]
    expected_output = ["a"]
    sol.reverseString(input_list)
    assert input_list == expected_output

def test_two_characters(sol):
    input_list = ["h", "i"]
    expected_output = ["i", "h"]
    sol.reverseString(input_list)
    assert input_list == expected_output

def test_even_length_string(sol):
    input_list = ["h", "e", "l", "l", "o"]
    expected_output = ["o", "l", "l", "e", "h"]
    sol.reverseString(input_list)
    assert input_list == expected_output

def test_odd_length_string(sol):
    input_list = ["r", "a", "c", "e", "c", "a", "r"]
    expected_output = ["r", "a", "c", "e", "c", "a", "r"]
    sol.reverseString(input_list)
    assert input_list == expected_output