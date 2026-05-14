# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1

# Mengimpor modul heapq untuk menggunakan struktur data Min-Priority Queue (antrean prioritas)
import heapq 
 
# Representasi graf menggunakan Adjacency List (Daftar Ketetangan) berbobot
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 
 
# Fungsi untuk mencari Minimum Spanning Tree (MST) menggunakan Algoritma Prim
def prim(graph, start): 
 
    # Set untuk mencatat node yang sudah dikunjungi/dimasukkan ke dalam MST
    visited = set([start]) 
 
    # List kosong yang akan digunakan sebagai container Min-Heap untuk menyimpan sisi (edges)
    edges = [] 
 
    # Mengambil semua tetangga dari node awal dan memasukkannya ke dalam Min-Heap
    for neighbor, weight in graph[start].items(): 
        # Menyimpan dengan format (bobot, node_asal, node_tujuan) agar heap mengurutkan berdasarkan bobot terkecil
        heapq.heappush(edges, (weight, start, neighbor)) 
 
    # List untuk menyimpan daftar sisi yang terpilih menjadi bagian dari MST
    mst = [] 
    # Variabel untuk menghitung akumulasi total bobot dari MST
    total_weight = 0 
 
    # Melakukan perulangan selama masih ada sisi di dalam Min-Heap
    while edges: 
 
        # Mengambil (pop) sisi dengan bobot terkecil dari Min-Heap
        weight, u, v = heapq.heappop(edges) 
 
        # Memeriksa apakah node tujuan (v) belum pernah dikunjungi (untuk mencegah cycle)
        if v not in visited: 
 
            # Menandai node tujuan (v) sebagai node yang sudah dikunjungi
            visited.add(v) 
 
            # Memasukkan sisi yang lolos seleksi ke dalam list hasil MST
            mst.append((u, v, weight)) 
            # Menambahkan bobot sisi terpilih ke total bobot MST
            total_weight += weight 
 
            # Memeriksa semua tetangga dari node yang baru saja dikunjungi (v)
            for neighbor, w in graph[v].items(): 
 
                # Jika node tetangga tersebut belum dikunjungi, masukkan sisinya ke dalam Min-Heap
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    # Mengembalikan hasil berupa daftar sisi MST dan total bobotnya
    return mst, total_weight 
 
 
# Menjalankan fungsi Prim dengan memulai pencarian dari node 'A'
mst, total = prim(graph, 'A') 
 
# Menampilkan teks judul output
print("Minimum Spanning Tree:") 
 
# Menampilkan daftar sisi yang terpilih masuk ke dalam MST satu per satu
for edge in mst: 
    print(edge) 
 
# Menampilkan hasil akhir total bobot dari pohon merentang minimum yang terbentuk
print("Total bobot =", total)
