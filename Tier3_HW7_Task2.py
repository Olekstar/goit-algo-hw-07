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

def findMinValue(node):
    current = node
    # Переміщуємося до найлівішого вузла
    while current.left is not None:
        current = current.left
    return current.val

# Створення прикладу BST
root = Node(10)
insert(root, 5)
insert(root, 15)
insert(root, 2)
insert(root, 5)
insert(root, 13)
insert(root, 22)
insert(root, 1)

# Пошук найбільшого значення
print("Найменше значення в дереві:", findMinValue(root))
