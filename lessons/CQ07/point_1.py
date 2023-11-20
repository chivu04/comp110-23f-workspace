"""Object Oriented Programming."""

__author__ = 730597416


class Point:
    """Creating a Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating a Point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> 'Point':
        """Creating a new Point."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)