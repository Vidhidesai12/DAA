# Vidhi Desai
# 1002081553
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.left_child = None
        self.right_child = None

class MyAVLTree:
    def __init__(self):
        self.root_node = None

    def insert_value(self, val):
        self.root_node = self._insert_recursive(self.root_node, val)

    def _insert_recursive(self, node, val):
        if not node:
            return AVLNode(val)
        elif val < node.val:
            node.left_child = self._insert_recursive(node.left_child, val)
        else:
            node.right_child = self._insert_recursive(node.right_child, val)

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))

        balance = self._get_balance(node)

        if balance > 1:
            if val < node.left_child.val:
                return self._right_rotate(node)
            else:
                node.left_child = self._left_rotate(node.left_child)
                return self._right_rotate(node)
        if balance < -1:
            if val > node.right_child.val:
                return self._left_rotate(node)
            else:
                node.right_child = self._right_rotate(node.right_child)
                return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))

        return y

    def _right_rotate(self, z):
        y = z.left_child
        T3 = y.right_child

        y.right_child = z
        z.left_child = T3

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root_node)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left_child)
            result.append(node.val)
            result += self._inorder_traversal_recursive(node.right_child)
        return result

# Test the AVL Tree
my_avl = MyAVLTree()
my_avl.insert_value(5)
my_avl.insert_value(3)
my_avl.insert_value(7)
my_avl.insert_value(2)
my_avl.insert_value(4)
my_avl.insert_value(6)
my_avl.insert_value(8)
print("AVL Tree Inorder Traversal:", my_avl.inorder_traversal())  # Should print [2, 3, 4, 5, 6, 7, 8]
