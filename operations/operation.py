from . import calculation
import re

nilai_gapok = calculation.ambil_gapok()
my_data = calculation.ambil_data()

def semua_data_overtime():
    print("=" * 100)
    print(f"\t\t\t\t\t\t\t\t\tALL DATA OVERTIME")
    print("No \t\t Tanggal \t\t Jam lembur \t\t Perkalian Jam Lembur \t\t Nominal Uang Lembur")
    print('=' * 100)

    no = 1
    for th in my_data:
        for u in my_data[th]:
            for i in my_data[th][u]:
                print(f"{no}\t\t{i}/{u}/{th}\t\t\t{my_data[th][u][i]['Jam lembur']}\t\t\t{my_data[th][u][i]['Perkalian jam lembur']}\t\t\t\t{calculation.format_rupiah(my_data[th][u][i]['Nominal uang lembur'])}")
                no += 1
    print("=" * 100)

def data_overtime():
    if len(my_data) > 0:
        print("1. Pilih tahun dan bulan")
        print("2. Tampilkan semua")
        print("Input pilihan:")
        ouwe = input()
        if ouwe == '1':
            print("Data yang tersedia:")
            print("Tahun")
            print("\t| - Bulan")

            for i in my_data:
                print(i)
                for u in my_data[i]:
                    print('\t| -',u)


            print("Masukkan tahun:")
            tahun = input()
            print("Masukkan bulan:")
            bulan = input()

            if tahun in my_data.keys():
                ambil_bulanan = my_data[tahun]
                if bulan in ambil_bulanan.keys():
                    ambil_harian = ambil_bulanan[bulan]
                    print("="*100)
                    print(f"\t\t\t\t\t\t\t\t\tDATA OVERTIME TAHUN {tahun} BULAN {bulan}")
                    print("No \t\t Tanggal \t\t Jam lembur \t\t Perkalian Jam Lembur \t\t Nominal Uang Lembur")
                    print('=' * 100)
                    no = 1
                    for i in ambil_harian:
                        print(f"{no}\t\t{i}/{bulan}/{tahun}\t\t\t{ambil_harian[i]['Jam lembur']}\t\t\t\t\t\t{ambil_harian[i]['Perkalian jam lembur']}\t\t\t\t\t\t{calculation.format_rupiah(ambil_harian[i]['Nominal uang lembur'])}")
                        no += 1
                    print("=" * 100)
                else:
                    print(f"Belum ada data lemburan Bulan {bulan} di Tahun {tahun}")
                    print("Atau input yang kamu masukkan salah")
            else:
                print(f"Belum ada data lemburan di Tahun {tahun}")
                print("Atau input yang kamu masukkan salah")
        elif ouwe == '2':
            semua_data_overtime()
        else:
            print("Pilihan tidak tersedia")
    else:
        print("Tidak ada data lemburan")

