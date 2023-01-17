#!/usr/bin/env python3
"""
A Choose Your Own Adventure game using a tree node data structure.
"""
##################
# TREENODE CLASS #
##################
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        if node not in self.choices:
            self.choices.append(node)

    def traverse(self):
        valid_choices = ["1", "2"]
        story_node = self
        print(story_node.story_piece)
        while story_node.choices:
            choice = input()
            while choice not in valid_choices:
                choice = input("Enter 1 or 2 to continue the story: \n")
            chosen_index = int(choice) - 1
            chosen_child = story_node.choices[chosen_index]
            print(chosen_child.story_piece)
            story_node = chosen_child


######################
# VARIABLES FOR TREE #
######################
story_root = TreeNode(
    """
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!
    Do you:
    1 ) Roar back!
    2 ) Run to the left...
    """.replace("\n    ", "\n")
)

choice_a = TreeNode(
    """
    The bear is startled and runs away.
    Do you:
    1 ) Shout 'Sorry bear!'
    2 ) Yell 'Hooray!'
    """.replace("\n    ", "\n")
)
choice_b = TreeNode(
    """
    You come across a clearing full of flowers.
    The bear follows you and asks 'what gives?'
    Do you:
    1 ) Gasp 'A talking bear!'
    2 ) Explain that the bear scared you.
    """.replace("\n    ", "\n")
)

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a1 = TreeNode(
    """
    The bear returns and tells you it's been
    a rough week. After making peace with
    a talking bear, he shows you the way out of
    the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
    """.replace("\n    ", "\n")
)
choice_a2 = TreeNode(
    """
    The bear returns and tells you that
    bullying is not okay before leaving you
    alone in the wilderness.

    YOU REMAIN LOST.
    """.replace("\n    ", "\n")
)

choice_a.add_child(choice_a1)
choice_a.add_child(choice_a2)

choice_b1 = TreeNode(
    """
    The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

    YOU REMAIN LOST.
    """.replace("\n    ", "\n")
)
choice_b2 = TreeNode(
    """
    The bear understands and apologizes for startling you. Your new friend shows you a
    path leading out of the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
    """.replace("\n    ", "\n")
)

choice_b.add_child(choice_b1)
choice_b.add_child(choice_b2)

# user_choice = input("What is your name? \n")

if __name__ == "__main__":
    print("Once upon a time...")
    story_root.traverse()
