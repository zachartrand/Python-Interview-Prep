class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print(f"Removing {child_node.value} from {self.value}")
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # Moves through each node referenced from self downwards.
        nodes_to_visit = [self]
        while nodes_to_visit:
            nodes_to_visit.extend(current_node.children)
            current_node = nodes_to_visit.pop()
            print(current_node.value)
