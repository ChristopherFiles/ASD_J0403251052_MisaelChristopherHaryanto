# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Modul heapq digunakan untuk menjalankan priority queue.

# Graph lokasi kampus.
# Bobot menunjukkan perkiraan waktu tempuh dalam menit.
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # Dari Gerbang bisa ke Perpustakaan atau Kantin.
    'Perpustakaan': {'Lab': 3},                   # Dari Perpustakaan bisa menuju Lab.
    'Kantin': {'Lab': 4, 'Aula': 7},              # Dari Kantin bisa menuju Lab atau Aula.
    'Lab': {'Aula': 1},                           # Dari Lab bisa menuju Aula.
    'Aula': {}                                    # Aula adalah lokasi akhir tanpa edge keluar.
}


def dijkstra(graph, start):
    """Menghitung waktu tempuh terpendek dari start ke semua lokasi."""

    # Semua lokasi diberi jarak awal tak hingga.
    distances = {node: float('inf') for node in graph}

    # Waktu tempuh dari lokasi awal ke dirinya sendiri adalah 0 menit.
    distances[start] = 0

    # Priority queue berisi pasangan (waktu_tempuh, lokasi).
    priority_queue = [(0, start)]

    # Selama masih ada lokasi yang perlu diproses, perulangan terus berjalan.
    while priority_queue:
        # Mengambil lokasi dengan waktu tempuh paling kecil.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika data yang keluar dari queue sudah bukan jarak terbaik, lewati.
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua lokasi tetangga dari lokasi saat ini.
        for neighbor, weight in graph[current_node].items():
            # Menghitung waktu tempuh baru menuju neighbor.
            distance = current_distance + weight

            # Jika waktu baru lebih kecil, simpan sebagai waktu terpendek.
            if distance < distances[neighbor]:
                # Update jarak/waktu tempuh ke neighbor.
                distances[neighbor] = distance

                # Masukkan neighbor ke queue agar diproses berdasarkan waktu terkecil.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan semua waktu tempuh terpendek.
    return distances


# Menjalankan Dijkstra dari Gerbang Kampus.
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan waktu tempuh terpendek dari Gerbang ke setiap lokasi.
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalurnya adalah Gerbang -> Kantin -> Lab -> Aula dengan total 2 + 4 + 1 = 7.
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil. Contohnya,
#    dari Gerbang ke Aula melalui Kantin langsung bernilai 2 + 7 = 9,
#    sedangkan melalui Kantin -> Lab -> Aula bernilai 2 + 4 + 1 = 7.
# 4. Dijkstra cocok untuk kasus lokasi kampus ini karena semua bobot berupa waktu
#    tempuh bernilai positif, sehingga asumsi greedy Dijkstra tetap valid.
