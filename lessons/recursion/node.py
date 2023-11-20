"""Node class for a linked list."""

from __future__ import annotations

class Node:

    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a node."""
        self.data = data
        self.next = next 

    def __str__(self) -> str:
        if self.next is None:
            # base case
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + "->" + str(self.next)
    