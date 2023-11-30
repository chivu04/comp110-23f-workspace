"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730597416"


class Simpy:
    """Utility class for numerical operations."""

    def __init__(self, values: list[float]):
        """Constructor for Simpy class."""
        self.values = values

    def __str__(self) -> str:
        """String representation of the Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, values: float, num_values: int) -> None:
        """Fill the Simpy object's values with a specific number of repeating values."""
        self.values = [values] * num_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the Simpy object's values with a range of values."""
        assert step != 0.0
        self.values = []
        if start < stop:
            current_value = start
            while current_value < stop:
                self.values.append(current_value)
                current_value += step
        else:
            current_value = start
            while current_value > stop:
                self.values.append(current_value)
                current_value += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the Simpy object's values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloaded addition operator for Simpy objects."""
        result_values = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_values.append(self.values[i] + rhs.values[i])
        else:
            for x in self.values:
                result_values.append(x + rhs)
        return Simpy(result_values)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloaded power operator for Simpy objects."""
        result_values = []
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                result_values.append(self.values[i] ** rhs.values[i])
        else:
            for x in self.values:
                result_values.append(x ** rhs)
        return Simpy(result_values)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloaded equality operator for Simpy objects."""
        result_values = []
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                result_values.append(self.values[i] == rhs.values[i])
        else:
            for x in self.values:
                result_values.append(x == rhs)
        return result_values

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloaded greater-than operator for Simpy objects."""
        result_values = []
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                result_values.append(self.values[i] > rhs.values[i])
        else:
            for x in self.values:
                result_values.append(x > rhs)
        return result_values

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloaded subscription notation to get specific values or filter with a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            filtered_values = []
            for i in range(len(self.values)):
                if rhs[i]:
                    filtered_values.append(self.values[i])
            return Simpy(filtered_values)