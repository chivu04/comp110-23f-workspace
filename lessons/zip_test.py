"""Test my zip function."""

__author__ = 730597416

from lessons.zip import zip


def test_empty_lists():
    """The zip function should return an empty dictionary when both input lists are empty."""
    result = zip([], [])
    assert result == {}
    

def test_equal_length_lists():
    """The zip function should create a dictionary by pairing elements from the two lists."""
    str_list = ["apple", "banana", "cherry"]
    int_list = [1, 2, 3]
    expected_result = {"apple": 1, "banana": 2, "cherry": 3}
    
    result = zip(str_list, int_list)
    assert result == expected_result
    
    
def test_unequal_length_lists():
    """The zip function should return an empty dictionary when input lists have different lengths."""
    str_list = ["apple", "banana", "cherry"]
    int_list = [1, 2]
    result = zip(str_list, int_list)
    assert result == {}