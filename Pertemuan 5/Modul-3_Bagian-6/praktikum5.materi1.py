# ==========================================
# Nama  : [Nama Kamu]
# NIM   : [NIM Kamu]
# Kelas : [Kelas Kamu]
# Tugas : Praktikum 5 - Materi 1 (Faktorial)
# ==========================================

# Fungsi rekursif untuk menghitung nilai faktorial dari n
def faktorial(n):
    # Base case: Kondisi berhenti ketika n mencapai 0. 
        # Faktorial dari 0 adalah 1.
            if n == 0:
                    return 1
                        
                            # Recursive case: Mengalikan n dengan hasil faktorial (n-1).
                                # Ukuran masalah diperkecil setiap kali fungsi memanggil dirinya sendiri.
                                    return n * faktorial(n - 1)

                                    # Mencetak hasil faktorial 5 (yaitu 5 * 4 * 3 * 2 * 1 * 1)
                                    print(faktorial(5)) # Output: 120