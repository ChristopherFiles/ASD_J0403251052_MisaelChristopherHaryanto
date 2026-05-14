# ==========================================================
# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1
# Latihan 1: Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree (harus menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# 1. Graph awal berisi semua edge, sedangkan spanning tree hanya subset edge
#    yang menghubungkan semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle agar tetap berbentuk pohon.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena hanya cukup
#    untuk menghubungkan semua node (n-1 edge).
# ==========================================================
