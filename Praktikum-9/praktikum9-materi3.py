#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 3 : Membuat Preorder
#====================================

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

def preorder(node):
    if node:
        print(node.data) # Kunjungi node
        preorder(node.left) # Kunjungi subtree kiri
        preorder(node.right) # Kunjungi subtree kanan

# membuat Root
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")


# menjalankan traversal preorder
print("Traversal Preorder:")
preorder(root)

# Penjelasan:
"""
Traversal preorder mengunjungi node itu sendiri terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan. Dalam contoh pohon biner ini, traversal preorder akan mencetak nama-nama node dalam urutan berikut:
1. A (karena ini adalah root)
2. B (karena ini adalah child kiri dari root)
3. D (karena ini adalah child kiri dari B)
4. E (karena ini adalah child kanan dari B)
5. C (karena ini adalah child kanan dari root)
Traversal preorder sangat berguna untuk mencetak struktur pohon dalam urutan hierarki, dimulai dari node root hingga ke daun-daun (leaf nodes).
"""