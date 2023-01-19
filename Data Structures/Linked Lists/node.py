"""
Node

Module containing the Node class used for linked lists and queues.
"""

__all__ = ["Node"]


class Node:
    """
    Definition of the Node class used in linked lists and queues.

    This is not the Node class used with doubly linked lists; those
    are in the doubly_linked_list module.

    Parameters:
        value: The value stored in the Node.

        next_node (Node or None): The node that this node links to.
            Default is None.
    """
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        """Return the value stored in the Node."""
        return self._value

    @property
    def next_node(self):
        """Return the node that this node links to."""
        return self._next_node

    def __repr__(self):
        next_node = self.next_node
        if next_node is None:
            next_node_string = ")"
        else:
            next_node_string = f", next_node={next_node.__repr__()})"

        return (f"{self.__class__.__qualname__}({self.value}"
                + next_node_string)

    def set_next_node(self, next_node):
        """Set the node that comes after this node."""
        self._next_node = next_node
