from typing import Union, Any, Optional
import unittest

from chapter_12.binary_search_tree import inorder_tree_walk


class Node:
    def __init__(self, value, color="RED", nil: Optional["Node"] = None):
        self.value = value
        self.color = color
        self.parent: Optional[Node] = None if not nil else nil
        self.left: Optional[Node] = None if not nil else nil
        self.right: Optional[Node] = None if not nil else nil


class RedBlackTree:
    def __init__(self):
        self.nil: Node = Node(None, "BLACK")
        self.root: Node = self.nil
        self.root.left = self.nil
        self.root.right = self.nil

    def insert(self, value: Union[str, int]) -> None:
        z = Node(value)
        self.rb_insert(z)

    def search(self, value: Union[str, int]) -> Optional[Node]:
        node = self.root
        while node and node != self.nil and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def left_rotate(self, node: Node) -> None:
        left_rotate(node)
        if node.parent is self.nil:
            self.root = node
        elif node.parent.parent is self.nil:
            self.root = node.parent

    def right_rotate(self, node: Node) -> None:
        right_rotate(node)
        if node.parent is self.nil:
            self.root = node
        elif node.parent.parent is self.nil:
            self.root = node.parent

    def rb_insert(self, z: Node) -> None:
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is self.nil:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "RED"
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, node: Node) -> None:
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y is not None and y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y is not None and y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        self.root.color = "BLACK"


def left_rotate(node: Node) -> None:
    """Left rotates a node in a Red-Black Tree.

    Args
    ----

    node: Node
        The node to be rotated. This node's right child will become the new
        parent.

    Returns None
    """
    y: Node = node.right
    node.right = y.left
    if y.left is not None:
        y.left.parent = node
    y.parent = node.parent
    if node.parent is None:
        node.parent = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.left = node
    node.parent = y


def right_rotate(node: Node) -> None:
    y: Node = node.left
    node.left = y.right
    if y.right is not None:
        y.right.parent = node
    y.parent = node.parent
    if node.parent is None:
        node.parent = y
    elif node == node.parent.right:
        node.parent.right = y
    else:
        node.parent.left = y
    y.right = node
    node.parent = y


def rb_insert_fixup(T: RedBlackTree, node: Node) -> None:
    while node.parent is not None and node.parent.color == "RED":
        if node.parent == node.parent.parent.left:
            y = node.parent.parent.right
            if y is not None and y.color == "RED":
                node.parent.color = "BLACK"
                y.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent
                    left_rotate(node)
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                right_rotate(node.parent.parent)
        else:
            y = node.parent.parent.left
            if y is not None and y.color == "RED":
                node.parent.color = "BLACK"
                y.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    right_rotate(node)
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                left_rotate(node.parent.parent)
    T.root.color = "BLACK"


def rb_insert(T: RedBlackTree, z: Node) -> None:
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is T.nil:
        T.root = z
    elif z.value < y.value:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = "RED"
    rb_insert_fixup(T, z)


class TestRedBlackTree(unittest.TestCase):
    def run_all_tests(self):
        self.setUp()
        self.test_search()
        self.test_left_rotate()
        self.test_right_rotate()
        self.test_rb_insert_fixup()
        self.test_insert_sequence_1()

    def setUp(self):
        # Set up a basic Red-Black Tree
        self.tree = RedBlackTree()
        self.node_20 = Node(20, nil=self.tree.nil)
        self.node_10 = Node(10, nil=self.tree.nil)
        self.node_30 = Node(30, nil=self.tree.nil)

        # Manually create a small Red-Black Tree
        self.tree.root = self.node_20
        self.node_20.left = self.node_10
        self.node_20.right = self.node_30
        self.node_10.parent = self.node_20
        self.node_30.parent = self.node_20

    def test_insert(self):
        self.tree.insert(40)
        self.assertEqual(self.tree.root.right.right.value, 40)
        self.assertEqual(self.tree.root.right.right.color, "RED")

    def test_search(self):
        self.assertEqual(self.tree.search(10), self.node_10)
        self.assertEqual(self.tree.search(20), self.node_20)
        self.assertEqual(self.tree.search(30), self.node_30)
        self.assertEqual(self.tree.search(40), self.tree.nil)

    def test_left_rotate(self):
        self.setUp()
        self.tree.left_rotate(self.node_20)
        self.assertEqual(self.tree.root, self.node_30)
        self.assertEqual(self.node_20.right, self.tree.nil)
        self.assertEqual(self.node_20.left, self.node_10)
        self.assertEqual(self.node_30.left, self.node_20)

    def test_right_rotate(self):
        self.setUp()
        self.tree.right_rotate(self.node_20)
        self.assertEqual(self.tree.root, self.node_10)
        self.assertEqual(self.node_20.right, self.node_30)
        self.assertEqual(self.node_20.left, self.tree.nil)

    def test_insert_sequence_1(self):
        """Testing that the example from 13.3.2 works as expected, with the nodes being
        properly colored and rotated."""
        tree = RedBlackTree()
        for i in [41, 38, 31, 12, 19, 8]:
            tree.insert(i)

        inorder_tree_walk(tree.root)

        # Verify the tree's properties after insertion
        self.assertEqual(tree.root.value, 38)
        self.assertEqual(tree.root.color, "BLACK")
        self.assertEqual(tree.root.left.value, 19)
        self.assertEqual(tree.root.left.color, "RED")
        self.assertEqual(tree.root.right.value, 41)
        self.assertEqual(tree.root.right.color, "BLACK")
        self.assertEqual(tree.root.left.left.value, 12)
        self.assertEqual(tree.root.left.left.color, "BLACK")
        self.assertEqual(tree.root.left.right.value, 31)
        self.assertEqual(tree.root.left.right.color, "BLACK")
        self.assertEqual(tree.root.left.left.left.value, 8)
        self.assertEqual(tree.root.left.left.left.color, "RED")


if __name__ == "__main__":
    TestRedBlackTree().run_all_tests()
