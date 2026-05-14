# ============================================
# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1
# Latihan 2: Implementasi Algoritma Kruskal
# ============================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

edges.sort()
mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge pertama dipilih: (C, D) bobot 1.
# 2. Edge bobot kecil dipilih dulu karena Kruskal mencari biaya minimum.
# 3. Total bobot MST = 6.
# 4. Edge tertentu tidak dipilih karena membentuk cycle.
