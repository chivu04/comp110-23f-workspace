"""EX04 - 'list' Utility."""

__author__ = "730597416"


def all(list_of_integers: list[int], int: int) -> bool:
    """Check if all integers in the given list are equal to the target integer."""
    if len(list_of_integers) == 0:
        return False
    index = 0
    while index < len(list_of_integers):
        if int != list_of_integers[index]:
            return False
        index += 1
    return True


def max(integers: list[int]) -> int:
    """Find the largest integer in the given list."""
    if len(integers) == 0:
        raise ValueError("max() arg is an empty List")
    max_number = integers[0]
    index = 1
    while index < len(integers):
        if integers[index] > max_number:
            max_number = integers[index]
        index += 1
    return max_number


def is_equal(list1: list[int], list2: list[int]) -> int:
    """Check if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True