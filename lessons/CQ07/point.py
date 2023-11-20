"""Object Oriented Programming."""

from __future__ import annotations

__author__ = 730597416


class Point:
    """Class to represent (x, y) coordinate point."""
    x: float
    y: float
    
    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Construct a point."""
        self.x = init_x
        self.y = init_y
    
    def scale_by(self, factor: int) -> None:
        """Modify a point."""
        self.x *= factor
        self.y *= factor
        
    def scale(self, factor: int) -> Point:
        """Make a new point."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)

    def __str__(self) -> str:
        """Return a string representation of the point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Overload the multiplication * operator."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)

    def __add__(self, factor: int | float) -> Point:
        """Overload the addition + operator."""
        new_x = self.x + factor
        new_y = self.y + factor
        return Point(new_x, new_y)