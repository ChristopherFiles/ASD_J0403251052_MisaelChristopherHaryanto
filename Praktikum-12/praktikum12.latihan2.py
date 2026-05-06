# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq  # Modul heapq digunakan untuk membuat priority queue.

# Weighted graph dengan semua bobot bernilai positif.
# Dijkstra cocok digunakan pada graph seperti ini.
graph = {
    'A': {'B': 4, 'C': 2},  # A memiliki edge ke B berbobot 4 dan ke C berbobot 2.
    'B': {'D': 5},          # B memiliki edge ke D berbobot 5.
    'C': {'D': 1},          # C memiliki edge ke D berbobot 1.
    'D': {}                 # D tidak memiliki edge keluar.
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga karena belum ada jalur yang diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node).
    # Node dengan jarak paling kecil akan diproses lebih dahulu.
    priority_queue = [(0, start)]

    # Perulangan berjalan selama masih ada node di priority queue.
    while priority_queue:
        # Mengambil node dengan jarak terkecil saat ini.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang keluar dari queue lebih besar dari data terbaik,
        # maka node ini dilewati karena sudah ada jarak yang lebih kecil.
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga dari node saat ini.
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru dari start menuju neighbor melalui current_node.
            distance = current_distance + weight

            # Jika jarak baru lebih kecil dari jarak lama, lakukan update.
            if distance < distances[neighbor]:
                # Menyimpan jarak yang lebih kecil ke dictionary distances.
                distances[neighbor] = distance

                # Memasukkan neighbor ke priority queue untuk diproses berikutnya.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan semua jarak terpendek dari node start.
    return distances


# Menjalankan fungsi Dijkstra dari node awal A.
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak terpendek dari node A.
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
# 4. Jarak A ke D lebih kecil melalui C karena A -> C -> D = 2 + 1 = 3,
#    sedangkan melalui B yaitu A -> B -> D = 4 + 5 = 9.
# 5. priority_queue berfungsi menyimpan node yang akan diproses berdasarkan
#    jarak sementara terkecil, sehingga Dijkstra selalu memilih node paling dekat.
# 6. Dijkstra tidak cocok untuk graph berbobot negatif karena algoritma ini
#    bersifat greedy dan menganggap node dengan jarak terkecil yang sudah dipilih
#    tidak akan menjadi lebih kecil lagi. Edge negatif dapat membatalkan asumsi itu.
