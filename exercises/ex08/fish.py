"""File to define Fish class."""

__author__ = "730597416"


class Fish:
    """Fish in river ecosystem."""
    def __init__(self) -> None:
        """Initialize a new Fish with age 0."""
        self.age = 0
        return None
    
    def one_day(self) -> None:
        """Simulate one day of life in the river."""
        self.age += 1
        return None