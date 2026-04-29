#====================================
# Nama : Misael Christopher Haryanto
# NIM : J0403251052
# KELAS : TPL B1
#====================================

#====================================
# Latihan 1 : Study kasus BFS
#====================================

from collections import deque

graph = {
    'Rumah' : ['Sekolah', 'Toko'],
    'Sekolah' : ['Perpustakaan'],
    'Toko' : ['Pasar'],
    'Perpustakaan' : [],
    'Pasar' : []
}

def bfs(graph, start):
    visited = set() # Set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start]) # Queue untuk BFS, mulai dengan node awal

    visited.add(start) # Tandai node awal sebagai sudah dikunjungi
    while queue:
        node = queue.popleft() # Ambil node dari depan queue
        print(node) # Kunjungi node
        # Tambahkan semua tetangga yang belum dikunjungi ke dalam queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor) # Tandai tetangga sebagai sudah dikunjungi
                queue.append(neighbor) # Tambahkan tetangga ke dalam queue

print("BFS Traversal of the Graph:")
bfs(graph, 'Rumah') # Memulai BFS dari node 'Rumah'

"""
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
2. Mengapa BFS cocok untuk mencari jalur terdekat?  
3. Apa perbedaan urutan BFS jika struktur graph diubah? 

Jawaban Analisis
1. Node yang dikunjungi pertama adalah 'Rumah', karena BFS memulai penelusuran dari node awal yang diberikan.
2. BFS sangat cocok untuk mencari jalur terdekat pada graf tanpa bobot karena algoritma ini menjelajahi graf lapis demi lapis sehingga node yang pertama kali ditemukan dijamin memiliki jumlah lompatan paling sedikit dari titik awal.
3. Jika struktur graf diubah, urutan kunjungan BFS otomatis berubah karena keterhubungan dan kedalaman level antar node yang menjadi prioritas antrean ikut bergeser.