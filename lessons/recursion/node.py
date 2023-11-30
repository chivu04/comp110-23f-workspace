"""Node class for a linked list."""

from __future__ import annotations

__author__ = "730597416"


class Node:
    """Node class for linked list."""
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a node."""
        self.data = data
        self.next = next 

    def __str__(self) -> str:
        """Return a string representation of the node."""
        if self.next is None:
            # base case
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + "->" + str(self.next)
        
    def head(self) -> int: 
        """Return the data attribute for first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()