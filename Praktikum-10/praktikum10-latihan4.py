#====================================
# Nama : Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 6 : Rotasi Kanan pada BST tidak seimbang
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

def tampil_struktur(node, level=0, posisi='Root'):
    if node is not None:
        tampil_struktur(node.right, level + 1) # Tampilkan subtree kanan terlebih dahulu
        print(' ' * 4 * level + '-> ' + str(node.data)) # Tampilkan node dengan indentasi sesuai level
        tampil_struktur(node.left, level + 1) # Tampilkan subtree kiri

def rotate_right(root):
    new_root = root.left # Node baru menjadi child kiri dari root
    root.left = new_root.right # Subtree kanan dari new_root menjadi child kiri dari root
    new_root.right = root # Root menjadi child kanan dari new_root
    return new_root # Kembalikan new_root sebagai root baru

#============================
# Program Utama
#============================
# Membuat BST tidak seimbang
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)
print("Preorder Traversal of Unbalanced BST:")
preorder(root)

print("\nStruktur BST Tidak Seimbang:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)
print("\nPreorder Traversal after Right Rotation:")
preorder(root)

print("\nStruktur BST Setelah Rotasi Kanan:")
tampil_struktur(root)

# Penjelasan Alurnya:
"""
1. BST dibuat tidak seimbang: 30 -> 20 -> 10 (semua ke kiri).
2. Rotasi kanan dilakukan pada root (30), sehingga 20 menjadi root baru, 30 menjadi child kanan dari 20, dan 10 tetap menjadi child kiri dari 20.
3. Traversal dan struktur ditampilkan setelah rotasi untuk melihat perubahan pada BST.
"""