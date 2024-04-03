# Vidhi Desai
# 1002081553
class RedBlackTreeNode:
    def __init__(self, val, color="RED"):
        self.val = val
        self.color = color
        self.left_child = None
        self.right_child = None
        self.parent = None

class MyRedBlackTree:
    def __init__(self):
        self.root_node = None

    def insert_value(self, val):
        if not self.root_node:
            self.root_node = RedBlackTreeNode(val, color="BLACK")
        else:
            self._insert_recursive(self.root_node, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left_child is None:
                node.left_child = RedBlackTreeNode(val)
                node.left_child.parent = node
                self._fix_insertion(node.left_child)
            else:
                self._insert_recursive(node.left_child, val)
        elif val > node.val:
            if node.right_child is None:
                node.right_child = RedBlackTreeNode(val)
                node.right_child.parent = node
                self._fix_insertion(node.right_child)
            else:
                self._insert_recursive(node.right_child, val)

    def _fix_insertion(self, node):
        while node != self.root_node and node.parent.color == "RED":
            if node.parent == node.parent.parent.left_child:
                uncle = node.parent.parent.right_child
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left_child
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left_child:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
        self.root_node.color = "BLACK"

    def _left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child:
            y.left_child.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root_node = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left_child
        y.left_child = x.right_child
        if x.right_child:
            x.right_child.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root_node = x
        elif y == y.parent.right_child:
            y.parent.right_child = x
        else:
            y.parent.left_child = x
        x.right_child = y
        y.parent = x

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root_node)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left_child)
            result.append(node.val)
            result += self._inorder_traversal_recursive(node.right_child)
        return result

# Test the Red-Black Tree
my_rbt = MyRedBlackTree()
my_rbt.insert_value(5)
my_rbt.insert_value(3)
my_rbt.insert_value(7)
my_rbt.insert_value(2)
my_rbt.insert_value(4)
my_rbt.insert_value(6)
my_rbt.insert_value(8)
print("Red-Black Tree Inorder Traversal:", my_rbt.inorder_traversal())  # Should print [2, 3, 4, 5, 6, 7, 8]
