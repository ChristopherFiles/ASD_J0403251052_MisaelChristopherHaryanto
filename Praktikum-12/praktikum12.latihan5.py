# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Program Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Mengimpor heapq untuk mengelola priority queue.

# Graph berbobot antar kota sesuai instruksi soal.
# Bobot pada edge menyatakan jarak/biaya perjalanan antar kota.
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},      # Bogor terhubung ke Jakarta dan Depok.
    'Jakarta': {'Bandung': 7},                # Jakarta terhubung ke Bandung.
    'Depok': {'Jakarta': 2, 'Bandung': 6},    # Depok terhubung ke Jakarta dan Bandung.
    'Bandung': {}                             # Bandung tidak memiliki edge keluar pada kasus ini.
}


def dijkstra(graph, start):
    """Menghitung jarak terpendek dari kota start ke semua kota lain."""

    # Membuat dictionary jarak awal untuk semua kota.
    distances = {node: float('inf') for node in graph}

    # Jarak kota awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan data (jarak_sementara, nama_kota).
    priority_queue = [(0, start)]

    # Memproses queue sampai semua kandidat jalur selesai diperiksa.
    while priority_queue:
        # Mengambil kota dengan jarak sementara paling kecil.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak ini lebih besar dari jarak terbaik yang tersimpan,
        # maka data ini dilewati karena sudah tidak relevan.
        if current_distance > distances[current_node]:
            continue

        # Mengecek semua kota tujuan yang terhubung dari current_node.
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru menuju neighbor melalui current_node.
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update jarak terpendek menuju neighbor.
            if distance < distances[neighbor]:
                # Menyimpan nilai jarak terbaru.
                distances[neighbor] = distance

                # Memasukkan neighbor ke priority queue untuk diproses berikutnya.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan semua jarak terpendek dari start.
    return distances


# Node awal ditentukan langsung dalam program sesuai instruksi soal.
node_awal = 'Bogor'

# Menjalankan algoritma Dijkstra dari Bogor.
hasil = dijkstra(graph, node_awal)

# Menampilkan output jarak terpendek dari Bogor ke semua kota.
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(node_awal, "->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node dengan jarak paling kecil dari Bogor selain Bogor sendiri adalah Depok,
#    karena jaraknya 2.
# 3. Node dengan jarak paling besar dari Bogor adalah Bandung, karena jarak terpendeknya 8.
# 4. Dijkstra bekerja dengan memilih kota yang memiliki jarak sementara paling kecil.
#    Dari Bogor, jarak awal ke Jakarta adalah 5 dan ke Depok adalah 2, sehingga Depok
#    diproses lebih dulu. Dari Depok, jarak ke Jakarta menjadi 2 + 2 = 4, lebih kecil
#    daripada jalur langsung Bogor -> Jakarta = 5. Dari Depok juga ditemukan jarak
#    ke Bandung sebesar 2 + 6 = 8. Setelah semua kandidat diproses, hasil akhirnya
#    adalah Bogor = 0, Jakarta = 4, Depok = 2, dan Bandung = 8.
