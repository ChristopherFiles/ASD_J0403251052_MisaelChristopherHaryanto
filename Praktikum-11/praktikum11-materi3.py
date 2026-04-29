#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Implementasi DFS
#====================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, start, visited=None):
    #fungsi untuk melakukan penelusuran graph menggunakan dfs
    #graph :  dicionary yang menyimpan graph
    #node : menyimpan node yang akan dikunjungi
    #visited : set untuk menyimpan node yang sudah dikunjungi
    if visited is None:
        visited = set() # Set untuk menyimpan node yang sudah dikunjungi
    visited.add(start) # Tandai node saat ini sebagai sudah dikunjungi
    print(start) # Kunjungi node
    for neighbor in graph[start]: # Kunjungi semua tetangga
        if neighbor not in visited:
            dfs(graph, neighbor, visited) # Rekursi untuk tetangga yang belum dikunjungi


dfs(graph, 'A') # Memulai DFS dari node 'A'