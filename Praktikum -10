#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 1 : BST
#====================================

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None


def insert(root, data):
    if root is None:
        return Node(data) # Jika root kosong, buat node baru
    if data < root.data:
        root.left = insert(root.left, data) # Sisipkan ke subtree kiri
    else:
        root.right = insert(root.right, data) # Sisipkan ke subtree kanan
    return root

# Membuat BST dan menyisipkan data
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]
for data in data_list:
    root = insert(root, data)

#=======================================================
# Latihan 2 : Inorder Traversal
#=======================================================

def inorder(node):
    if node:
        inorder(node.left) # Kunjungi subtree kiri
        print(node.data) # Kunjungi node
        inorder(node.right) # Kunjungi subtree kanan
# Menampilkan hasil inorder traversal
print("Inorder Traversal of BST:")
inorder(root)

#=======================================================
# Latihan 3 : Search dalam BST
#=======================================================

def search(node, key):
    if node is None or node.data == key:
        return node # Kembalikan node jika ditemukan atau jika mencapai leaf
    if key < node.data:
        return search(node.left, key) # Cari di subtree kiri
    else:
        return search(node.right, key) # Cari di subtree kanan
    
# Mencari nilai dalam BST
key_to_search = 40
result = search(root, key_to_search)
if result:
    print(f"Data {key_to_search} ditemukan dalam BST.")
else:    print(f"Data {key_to_search} tidak ditemukan dalam BST.")

# Penjelasannya :
"""
BST (Binary Search Tree) adalah struktur data pohon biner yang
di mana setiap node memiliki nilai yang lebih besar dari 
semua nilai di subtree kiri dan lebih kecil dari semua nilai di subtree kanan. 
"""