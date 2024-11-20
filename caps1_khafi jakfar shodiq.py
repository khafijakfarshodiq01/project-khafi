# Data mobil disimpan dalam list
mobil_list = ['1', 'mitsubishi','pajero',2024,76]

# Fungsi untuk menambahkan mobil
def tambah_mobil():
    print("Tambah Mobil")
    merk = input("Masukkan merk mobil: ")
    model = input("Masukkan model mobil: ")
    tahun = input("Masukkan tahun mobil: ")
    harga = input("Masukkan harga mobil: ")

    # Validasi input
    if merk and model and tahun.isdigit() and harga.replace('.', '', 1).isdigit():
        tahun = int(tahun)
        harga = float(harga)
        mobil = {
            'merk': merk,
            'model': model,
            'tahun': tahun,
            'harga': harga
        }
        mobil_list.append(mobil)
        print("Mobil berhasil ditambahkan!")
    else:
        print("Input tidak valid, silakan coba lagi!")

# Fungsi untuk melihat semua mobil
def lihat_mobil():
    print("Daftar Mobil")
    if not mobil_list:
        print("Tidak ada data mobil.")
    else:
        for idx, mobil in enumerate(mobil_list):
            print(f"ID: {idx+1} | Merk: {mobil['merk']} | Model: {mobil['model']} | Tahun: {mobil['tahun']} | Harga: {mobil['harga']}")

# Fungsi untuk mengedit mobil berdasarkan ID
def edit_mobil():
    lihat_mobil()
    if mobil_list:
        try:
            id_mobil = int(input("Masukkan ID mobil yang ingin diedit: ")) - 1
            if 0 <= id_mobil < len(mobil_list):
                print("Edit Mobil")
                merk = input(f"Masukkan merk baru (sekarang: {mobil_list[id_mobil]['merk']}): ")
                model = input(f"Masukkan model baru (sekarang: {mobil_list[id_mobil]['model']}): ")
                tahun = input(f"Masukkan tahun baru (sekarang: {mobil_list[id_mobil]['tahun']}): ")
                harga = input(f"Masukkan harga baru (sekarang: {mobil_list[id_mobil]['harga']}): ")

                # Validasi input
                if merk: mobil_list[id_mobil]['merk'] = merk
                if model: mobil_list[id_mobil]['model'] = model
                if tahun.isdigit(): mobil_list[id_mobil]['tahun'] = int(tahun)
                if harga.replace('.', '', 1).isdigit(): mobil_list[id_mobil]['harga'] = float(harga)

                print("Mobil berhasil diperbarui!")
            else:
                print("ID mobil tidak ditemukan!")
        except ValueError:
            print("Masukkan ID yang valid!")

# Fungsi untuk menghapus mobil berdasarkan ID
def hapus_mobil():
    lihat_mobil()
    if mobil_list:
        try:
            id_mobil = int(input("Masukkan ID mobil yang ingin dihapus: ")) - 1
            if 0 <= id_mobil < len(mobil_list):
                mobil_list.pop(id_mobil)
                print("Mobil berhasil dihapus!")
            else:
                print("ID mobil tidak ditemukan!")
        except ValueError:
            print("Masukkan ID yang valid!")

# Fungsi utama untuk menampilkan menu
def menu_utama():
    while True:
        print("\nMenu Utama Toko Mobil")
        print("1. Tambah Mobil")
        print("2. Lihat Daftar Mobil")
        print("3. Edit Mobil")
        print("4. Hapus Mobil")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tambah_mobil()
        elif pilihan == '2':
            lihat_mobil()
        elif pilihan == '3':
            edit_mobil()
        elif pilihan == '4':
            hapus_mobil()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi Toko Mobil!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Menjalankan aplikasi
menu_utama()
