class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def sumOfValues(node):
    if node is None:
        return 0
    return node.val + sumOfValues(node.left) + sumOfValues(node.right)

# Створення прикладу BST
root = Node(10)
insert(root, 5)
insert(root, 15)
insert(root, 2)
insert(root, 5)  
insert(root, 13)
insert(root, 22)
insert(root, 1)

# Обчислення суми всіх значень
total_sum = sumOfValues(root)
print("Сума всіх значень у дереві:", total_sum)
