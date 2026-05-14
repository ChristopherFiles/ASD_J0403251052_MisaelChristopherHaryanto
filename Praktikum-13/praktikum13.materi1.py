# ========================================================== 
# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1
# Implementasi Kruskal 
# ========================================================== 

# Daftar seluruh sisi (edge) pada graf dengan format: (bobot, node_asal, node_tujuan)
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 
 
# Mengurutkan semua sisi dari bobot terkecil ke terbesar (Syarat utama algoritma Kruskal)
edges.sort() 
 
# List untuk menampung sisi-sisi yang terpilih menjadi bagian dari Minimum Spanning Tree (MST)
mst = [] 

# Variabel untuk menghitung akumulasi total bobot dari MST yang terbentuk
total_weight = 0 
 
# Set untuk mencatat node mana saja yang sudah terhubung atau pernah dikunjungi
connected = set() 
 
# Melakukan perulangan untuk memeriksa setiap sisi graf yang sudah diurutkan
for weight, u, v in edges: 
 
    # Cek apakah salah satu atau kedua node (u atau v) belum pernah dikunjungi sebelumnya.
    # Logika ini digunakan sebagai deteksi sederhana agar tidak terjadi loop/cycle.
    if u not in connected or v not in connected: 
 
        # Jika aman (tidak membentuk cycle menurut logika ini), masukkan sisi ke dalam list MST
        mst.append((u, v, weight)) 
        
        # Tambahkan bobot sisi yang terpilih ke dalam total bobot MST
        total_weight += weight 
 
        # Masukkan kedua node (u dan v) ke dalam set connected sebagai tanda sudah dikunjungi
        connected.add(u) 
        connected.add(v) 
 
# Menampilkan teks judul output
print("Minimum Spanning Tree:") 
 
# Menampilkan daftar sisi yang terpilih masuk ke dalam MST satu per satu
for edge in mst: 
    print(edge) 
 
# Menampilkan hasil akhir total bobot dari seluruh sisi MST yang terbentuk
print("Total bobot =", total_weight)
