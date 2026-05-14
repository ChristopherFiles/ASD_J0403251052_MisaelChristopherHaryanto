# ============================================
# Nama : Misael Christopher Haryanto
# NIM  : J0403251052
# Kelas: B1
# Latihan 4: Jaringan Kabel Antar Gedung
# ============================================
import heapq

graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'GedungA')
print("Jaringan Kabel Minimum:")
for edge in mst:
    print(edge)
print("Total biaya =", total)

# Jawaban Analisis:
# 1. Algoritma: Prim.
# 2. Edge dipilih: (GedungA, GedungC), (GedungC, GedungD), (GedungD, GedungB).
# 3. Total biaya minimum = 6.
# 4. MST cocok karena efisien dan tanpa kabel berlebih.
