#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Implementasi BFS
#====================================
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = set() # Set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start]) # Queue untuk BFS, mulai dengan node awal

    while queue:
        node = queue.popleft() # Ambil node dari depan queue
        if node not in visited:
            print(node) # Kunjungi node
            visited.add(node) # Tandai node sebagai sudah dikunjungi
            # Tambahkan semua tetangga yang belum dikunjungi ke dalam queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("BFS Traversal of the Graph:")
bfs(graph, 'A') # Memulai BFS dari node 'A'