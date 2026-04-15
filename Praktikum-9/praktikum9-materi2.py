#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 2 : Membuat Child level 1
#====================================

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# membuat Root
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")


# menampilkan isi node
print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari node B:", root.left.left)
print("Child kanan dari node B:", root.left.right)

# Penjelasan: 
"""
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Kemudian kita membuat sebuah node root dengan data "A" dan menambahkan dua child yaitu "B" sebagai child kiri dan "C" sebagai child kanan
. Saat kita menampilkan isi node, kita dapat melihat data pada root dan child-childnya. Child kiri dari node B adalah None karena kita belum menambahkan child untuk node B, begitu juga dengan child kanan dari node B.
"""