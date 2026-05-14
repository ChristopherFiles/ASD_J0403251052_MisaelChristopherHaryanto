# ============================================
# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1
# Latihan 5: Jaringan Jalan Antar Kota (Kruskal)
# ============================================

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
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

print("MST Jaringan Jalan:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Kasus: Jaringan Jalan Antar Kota.
# 2. Algoritma: Kruskal.
# 3. Edge dipilih: (Bogor, Depok), (Depok, Jakarta), (Depok, Bandung).
# 4. Total bobot MST = 9.
# 5. Edge lain tidak dipilih karena membentuk cycle atau tidak efisien.
