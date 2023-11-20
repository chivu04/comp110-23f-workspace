def value_exists (test_dict: dict[str, int], test_val: int) -> bool:
    """Returns True if the int exists as a value in the dictionary."""
    for elem in test_dict:
        if test_dict[elem] == test_val:
            return True
        else:
            return False