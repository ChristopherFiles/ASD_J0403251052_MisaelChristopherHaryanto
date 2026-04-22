#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 4 : membuat BST Tidak seimbang
#====================================

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None


# Membuat BST tidak seimbang dengan menyisipkan data dalam urutan menaik
def insert(root, data):
    if root is None:
        return Node(data) # Jika root kosong, buat node baru
    if data < root.data:
        root.left = insert(root.left, data) # Sisipkan ke subtree kiri
    else:
        root.right = insert(root.right, data) # Sisipkan ke subtree kanan
    return root

# Membuat BST tidak seimbang


# Menampilkan hasil inorder traversal untuk melihat struktur BST
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


#============================
# Program Utama
#============================

root = None
data_list = [10, 20, 30, 40, 50] # Data disisipkan dalam urutan menaik

for data in data_list:
    root = insert(root, data)

print("Preorder Traversal of Unbalanced BST:")
preorder(root)

print("\nStruktur BST Tidak Seimbang:")
tampil_struktur(root)

#Penjelasan alurnya :
# 1. Kita membuat kelas Node untuk merepresentasikan setiap node dalam BST, dengan atribut data, left, dan right.
# 2. Fungsi insert digunakan untuk menyisipkan data ke dalam BST. Karena data
#   disisipkan dalam urutan menaik, setiap data baru akan menjadi child kanan dari node sebelumnya, sehingga menghasilkan BST yang tidak seimbang.
# 3. Fungsi preorder digunakan untuk melakukan traversal preorder pada BST, yang mencetak data dari setiap node dalam urutan root, left, right.
# 4. Fungsi tampil_struktur digunakan untuk menampilkan struktur BST secara visual, dengan indentasi yang menunjukkan level dari setiap node.
# 5. Dalam program utama, kita menyisipkan data ke dalam BST dan kemudian menampilkan hasil preorder traversal serta struktur BST yang tidak seimbang.
