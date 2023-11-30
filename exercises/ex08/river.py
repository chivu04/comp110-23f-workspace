"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730597416"


class River:
    """River ecosystem with fish and bears."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish and bears that exceed age limit."""
        new_fish = [fish for fish in self.fish if fish.age <= 3]
        new_bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = new_fish
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Remove a certain amount of fish from the river."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Simulate Bear's eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Remove hungry Bear's from River."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    def repopulate_fish(self):
        """Simulate Fish repopulation."""
        offspring = (len(self.fish) // 2) * 4
        self.fish += [Fish() for _ in range(offspring)]
        return None
    
    def repopulate_bears(self):
        """Simulate Bear repopulation."""
        offspring = len(self.bears) // 2
        self.bears += [Bear() for _ in range(offspring)]
        return None
    
    def view_river(self):
        """Visualize River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()

            
