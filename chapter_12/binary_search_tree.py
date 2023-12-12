from typing import List, Union, Any, Optional
from unittest import TestCase
import unittest


class Node:
    def __init__(
        self,
        value: Union[str, int],
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        parent: Optional["Node"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def inorder_tree_walk(x: Node) -> None:
    """Prints the values of the nodes in a binary search tree in sorted order."""
    if x.value is not None:
        inorder_tree_walk(x.left)
        print(x.value)
        inorder_tree_walk(x.right)


def preorder_tree_walk(x: Node) -> None:
    """Prints the values of the nodes in a binary search tree in sorted order."""
    if x.value is not None:
        print(x.value)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)


def postorder_tree_walk(x: Node) -> None:
    """Prints the values of the nodes in a binary search tree in sorted order."""
    if x.value is not None:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.value)


def tree_search(x: Node, k: int) -> Optional[Node]:
    """Searches for a value in a binary search tree and returns the node with
    that value."""
    if x is None or k == x.value:
        return x
    if k < x.value:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x: Node, k: int) -> Optional[Node]:
    """Searches for a value in a binary search tree and returns the node with
    that value."""
    while x is not None and k != x.value:
        if k < x.value:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x: Node) -> Node:
    """Returns the node with the minimum value in a binary search tree."""
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x: Node) -> Node:
    """Returns the node with the maximum value in a binary search tree."""
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x: Node) -> Optional[Node]:
    """Returns the node with the next largest value in a binary search tree.

    The successor of a node x is the node with the smallest key greater than
    x.key. If x has a right child, then its successor is just the leftmost node
    in the right subtree of x. Otherwise, it is the lowest ancestor of x whose
    left child is also an ancestor of x.

    """
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


def tree_insert(T: Node, z: Node) -> None:
    """Inserts a node into a binary search tree."""
    y = None
    x = T
    while x is not None:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        T = z
    elif z.value < y.value:
        y.left = z
    else:
        y.right = z

    return T


def transplant(T: Node, u: Node, v: Node) -> None:
    """Replaces one subtree as a child of its parent with another subtree.
    u then becomes detached from the tree."""
    if u.parent is None:
        T = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent
    return T


def tree_delete(T: Node, z: Node) -> None:
    """Deletes a node from a binary search tree."""
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y

    return T


class TestBinarySearchTree(unittest.TestCase):
    def run_all_tests(self):
        self.setUp()
        self.test_tree_minimum()
        self.test_tree_maximum()
        self.test_tree_search()
        self.test_iterative_tree_search()
        self.test_tree_successor()
        self.test_tree_insert()
        self.test_tree_delete()

    def setUp(self):
        # Set up a sample binary search tree
        self.root = Node(15)
        self.root.left = Node(6, parent=self.root)
        self.root.right = Node(18, parent=self.root)
        self.root.left.left = Node(3, parent=self.root.left)
        self.root.left.right = Node(7, parent=self.root.left)
        self.root.right.left = Node(17, parent=self.root.right)
        self.root.right.right = Node(20, parent=self.root.right)

    def test_tree_minimum(self):
        self.assertEqual(tree_minimum(self.root).value, 3)

    def test_tree_maximum(self):
        self.assertEqual(tree_maximum(self.root).value, 20)

    def test_tree_search(self):
        self.assertEqual(tree_search(self.root, 7).value, 7)
        self.assertIsNone(tree_search(self.root, 99))

    def test_iterative_tree_search(self):
        self.assertEqual(iterative_tree_search(self.root, 7).value, 7)
        self.assertIsNone(iterative_tree_search(self.root, 99))

    def test_tree_successor(self):
        node = tree_search(self.root, 6)
        self.assertEqual(tree_successor(node).value, 7)

    def test_tree_insert(self):
        new_node = Node(10)
        tree_insert(self.root, new_node)
        self.assertEqual(self.root.left.right.right.value, 10)

    def test_tree_delete(self):
        node_to_delete = tree_search(self.root, 6)
        tree_delete(self.root, node_to_delete)
        self.assertIsNone(tree_search(self.root, 6))

    # Additional tests can be written for transplant, inorder, preorder, and postorder walks


if __name__ == "__main__":
    # unittest.main(argv=["first-arg-is-ignored"], exit=False)
    TestBinarySearchTree().run_all_tests()

    root = Node(15)
    for i in [6, 18, 3, 7, 17, 20]:
        tree_insert(root, Node(i))

    inorder_tree_walk(root)
