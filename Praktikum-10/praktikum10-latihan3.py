#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 5 : Rotasi Kiri pada BST tidak seimbang
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


def rotate_left(root):
    new_root = root.right # Node baru menjadi child kanan dari root
    root.right = new_root.left # Subtree kiri dari new_root menjadi child kanan dari root
    new_root.left = root # Root menjadi child kiri dari new_root
    return new_root # Kembalikan new_root sebagai root baru

#============================
# Program Utama
#============================

# Membuat BST tidak seimbang
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder Traversal of Unbalanced BST:")
preorder(root)

print("\nStruktur BST Tidak Seimbang:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)
print("\nPreorder Traversal after Left Rotation:")
preorder(root)
print("\nStruktur BST Setelah Rotasi Kiri:")
tampil_struktur(root)

#Penjelasan Alurnya:
"""
1. BST dibuat tidak seimbang: 10 -> 20 -> 30 (semua ke kanan).
2. Traversal dan struktur ditampilkan sebelum rotasi.
3. Rotasi kiri pada 10 membuat 20 jadi root, 10 di kiri, 30 di kanan.
4. Traversal dan struktur ditampilkan lagi setelah rotasi.
Rotasi kiri membantu menyeimbangkan BST saat sisi kanan terlalu tinggi.


"""