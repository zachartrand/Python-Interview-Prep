class Node:
    def __init__(self, value, link_node=None):
        self._value = value
        self._link_node = link_node

    def set_next_node(self, link_node):
        self._link_node = link_node

    def get_next_node(self):
        return self._link_node

    @property
    def value(self):
        return self._value
