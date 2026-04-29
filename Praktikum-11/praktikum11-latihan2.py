#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 2 : Studi Kasus DFS
#====================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, start, visited):
    visited.add(start) # Tandai node saat ini sebagai sudah dikunjungi
    print(start, end=" ") # Kunjungi node

    for neighbor in graph[start]: # Kunjungi semua tetangga
        if neighbor not in visited:
            dfs(graph, neighbor, visited) # Rekursi untuk tetangga yang belum dikunjungi

visited = set() # Set untuk menyimpan node yang sudah dikunjungi

print("DFS Traversal of the Graph:")
dfs(graph, 'A', visited) # Memulai DFS dari node 'A'

"""
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

Jawaban Analisis
1. DFS masuk ke node terdalam terlebih dahulu karena menggunakan struktur data tumpukan atau rekursi yang selalu memprioritaskan penelusuran cabang baru yang ditemukan sebelum kembali ke cabang sebelumnya.
2. Jika urutan tetangga neighbor, urutan kunjungan node akan berubah secara drastis karena urutan pemrosesan antrean atau tumpukannya bergeser. Namun, cakupan akhir seluruh node yang terhubung tetap sama.
3. BFS menghasilkan jalur terpendek berdasarkan jumlah lompatan, sedangkan DFS menghasilkan jalur acak yang mendalam dan belum tentu merupakan rute terdekat.