#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 5 : Membuat Postorder
#====================================


class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

def postorder(node):
    if node:
        postorder(node.left) # Kunjungi subtree kiri
        postorder(node.right) # Kunjungi subtree kanan
        print(node.data) # Kunjungi node

# membuat Root
root = Node("A")
# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# menjalankan traversal postorder
print("Traversal Postorder:")
postorder(root)