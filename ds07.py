class TreeNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

def count_leaves(root):
    if root is None:
        return 0
    if root.Lchild is None and root.Rchild is None:
        return 1
    return count_leaves(root.Lchild) + count_leaves(root.Rchild)

def count_1deg(root):
    if root is None:
        return 0
    count = 0
    if (root.Lchild is None) != (root.Rchild is None):
        count = 1
    return count + count_1deg(root.Lchild) + count_1deg(root.Rchild)

def count_2deg(root):
    if root is None:
        return 0
    count = 0
    if root.Lchild and root.Rchild:
        count = 1
    return count + count_2deg(root.Lchild) + count_2deg(root.Rchild)

def sum_tree(root):
    if root is None:
        return 0
    return root.data + sum_tree(root.Lchild) + sum_tree(root.Rchild)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.Lchild) + count_nodes(root.Rchild)

def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.Lchild)
    preorder(root.Rchild)

def search(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return search(root.Lchild, target) or search(root.Rchild, target)

def max_tree(root):
    if root is None:
        return float("-inf")
    return max(root.data, max_tree(root.Lchild), max_tree(root.Rchild))
