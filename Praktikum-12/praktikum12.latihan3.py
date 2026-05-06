# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif pada edge C -> B.
# Bellman-Ford dipakai karena dapat menghitung shortest path walaupun ada bobot negatif.
graph = {
    'A': {'B': 5, 'C': 4},  # Dari A bisa langsung ke B dengan bobot 5 dan ke C dengan bobot 4.
    'B': {},               # B tidak memiliki edge keluar.
    'C': {'B': -2}         # Dari C ke B terdapat bobot negatif -2.
}


def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node start ke node start adalah 0.
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1.
    # Relaksasi berulang memastikan jarak terpendek menyebar ke semua node.
    for _ in range(len(graph) - 1):
        # Memeriksa setiap node asal di dalam graph.
        for node in graph:
            # Memeriksa setiap edge dari node asal ke neighbor.
            for neighbor, weight in graph[node].items():
                # Proses update hanya dilakukan jika node asal sudah bisa dicapai.
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    # Jika jarak melalui node asal lebih kecil, update jarak neighbor.
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak terpendek dari start.
    return distances


# Menjalankan algoritma Bellman-Ford dari node A.
hasil = bellman_ford(graph, 'A')

# Menampilkan jarak terpendek dari A ke semua node.
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 4 + (-2) = 2.
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah A -> C -> B.
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini
#    tidak langsung mengunci satu node seperti Dijkstra. Bellman-Ford mengulang proses
#    relaksasi edge sehingga jarak yang awalnya besar masih dapat diperbaiki.
# 5. Relaksasi edge adalah proses membandingkan jarak lama menuju suatu node dengan
#    jarak baru melalui edge tertentu. Jika jarak baru lebih kecil, nilai jaraknya diperbarui.
# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah Dijkstra memakai priority queue
#    dan pendekatan greedy untuk bobot positif, sedangkan Bellman-Ford merelaksasi
#    semua edge berulang kali sehingga dapat menangani bobot negatif, tetapi lebih lambat.
