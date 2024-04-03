# Vidhi Desai
# 1002081553
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

class MyBinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert_value(self, val):
        if not self.root_node:
            self.root_node = TreeNode(val)
        else:
            self._insert_recursive(self.root_node, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left_child is None:
                node.left_child = TreeNode(val)
            else:
                self._insert_recursive(node.left_child, val)
        elif val > node.val:
            if node.right_child is None:
                node.right_child = TreeNode(val)
            else:
                self._insert_recursive(node.right_child, val)

    def search_value(self, val):
        return self._search_recursive(self.root_node, val)

    def _search_recursive(self, node, val):
        if node is None or node.val == val:
            return node
        elif val < node.val:
            return self._search_recursive(node.left_child, val)
        else:
            return self._search_recursive(node.right_child, val)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root_node)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left_child)
            result.append(node.val)
            result += self._inorder_traversal_recursive(node.right_child)
        return result

# Test the Binary Search Tree
my_bst = MyBinarySearchTree()
my_bst.insert_value(5)
my_bst.insert_value(3)
my_bst.insert_value(7)
my_bst.insert_value(2)
my_bst.insert_value(4)
my_bst.insert_value(6)
my_bst.insert_value(8)
print("Inorder Traversal:", my_bst.inorder_traversal())  # Should print [2, 3, 4, 5, 6, 7, 8]
print("Search 4:", my_bst.search_value(4).val)  # Should print 4