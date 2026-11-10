import modul_sensor


def input_sensor():
    # Meminta suhu dan kelembaban secara aman, mengembalikan tuple (suhu, kelembaban)
    while True:
        try:
            suhu = float(input("Suhu Udara (C), 0-100       : "))
            if suhu < 0 or suhu > 100:
                print("  [Warning] Suhu harus di antara 0 sampai 100. Coba lagi.")
                continue
            break
        except ValueError:
            print("  [Error] Input harus berupa angka, bukan huruf/teks. Coba lagi.")

    while True:
        try:
            lembab = float(input("Kelembaban Tanah (%), 0-100 : "))
            if lembab < 0 or lembab > 100:
                print("  [Warning] Kelembaban harus di antara 0 sampai 100. Coba lagi.")
                continue
            break
        except ValueError:
            print("  [Error] Input harus berupa angka, bukan huruf/teks. Coba lagi.")

    return (suhu, lembab)


def rekam_data(log_kebun):
    # Menu 1: rekam data baru lalu append tuple ke log_kebun
    print("\n--- Rekam Data Sensor ---")
    data = input_sensor()
    log_kebun.append(data)
    print(f"Data tersimpan. Total data saat ini: {len(log_kebun)}")


def analisis_tren(log_kebun):
    # Menu 2: analisis 3 data terakhir menggunakan slicing
    if len(log_kebun) == 0:
        print("\n  [Warning] Belum ada data. Rekam data dulu lewat menu 1.")
        return

    tiga_terakhir = log_kebun[-3:]

    print("\n--- Analisis Tren (3 Data Terakhir) ---")
    print(f"Lokasi : {modul_sensor.LOKASI[0]}")
    print("=" * 45)
    nomor = 1
    for suhu, lembab in tiga_terakhir:
        print(f"Data {nomor} -> Suhu: {suhu:.1f} C | Kelembaban: {lembab:.1f} %")
        nomor += 1

    rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
    status = modul_sensor.evaluasi_irigasi(rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS)

    print("-" * 45)
    print(f"Rata-rata Suhu       : {rata_suhu:.2f} C")
    print(f"Rata-rata Kelembaban : {rata_lembab:.2f} %")
    print(f"Ambang Kritis        : Suhu > {modul_sensor.AMBANG_KRITIS[0]} C atau Lembab < {modul_sensor.AMBANG_KRITIS[1]} %")
    print(f"Status               : {status}")
    print("=" * 45)


def main():
    log_kebun = []

    while True:
        print("\n===== MONITORING IOT KAMPUNG ANGGUR =====")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2/3): "))
        except ValueError:
            print("  [Error] Menu harus berupa angka 1, 2, atau 3.")
            continue

        if pilihan == 1:
            rekam_data(log_kebun)
        elif pilihan == 2:
            analisis_tren(log_kebun)
        elif pilihan == 3:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("  [Warning] Pilihan tidak tersedia. Pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()