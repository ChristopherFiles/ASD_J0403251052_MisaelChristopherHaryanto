#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 6 : Struktur Organisasi Perusahaan
#====================================
#Class Node digunakan untuk dasar dari Tree

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

# membuat tree struktur organisasi

root = Node("Direktur")

# level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff2")
root.right.right = Node("Staff3")

#menjalankan traversal preorder
print("Struktur Organisasi Perusahaan (Preorder Traversal):")
preorder(root)

# Penjelasannya :
"""
Traversal preorder mengunjungi node terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan. Dalam contoh struktur organisasi perusahaan, traversal preorder akan mencetak nama-nama posisi dalam urutan berikut:
1. Direktur (karena ini adalah node root)
2. Manajer A (karena ini adalah child kiri dari Direktur)
3. Staff 1 (karena ini adalah child kiri dari Manajer A)
4. Staff 2 (karena ini adalah child kanan dari Manajer A)
5. Manajer B (karena ini adalah child kanan dari Direktur)
6. Staff 3 (karena ini adalah child kanan dari Manajer B)

Traversal preorder sangat berguna untuk mencetak struktur organisasi karena kita ingin melihat posisi-posisi dalam urutan hierarki, dimulai dari posisi tertinggi (Direktur) hingga posisi yang lebih rendah (Staff).
"""