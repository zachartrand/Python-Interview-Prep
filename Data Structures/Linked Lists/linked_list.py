#!/usr/bin/env python3
"""
Linked List

Module containing a class for the Linked List data type.
"""

__all__ = ["LinkedList"]

from node import Node


def main():
    # The commented lines of code below were from Codecademy.
    # I made a new set of test lines below those.
    #
    # ll = LinkedList(5)
    # ll.insert_beginning(70)
    # ll.insert_beginning(5675)
    # ll.insert_beginning(90)
    # print(ll.stringify_list())  # 90 5675 70 5
    # print()

    ll = LinkedList()
    numbers = [2, 2, 10, 4, 1, 4, 5, 9, 1, 10, 6,
               2, 5, 3, 3, 4, 2, 8, 10, 3, 7, 7]
    for n in reversed(numbers):
        ll.insert_beginning(n)
    print(f"Linked List (size: {ll.size}):")
    print(ll.stringify_list())
    print()
    print(f"Head: {ll.peek()} Tail: {ll.tail.value} "
          f"Middle: {ll.get_middle_node().value}")
    print()
    n = -1
    while n < 0:
        s = input("Which value would you like to remove? (1 - 10)\n")
        try:
            possible_n = int(s)
            if possible_n in range(1, 11):
                n = possible_n
            else:
                print()
                print(f"{s} is not in the Linked List...\n")
        except:
            print()
            print("The value must be an integer between 1 and 10.\n")
    print()
    print(f"Removing all nodes equal to {n}...")
    ll.remove_all_nodes_with_value(n)
    print("Done!\n")
    print(f"Updated Linked List: (size: {ll.size})")
    print(ll.stringify_list())
    print()
    print(f"Head: {ll.peek()}")
    print(f"Middle: {ll.get_middle_node().value}")
    print(f"Tail: {ll.tail.value}")


