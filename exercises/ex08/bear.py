"""File to define Bear class."""

__author__ = "730597416"


class Bear:
    """Bear in river ecosystem."""
    def __init__(self) -> None:
        """Initialize a new Bear with age 0 and hunger score 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """Simulate one day of life in the river."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Beat eats fish."""
        self.hunger_score += num_fish