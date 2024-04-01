print("=" * 50)
print("Selamat Datang di Program Pemesanan Tiket Bioskop".center(50))
print("=" * 50)

filmgenre = {
    "action": ["Top Gun: Maverick", "The Batman", "The Northman", "Spider-Man: No Way Home", "No Time to Die"],
    "drama": ["The Glory Part 2", "Taxi Driver 2", "Love to Hate You", "Our Blooming Youth", "Payback"],
    "komedi": ["The Hangover", "Superbad", "Dumb and Dumber", "Anchorman", "Bridesmaids"],
    "horror": ["Smile (2022)", "Hellraiser (2022)", "Orphan: First Kill (2022)", "Incantation (2022)", "Scream (2022)"],
    "anime": ["Worlds Bubble Up Like Soda Pop", "Josee, the Tiger and the Fish", "A Whisker Away", "Made in Abyss: Dawn of the Deep Soul", "Digimon Adventure: Last Evolution Kizuna"]
}

harga_biasa = 50000
harga_hemat = 30000

print("=" * 50)
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print("=" * 50)

if umur > 18:
    print("=" * 50)
    print("Selamat datang,", nama)
    print("=" * 50)

    print("=" * 50)
    print("Pilih genre film:")
    print("1. Action")
    print("2. Drama")
    print("3. Komedi")
    print("4. Horror")
    print("5. Anime")
    print("=" * 50)

    pilihan_genre = int(input("Masukkan nomor genre film yang ingin Anda tonton: "))

    if 1 <= pilihan_genre <= 5:
        genre = ""
        if pilihan_genre == 1:
            genre = "action"
        elif pilihan_genre == 2:
            genre = "drama"
        elif pilihan_genre == 3:
            genre = "komedi"
        elif pilihan_genre == 4:
            genre = "horror"
        elif pilihan_genre == 5:
            genre = "anime"

        print("=" * 50)
        print(f"Daftar film dalam genre {genre.lower()} :")
        for i in range(len(filmgenre[genre])):
            print(f"{i + 1}. {filmgenre[genre][i]}")
        print("=" * 50)

        pilihan_film = int(input(f"Masukkan nomor film {genre.lower()} yang ingin Anda tonton: "))

        if 1 <= pilihan_film <= 5:
            nama_film = filmgenre[genre][pilihan_film - 1]

            hari = input("Masukkan hari Anda ingin menonton (Senin/Selasa/Rabu/Kamis/Jumat/Minggu/Sabtu): ").lower()
            if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
                harga_tiket = harga_hemat
            elif hari == "minggu" or hari == "sabtu":
                harga_tiket = harga_biasa
            else:
                print("Hari tidak valid.")
                exit()

            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin Anda beli: "))
            total_harga = harga_tiket * jumlah_tiket

            print("=" * 50)
            print("Detail Pesanan:")
            print("-" * 50)
            print(f"Nama: {nama}")
            print(f"Umur: {umur}")
            print(f"Film: {nama_film}")
            print(f"Hari: {hari.capitalize()}")

            print("-" * 50)
            print(f"Jumlah Tiket: {jumlah_tiket}")
            print(f"Harga Tiket: Rp{harga_tiket}")
            print("-" * 50)
            print(f"Total Harga: Rp{total_harga}")
            print("=" * 50)

            konfirmasi = input("Apakah Anda ingin melanjutkan pembelian? (Ya/Tidak): ").lower()
            if konfirmasi == "ya":
                print("Pesanan Anda telah dikonfirmasi. Terima kasih telah membeli tiket!")
            else:
                print("Pesanan Anda dibatalkan.")
        else:
            print("Nomor film tidak valid.")
    else:
        print("Nomor genre tidak valid.")
else:
    print("=" * 50)
    print("Maaf, Anda harus berusia di atas 18 tahun untuk menonton film.")
    print("=" * 50)