def input_overtime():
    if nilai_gapok == 0:
        print("Gapok masih 0, mau masukkin gapoknya?")
        print("1. Ya")
        print("2. Tidak")
        p = input()
        if p == '1':
            input_gaji_pokok()

    try:
        print("Masukkan 2 angka tanggal, 2 angka bulan, 4 angka tahun")
        print("Masukkan Tanggal 1 - 31: ")
        tanggal = input()
        print("Masukkan Bulan 1 - 12: ")
        bulan = input()
        print("Masukkan Tahun 1970 - Sekarang: ")
        tahun = input()
        print("Masukkan Jam Lembur: ")
        jam_lembur = float(input())

        if len(tanggal) == 2 and len(bulan) == 2 and len(tahun) == 4:
            calculation.rumus(tahun, bulan, tanggal, jam_lembur)
            if tahun in my_data:
                data_bulanan = my_data[tahun]
                if bulan in data_bulanan:
                    data_harian = data_bulanan[bulan]
                    if tanggal in data_harian:
                        print(f"Data tanggal {tanggal}/{bulan}/{tahun} sudah ada")
                        print("Mau di edit kah?")
                        print("1. Ya, edit")
                        print("2. Tidak, batalkan")
                        jo = input()
                        if jo == '1':
                            data_harian[tanggal] = {'Jam lembur': jam_lembur,
                                                     'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                     'Nominal uang lembur': calculation.hasil_uang_lemburan}
                            calculation.edit_data(my_data)
                        else:
                            print("Input data dibatalkan")
                    else:
                        data_harian[tanggal] = {'Jam lembur': jam_lembur,
                                                'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                'Nominal uang lembur': calculation.hasil_uang_lemburan}
                        calculation.input_data(my_data)
                else:
                    data_bulanan[bulan] = {tanggal: {'Jam lembur': jam_lembur,
                                                     'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                     'Nominal uang lembur': calculation.hasil_uang_lemburan}}
                    calculation.input_data(my_data)
            else:
                my_data[tahun] = {bulan: {tanggal: {'Jam lembur': jam_lembur,
                                                          'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                          'Nominal uang lembur': calculation.hasil_uang_lemburan}}}
                calculation.input_data(my_data)
        else:
            print("Input tanggal, bulan, dan tahun yang dimasukkan salah euyy")
            print("Formatnya harus seperti ini ges => dd/mm/yyyy")
    except ValueError:
        print("Ada kesalahan input, Jam Lembur hanya menerima angka dengan dot (titik) sebagai koma ya,.")

def edit_overtime():
    if len(my_data) > 0:
        print("Data yang tersedia:")
        print("Tahun")
        print("\t| - Bulan")
        print("\t\t\t| - Tanggal")

        for i in my_data:
            print(i)
            for u in my_data[i]:
                print('\t| -', u)
                for o in my_data[i][u]:
                    print('\t\t | -', o)

        print("Silahkan isi tanggal yang akan diedit")
        print("Format dd/mm/yyyy")
        tgl = input()
        # Cek string menggunakan regular expresion (import re)
        pattern_str = r'^\d{2}/\d{2}/\d{4}$'
        if re.match(pattern_str, tgl):
            dd = tgl[:2]
            mm = tgl[3:5]
            yyyy = tgl[6:10]
            try:
                print("Masukkan jam lembur:")
                jam_lembur = float(input())

                calculation.rumus(yyyy, mm, dd, jam_lembur)

                if f"{dd}" in my_data[yyyy][mm]:
                    my_data[yyyy][mm][dd] = {'Jam lembur': jam_lembur,
                                            'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                            'Nominal uang lembur': calculation.hasil_uang_lemburan}
                calculation.edit_data(my_data)
            except ValueError:
                print("Input yang dimasukkan salah euyy")
                print("Formatnya harus seperti ini ges => dd/mm/yyyy")
            except KeyError:
                print("Tanggal yang diminta tidak ada euyy")
        else:
            print("Masukan tidak sesuai format")
    else:
        print("Tidak ada yang bisa diedit")

def hapus_overtime():
    if len(my_data) > 0:
        print("Pilih metode hapus")
        print("1. Hapus tahunan\t\t2. Hapus bulanan\t\t3. Hapus harian")
        print("Input pilihan:")
        i = input()
        if i == '1':
            print("Data pertahun:")
            for ow in my_data:
                print(ow)
            print("Pilih tahun yang akan dihapus")
            joe = input()
            if joe in my_data:
                my_data.pop(joe)
                calculation.hapus_data(my_data)
                print(f"Data tahun {joe} dihapus")
            else:
                print("Input tahun tidak ada atau tidak sesuai data")
        elif i == '2':
            print("Data perbulan:")

            for i in my_data:
                print(i)
                for u in my_data[i]:
                    print('\t| -', u)

            print("Pilih tahun yang akan dihapus")
            joe = input()
            if joe in my_data:
                print("Pilih bulan yang akan dihapus")
                jahe = input()
                if jahe in my_data[joe]:
                    my_data[joe].pop(jahe)
                    calculation.hapus_data(my_data)
                    print(f"Data bulan {jahe} di tahun {joe} dihapus")
                else:
                    print("Tidak ada data bulan yang diminta")
            else:
                print("Input tahun tidak ada atau tidak sesuai data")

        elif i == '3':
            print("Data perhari:")

            for i in my_data:
                print(i)
                for u in my_data[i]:
                    print('\t| -', u)
                    for o in my_data[i][u]:
                        print('\t\t| -', o)

            print("Silahkan isi tanggal yang akan dihapus")
            print("Isikan sesuai data dengan format dd/mm/yyy gitu yaa,.")
            tgl = input()
            # Cek string menggunakan regular expresion (import re)
            pattern_str = r'^\d{2}/\d{2}/\d{4}$'
            if re.match(pattern_str, tgl):
                tg = tgl[:2]
                mm = tgl[3:5]
                yyyy = tgl[6:10]
                if tg in my_data[yyyy][mm]:
                    my_data[yyyy][mm].pop(tg)
                    calculation.hapus_data(my_data)
                    print(f"Data tanggal {tgl} dihapus")
                else:
                    print("Input tidak sesuai data")
            else:
                print("Format tidak sesuai permintaan")
                print("Isikan sesuai data dan format wajib seperti ini ya => dd/mm/yyy")
        else:
            print("Input yang dimasukkan tidak sesuai")
    else:
        print("Tidak ada data yang bisa dihapus")

def input_gaji_pokok():
    print("Silahkan masukkan gaji pokoknya")
    gapok = input()
    calculation.input_gapok(gapok)