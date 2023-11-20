"""Summing the elements of a list using different loops."""

__author__ = "730597416"


def w_sum(vals: list[float]) -> float:
    """Part 1: using a while loop."""
    if len(vals) == 0:
        result = 0.0
    else:
        index = 0
        result = 0.0
        while index < len(vals):
            result += vals[index]
            index += 1
    return result


def f_sum(vals: list[float]) -> float:
    """Part 2: using a for ... in ... loop."""
    result = 0.0
    for val in vals:
        result += val
    return result


def f_range_sum(vals: list[float]) -> float:
    """Part 3: using a for ... in range(...) loop."""
    result = 0.0
    for index in range(len(vals)):
        result += vals[index]
    return result