class LinkedList:
    """
    A linked list implimentation.

    Attributes:
        head (Node or None): The node at the head of the linked list.
        tail (Node or None): The node at the end of the linked list.
    """
    def __init__(self, value=None):
        self._size: int = 0

        if value is None:
            self._head = None
            self._tail = None
        else:
            node = Node(value)
            self._head = node
            self._tail = node
            self._size += 1

    @property
    def head(self) -> Node:
        return self._head

    @property
    def tail(self) -> Node:
        return self._tail

    @property
    def size(self):
        return self._size

    def peek(self):
        """Return the value of the head node if it exists."""
        if self.head is not None:
            return self.head.value
        else:
            print("List is empty.")

    def insert_beginning(self, new_value) -> None:
        new_node = Node(new_value)
        new_node.set_next_node(self._head)
        self._head = new_node
        self._size += 1

        if self._tail is None:
            self._tail = new_node

    def append(self, new_value) -> None:
        new_node = Node(new_value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next_node(new_node)
            self._tail = new_node

        self._size += 1

    def stringify_list(self) -> str:
        node_list = []
        node = self._head
        while node is not None:
            node_list.append(f"{node.value}")
            node = node.next_node

        return "-".join(node_list)

    def remove_node(self, value_to_remove) -> None:
        current_node = self._head
        if current_node is not None:
            if current_node.value == value_to_remove:
                self._head = current_node.next_node
                self._size -= 1
                if self.head is None:
                    self._tail = None
            else:
                while current_node is not None:
                    next_node = current_node.next_node
                    if (next_node is not None
                        and next_node.value == value_to_remove):
                        current_node.set_next_node(next_node.next_node)
                        self._size -= 1
                        current_node = None
                    else:
                        if next_node is None:
                            self._tail = current_node

                        current_node = next_node

    def remove_all_nodes_with_value(self, value_to_remove) -> None:
        current_node = self._head
        if current_node is not None:
            count: int = 0
            while (current_node is not None
                    and current_node.value == value_to_remove):
                current_node = current_node.next_node
                count += 1

            self._head = current_node
            self._size -= count

            while current_node is not None:
                next_node = current_node.next_node
                count = 0
                while (next_node is not None
                       and next_node.value == value_to_remove):
                    next_node = next_node.next_node
                    count += 1

                current_node.set_next_node(next_node)
                if next_node is None:
                    self._tail = current_node

                current_node = next_node
                self._size -= count

    def swap_nodes(self, val1, val2) -> None:
        if val1 == val2:
            print(f"Elements are the same ({val1}) - no swap needed.")

            return None

        print(f"Swapping {val1} with {val2}...")

        node1_prev = None
        remaining_val = None

        node1 = self._head
        while node1 is not None:
            node1_val = node1.value
            if node1_val == val1:
                remaining_val = val2
                break

            elif node1_val == val2:
                remaining_val = val1
                break

            node1_prev = node1
            node1 = node1.next_node

        node2 = node1
        node2_prev = node1_prev
        while node2 is not None:
            if node2.value == remaining_val:
                break

            node2_prev = node2
            node2 = node2.next_node

        if (node1 is None or node2 is None):
            print("Swap not possible - one or "
                  "more elements is not in the list.")

            return None

        if node1_prev is None:
            self._head = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self._head = node1
        else:
            node2_prev.set_next_node(node1)

        node1_next_old = node1.next_node
        node1.set_next_node(node2.next_node)
        node2.set_next_node(node1_next_old)
        if self.tail == node2:
            self._tail = node1

        print("Swap complete!")

    def nth_to_last_node(self, n: int) -> Node:
        if n <= 1:
            return self.tail

        current_node = None
        tail_node = self._head
        count = 0

        while tail_node is not None:
            tail_node = tail_node.next_node
            count += 1
            if count >= n:
                if current_node is None:
                    current_node = self._head
                else:
                    current_node = current_node.next_node

        return current_node

    @staticmethod
    def _get_middle_node(head: Node) -> Node:
        if head is None:
            return None
        slow = head
        fast = head.next_node
        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node

        return slow

    def get_middle_node(self) -> Node:
        return self._get_middle_node(self.head)

    def _get_tail_from_head(self):
        current = self.head
        while current.next_node is not None:
            current = current.next_node

        return current

    def sort(self, sortby: str = "ascending") -> None:
        """
        Sorts the LinkedList by value. Uses Merge Sort algorithm.

        Keyword Argument:
            sortby (str): Set to "ascending" to sort values from low to
                high or set to "descending" to sort from high to low.
                Default is "ascending".
        """
        self._head = self._merge_sort(self.head, sortby)
        self._tail = self._get_tail_from_head()

    @classmethod
    def _merge_sort(cls, head: Node, sortby: str = "ascending") -> Node:
        # Exit out of the function if the linked list has no Nodes or
        # only one (1) Node.
        if head is None or head.next_node is None:
            return head

        # Split the LinkedList into two linked lists, splitting after
        # the middle node.
        mid = cls._get_middle_node(head)
        head2 = mid.next_node
        mid.set_next_node(None)

        # Sort the two new LinkedLists
        left_head = cls._merge_sort(head, sortby)
        right_head = cls._merge_sort(head2, sortby)
        # Merge the two sorted LinkedLists.
        sorted_head = cls._merge(left_head, right_head, sortby)

        return sorted_head

    _comparison = dict(
        ascending = lambda x, y: x.value < y.value,
        descending = lambda x, y: x.value > y.value,
    )

    @classmethod
    def _merge(cls, head1: Node, head2: Node,
               sortby: str = "ascending") -> Node:
        """
        Merge two linked lists in ascending order.

        Parameters:
            head1 (Node): Head of the left-hand linked list.
            head2 (Node): Head of the right-hand linked list.
            sortby (str): Set to "ascending" to sort values from low to
                high or set to "descending" to sort from high to low.
                Default is "ascending".

        Returns:
            merged.next_node (Node): Head of the merged linked lists.
        """
        merged = Node(None)  # Need to use a dummy node for the merge.

        temp = merged
        # While both heads are not None
        while (head1 is not None and head2 is not None):
            # TODO: Replace conditional with comparison function
            # for custom sorts (e.g. ascending or descending).
            if cls._comparison.get(sortby,
                    cls._comparison["ascending"])(head1, head2):
                temp.set_next_node(head1)
                head1 = head1.next_node
            else:
                temp.set_next_node(head2)
                head2 = head2.next_node
            temp = temp.next_node

        while head1 is not None:
            temp.set_next_node(head1)
            head1 = head1.next_node
            temp = temp.next_node

        while head2 is not None:
            temp.set_next_node(head2)
            head2 = head2.next_node
            temp = temp.next_node

        return merged.next_node


if __name__ == "__main__":
    main()
