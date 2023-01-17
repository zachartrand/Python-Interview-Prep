r"""
Balanced Binary Search Tree

Given a sorted list of numbers a, write a function balanced_bst(a) to
create a balanced binary search tree. A balanced Binary Search Tree has
no more than one level of depth difference between the right and left
sides of the tree.

Each value in the list a should correspond to a node value. The return
value of balanced_bst() will be the root node of the balanced tree. An
empty array passed to balanced_bst() should return None.

For example, given a list a = [1,2,3,4,5,6,7,8], you want to create a
balanced tree that may resemble the following:

           5
          / \
         /   \
        3     7
       / \   / \
      2   4 6   8
     /
    1

The above figure represents a balanced tree because there is at most 1
level of difference between the depths of each side of the tree.

For this challenge you are given the class TreeNode with the members:

    value: the node value

    left: the left child node; defaults to None

    right: the right child node; defaults to None

The __str__() function is also implemented in the class TreeNode, so at
any time you can print the root node to see a basic representation of
the tree.

This challenge and variations of it were reported to have been asked at
interviews with Google. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.

https://www.codecademy.com/code-challenges/code-challenge-balanced-binary-search-tree-python
"""


class TreeNode():
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def __str__(self):
        return f"{self.value}->{self.left}\n{self.value}->{self.right}"


def main():
    a = [1, 2, 3, 4, 5, 6, 7]
    balanced_node = balanced_bst(a)
    print(balanced_node)


def balanced_bst(a):
    # Write your code here
    n = len(a)
    if n < 1:
        return None

    middle = n//2
    tree = TreeNode(a[middle])
    tree.left = balanced_bst(a[:middle])
    tree.right = balanced_bst(a[middle + 1:])

    return tree


if __name__ == '__main__':
    main()
