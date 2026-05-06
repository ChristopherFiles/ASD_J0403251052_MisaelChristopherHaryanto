# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Graph berbobot dibuat menggunakan dictionary bersarang.
# Setiap node menyimpan tetangganya beserta bobot/jarak menuju tetangga tersebut.
graph = {
    'A': {'B': 4, 'C': 2},  # Dari A bisa menuju B dengan bobot 4 dan C dengan bobot 2.
    'B': {'D': 5},          # Dari B bisa menuju D dengan bobot 5.
    'C': {'D': 1},          # Dari C bisa menuju D dengan bobot 1.
    'D': {}                 # D adalah node tujuan dan tidak memiliki edge keluar.
}

# Menghitung total bobot jalur pertama, yaitu A -> B -> D.
jalur_1 = graph['A']['B'] + graph['B']['D']

# Menghitung total bobot jalur kedua, yaitu A -> C -> D.
jalur_2 = graph['A']['C'] + graph['C']['D']

# Menampilkan total bobot jalur pertama.
print("Jalur 1: A -> B -> D =", jalur_1)

# Menampilkan total bobot jalur kedua.
print("Jalur 2: A -> C -> D =", jalur_2)

# Percabangan digunakan untuk membandingkan total bobot kedua jalur.
if jalur_1 < jalur_2:
    # Bagian ini dijalankan jika jalur pertama memiliki bobot lebih kecil.
    print("Jalur terpendek adalah A -> B -> D")
else:
    # Bagian ini dijalankan jika jalur kedua memiliki bobot lebih kecil atau sama.
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit,
#    tetapi dari total bobot terkecil. Pada contoh ini jumlah edge kedua jalur sama,
#    namun A -> C -> D lebih baik karena total bobotnya 3, bukan 9.
