class Node:
  def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def isBST(root, prev):
    if root is None:
        return True
    left = isBST(root.left, prev)
    if root.data <= prev.data:
        return False
    prev.data = root.data
    return left and isBST(root.right, prev)
def checkForBST(node):
    prev = Node(float('-inf'))
    if isBST(node, prev):
        print("This is a BST!")
    else:
        print("This is NOT a BST!")
def swap(root):
    left = root.left
    root.left = root.right
    root.right = left
if __name__ == '__main__':
    root = None
    keys = [15, 10, 20, 8, 12, 16, 25]
    for key in keys:
        root = insert(root, key)
    swap(root)
    checkForBST(root)