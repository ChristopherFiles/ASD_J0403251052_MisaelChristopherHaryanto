#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 1 : Membuat Node
#====================================

#Class Node digunakan untuk dasar dari Tree




class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# membuat Root
root = Node("A")

#menampilkan isi node root
print("Data pada root:", root.data)
print("Child kiri root:", root.left)
print("Child kanan root:", root.right)

# Pembahasan : ....................................................................................
# Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right.