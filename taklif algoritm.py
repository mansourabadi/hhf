class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def build_tree(numbers):
    root = None
    for number in numbers:
        root = insert(root, number)
    return root

numbers = []
for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

root = build_tree(numbers)
print("Inorder traversal of the binary tree:")
inorder_traversal(root)
