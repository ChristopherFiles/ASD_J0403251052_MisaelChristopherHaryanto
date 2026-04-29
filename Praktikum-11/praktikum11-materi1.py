#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Implementasi dasar Graph
#====================================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D',],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

for node in graph:
    print(node, "->", graph[node])