# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Materi 1: Implementasi Algoritma Dijkstra
# ==========================================================

import heapq  # Mengimpor modul heapq untuk membuat priority queue berbasis heap.

# Graph berbobot direpresentasikan dengan dictionary bersarang.
# Key pertama adalah node asal, key di dalamnya adalah node tujuan,
# sedangkan value-nya adalah bobot/jarak dari node asal ke node tujuan.
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B dengan bobot 4 dan ke C dengan bobot 2.
    'B': {'D': 5},          # Node B terhubung ke D dengan bobot 5.
    'C': {'D': 1},          # Node C terhubung ke D dengan bobot 1.
    'D': {}                 # Node D tidak memiliki tetangga keluar.
}


def dijkstra(graph, start):
    """Menghitung jarak terpendek dari node start ke semua node lain."""

    # Membuat dictionary jarak awal untuk semua node.
    # Semua node diberi nilai float('inf') karena pada awalnya jaraknya belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan data berbentuk (jarak_sementara, nama_node).
    # Node awal dimasukkan pertama kali dengan jarak 0.
    priority_queue = [(0, start)]

    # Perulangan berjalan selama priority queue masih memiliki node yang perlu diproses.
    while priority_queue:
        # Mengambil node dengan jarak sementara paling kecil dari priority queue.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak terbaik yang sudah tercatat,
        # maka data tersebut sudah usang dan tidak perlu diproses lagi.
        if current_distance > distances[current_node]:
            continue

        # Mengambil semua tetangga dari node yang sedang diproses.
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru menuju neighbor melalui current_node.
            distance = current_distance + weight

            # Jika jarak baru lebih kecil dari jarak yang tersimpan sebelumnya,
            # maka jarak terpendek menuju neighbor perlu diperbarui.
            if distance < distances[neighbor]:
                # Menyimpan jarak baru yang lebih kecil.
                distances[neighbor] = distance

                # Memasukkan neighbor ke priority queue agar diproses sesuai jarak terkecilnya.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan dictionary berisi jarak terpendek dari start ke semua node.
    return distances


# Menjalankan algoritma Dijkstra dengan node awal A.
hasil = dijkstra(graph, 'A')

# Menampilkan hasil akhir jarak terpendek.
print(hasil)

# Penjelasan hasil:
# A = 0 karena jarak dari A ke dirinya sendiri adalah 0.
# B = 4 karena jalur langsung A -> B memiliki bobot 4.
# C = 2 karena jalur langsung A -> C memiliki bobot 2.
# D = 3 karena jalur terbaik adalah A -> C -> D dengan total bobot 2 + 1 = 3.
