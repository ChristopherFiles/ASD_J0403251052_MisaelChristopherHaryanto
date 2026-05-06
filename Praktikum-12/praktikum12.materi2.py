# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Materi 2: Implementasi Algoritma Bellman-Ford
# ==========================================================

# Graph berbobot berikut memiliki edge negatif, yaitu C -> B dengan bobot -2.
# Bellman-Ford digunakan karena algoritma ini dapat menangani bobot negatif.
graph = {
    'A': {'B': 5, 'C': 4},  # Node A terhubung ke B berbobot 5 dan ke C berbobot 4.
    'B': {},               # Node B tidak memiliki tetangga keluar.
    'C': {'B': -2}         # Node C terhubung ke B dengan bobot negatif -2.
}


def bellman_ford(graph, start):
    """Menghitung jarak terpendek dari node start menggunakan Bellman-Ford."""

    # Membuat jarak awal semua node menjadi tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke node awal selalu 0.
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi edge sebanyak jumlah node - 1.
    # Pada graph dengan n node, jalur terpendek tanpa siklus maksimal memiliki n - 1 edge.
    for _ in range(len(graph) - 1):
        # Variabel updated dipakai untuk mengecek apakah masih ada perubahan jarak.
        updated = False

        # Memeriksa setiap node asal pada graph.
        for node in graph:
            # Memeriksa setiap tetangga dan bobot dari node asal.
            for neighbor, weight in graph[node].items():
                # Jika node asal belum bisa dijangkau, edge dari node itu dilewati.
                if distances[node] == float('inf'):
                    continue

                # Menghitung jarak baru menuju neighbor melalui node asal.
                new_distance = distances[node] + weight

                # Jika jarak baru lebih kecil, berarti ditemukan jalur yang lebih pendek.
                if new_distance < distances[neighbor]:
                    # Memperbarui jarak terpendek menuju neighbor.
                    distances[neighbor] = new_distance

                    # Menandai bahwa masih ada perubahan pada iterasi ini.
                    updated = True

        # Jika tidak ada jarak yang berubah, proses relaksasi bisa dihentikan lebih cepat.
        if not updated:
            break

    # Pemeriksaan tambahan untuk mendeteksi siklus negatif.
    # Jika setelah n - 1 relaksasi masih ada jarak yang bisa diperkecil,
    # berarti graph memiliki siklus negatif yang membuat shortest path tidak valid.
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph mengandung siklus negatif.")

    # Mengembalikan jarak terpendek dari node start ke semua node.
    return distances


# Menjalankan Bellman-Ford dari node awal A.
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil jarak terpendek.
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Penjelasan hasil:
# A = 0 karena A adalah node awal.
# C = 4 karena jalur langsung A -> C memiliki bobot 4.
# B = 2 karena jalur A -> C -> B memiliki total bobot 4 + (-2) = 2,
# sehingga lebih kecil daripada jalur langsung A -> B yang berbobot 5.
