"""Combining two lists into a dictionary."""

__author__ = 730597416


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Check if the input lists contain different lengths or are empty."""
    if len(str_list) != len(int_list) or not str_list or not int_list:
        return {}
    
    """Create a dictionary by pairing elements from the two lists."""
    dictionary = {}
    for index in range(len(str_list)):
        dictionary[str_list[index]] = int_list[index]
    
    return dictionary