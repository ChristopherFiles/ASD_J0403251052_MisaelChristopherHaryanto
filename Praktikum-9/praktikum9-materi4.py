#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 4 : Membuat trasversal In order
#====================================

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

def inorder(node):
    if node:
        inorder(node.left) # Kunjungi subtree kiri
        print(node.data) # Kunjungi node
        inorder(node.right) # Kunjungi subtree kanan
    
# membuat Root
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")
# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# menjalankan traversal inorder
print("Traversal Inorder:")
inorder(root)

# Penjelasan:
"""

Traversal inorder mengunjungi subtree kiri terlebih dahulu, kemudian node itu sendiri, dan terakhir subtree kanan. Dalam contoh pohon biner ini, traversal inorder akan mencetak nama-nama node dalam urutan berikut:
1. D (karena ini adalah leaf node paling kiri)
2. B (karena ini adalah child kiri dari root)
3. E (karena ini adalah child kanan dari B)
4. A (karena ini adalah root)
5. C (karena ini adalah child kanan dari root)

Traversal inorder sangat berguna untuk mencetak nilai-nilai dalam urutan yang terurut (jika pohon biner pencarian), karena ia mengunjungi node dalam urutan yang memenuhi sifat BST (Binary Search Tree).

"""