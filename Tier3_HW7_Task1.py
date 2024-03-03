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

def findMaxValue(node):
    current = node
    # Переміщуємося до найправішого вузла
    while(current.right is not None):
        current = current.right
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
print("Найбільше значення в дереві:", findMaxValue(root))
