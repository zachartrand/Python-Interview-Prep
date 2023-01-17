__all__ = ["Node", "DoublyLinkedList"]


def main():
    print()
    # Create your subway line here:
    subway = DoublyLinkedList()
    subway.add_to_head("Times Square")
    subway.add_to_head("Grand Central")
    subway.add_to_head("Central Park")
    print("Subway route:")
    print(subway.stringify_list())
    print()
    print("Adding Penn Station, Wall Street, and "
          "Brooklyn Bridge to the end of the route...\n")
    subway.add_to_tail("Penn Station")
    subway.add_to_tail("Wall Street")
    subway.add_to_tail("Brooklyn Bridge")
    print(subway.stringify_list())
    print()
    print("Removing first stop...")
    subway.remove_head()
    print("First stop removed!")
    print("Removing last stop...")
    subway.remove_tail()
    print("Last stop removed!")
    print()
    print("Updated subway route:")
    print(subway.stringify_list())
    print()
    print("Adding Times Square to beginning and end of route...")
    subway.add_to_head("Times Square")
    subway.add_to_tail("Times Square")
    print("Done!")
    print()
    print("Updated subway route:")
    print(subway.stringify_list())
    print()
    print("Removing all Times Square stops from the route...")
    subway.remove_by_value("Times Square")
    print("Done!")
    print()
    print("Updated subway route:")
    print(subway.stringify_list())
    print()


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head = new_head

        if self.tail is None:
            self.tail = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail = new_tail

        if self.head is None:
            self.head = new_tail

    def remove_head(self):
        removed_head = self.head

        if removed_head is not None:
            self.head = removed_head.get_next_node()

            if self.head is not None:
                self.head.set_prev_node(None)

            if removed_head == self.tail:
                self.remove_tail()

            return removed_head.get_value()

        return None

    def remove_tail(self):
        removed_tail = self.tail

        if removed_tail is not None:
            self.tail = removed_tail.get_prev_node()

            if self.tail is not None:
                self.tail.set_next_node(None)

            if removed_tail == self.head:
                self.remove_head()

            return removed_tail.get_value()

        return None

    def remove_by_value(self, value_to_remove, mode="head"):
        assert isinstance(mode, str)
        if mode.lower().startswith("h"):
            return self._head_remove_by_value(value_to_remove)
        elif mode.lower().startswith("t"):
            return self._tail_remove_by_value(value_to_remove)

        raise ValueError("""mode should be either "head" or "tail".""")

    def _head_remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove is None:
            return None

        if node_to_remove == self.head:
            self.remove_head()
        elif node_to_remove == self.tail:
            self.remove_tail()
        else:
            prev_node = node_to_remove.get_prev_node()
            next_node = node_to_remove.get_next_node()
            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)

        return node_to_remove

    def _tail_remove_by_value(self, value_to_remove):
        """
        Remove the first node from the list that matches the 
        value_to_remove, starting from the tail and working backwards 
        through the list. 
        """
        node_to_remove = None
        current_node = self.tail

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_prev_node()

        if node_to_remove is None:
            return None

        if node_to_remove == self.head:
            self.remove_head()
        elif node_to_remove == self.tail:
            self.remove_tail()
        else:
            prev_node = node_to_remove.get_prev_node()
            next_node = node_to_remove.get_next_node()
            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)

        return node_to_remove

    def stringify_list(self):
        string_list = []
        current_node = self.head

        while current_node:
            if current_node.get_value() != None:
                string_list.append(f"{current_node.get_value()}")

            current_node = current_node.get_next_node()

        return "\n".join(string_list)


if __name__ == "__main__":
    main()
