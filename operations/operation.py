import datetime
from . import calculation
# import re

nilai_gapok = calculation.ambil_gapok()
f_nilai_gapok = calculation.format_rupiah(nilai_gapok)
my_data = calculation.ambil_data()

def semua_data_overtime():
    if calculation.cek_data_isi():
        print("=" * 150)
        print(f"\t\t\t\t\t\t\t\t\tALL DATA OVERTIME")
        print("No \t\t Tanggal \t\t Jam lembur \t\t Perkalian Jam Lembur \t\t Nominal Uang Lembur \t\t Jumlah Jam Asli \t\t Jumlah Uang Lembur")
        print('=' * 150)
        print('='*100,'\t  ', calculation.jumlah_jam_asli(),'  \t\t\t\t', calculation.format_rupiah(calculation.jumlah_uang_lembur()))
        no = 1
        for th in my_data:
            for u in my_data[th]:
                for i in my_data[th][u]:
                    print(f"{no}\t\t{i}-{u}-{th}\t\t\t{my_data[th][u][i]['Jam lembur']}\t\t\t\t\t\t{my_data[th][u][i]['Perkalian jam lembur']}\t\t\t\t\t\t{calculation.format_rupiah(my_data[th][u][i]['Nominal uang lembur'])}")
                    no += 1
        print("=" * 150)
    else:
        print("Tidak ada data")

def data_overtime():
    if calculation.cek_data_isi():
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
                        print(f"{no}\t\t{i}-{bulan}-{tahun}\t\t\t{ambil_harian[i]['Jam lembur']}\t\t\t\t\t\t{ambil_harian[i]['Perkalian jam lembur']}\t\t\t\t\t\t{calculation.format_rupiah(ambil_harian[i]['Nominal uang lembur'])}")
                        no += 1
                    print("=" * 100)
                else:
                    print(f"Tidak ada data lemburan Bulan {bulan} di Tahun {tahun}")
                    print("Atau input yang kamu masukkan salah")
            else:
                print(f"Tidak ada data lemburan di Tahun {tahun}")
                print("Atau input yang kamu masukkan salah")
        elif ouwe == '2':
            semua_data_overtime()
        else:
            print("Pilihan tidak tersedia")
    else:
        print("Tidak ada data lemburan")

def input_overtime():
    if nilai_gapok == 0:
        print("Gapok masih 0, masukkin gapok dulu ya,.")
        input_gaji_pokok()

    try:
        print("Masukkan tanggal, bulan, tahun")
        print("Masukkan Tanggal 1 - 31: ")
        tanggal = int(input())
        print("Masukkan Bulan 1 - 12: ")
        bulan = int(input())
        print("Masukkan 4 digit Tahun 1970 - Sekarang: ")
        tahun = int(input())
        print("Masukkan Jam Lembur: ")
        print("Pemisah desimal pakai dot (titik) yaa,.")
        jam_lembur = float(input())

        calculation.rumus(tahun, bulan, tanggal, jam_lembur)
        ddmmyyyy = datetime.date(tahun, bulan, tanggal)
        f_yyyy = ddmmyyyy.strftime('%Y')

        if str(tahun) == f_yyyy:
            if str(tahun) in my_data:
                data_bulanan = my_data[str(tahun)]
                if str(bulan) in data_bulanan:
                    data_harian = data_bulanan[str(bulan)]
                    if str(tanggal) in data_harian:
                        print(f"Data tanggal {tanggal}-{bulan}-{tahun} sudah ada")
                        print("Mau di edit kah?")
                        print("1. Ya, edit")
                        print("2. Tidak, batalkan")
                        jo = input()
                        if jo == '1':
                            data_harian[str(tanggal)] = {'Jam lembur': jam_lembur,
                                                         'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                         'Nominal uang lembur': calculation.hasil_uang_lemburan}
                            calculation.edit_data(my_data)
                        else:
                            print("Input data dibatalkan")
                    else:
                        data_harian[str(tanggal)] = {'Jam lembur': jam_lembur,
                                                     'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                     'Nominal uang lembur': calculation.hasil_uang_lemburan}
                        calculation.input_data(my_data)
                else:
                    data_bulanan[str(bulan)] = {str(tanggal): {'Jam lembur': jam_lembur,
                                                     'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                     'Nominal uang lembur': calculation.hasil_uang_lemburan}}
                    calculation.input_data(my_data)
            else:
                my_data[str(tahun)] = {str(bulan): {str(tanggal): {'Jam lembur': jam_lembur,
                                                    'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                    'Nominal uang lembur': calculation.hasil_uang_lemburan}}}
                calculation.input_data(my_data)
        else:
            print("Kesalahan input")
            print("Input Tahun harus 4 angka ya,.")

    except ValueError:
        print("Kesalahan input")
        print("Coba cek lagi format nya ya,.")

def edit_overtime():
    if calculation.cek_data_isi():
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
        print("Format %d-%m-%Y")
        try:
            tgl = input()

            # Sudah di cek pakai fungsi
            # Cek string menggunakan regular expresion (import re)
            # Sudah tidak digunakan, ganti pakai pengecekan tanggal
            # pattern_str = r'^\d{2}-\d{2}-\d{4}$'
            # if re.match(pattern_str, tgl):


            dmy = calculation.spil_tgl(tgl)
            dd = dmy[0]
            mm = dmy[1]
            yyyy = dmy[2]
            ddmmyyyy = datetime.date(yyyy, mm, dd)
            f_yyyy = ddmmyyyy.strftime('%d-%m-%Y')

            if tgl == f_yyyy:
                print("Masukkan jam lembur:")
                print("Pemisah desimal pakai dot (titik) yaa,.")
                jam_lembur = float(input())

                calculation.rumus(yyyy, mm, dd, jam_lembur)

                if (f"{str(yyyy)}" in my_data and
                        f"{str(mm)}" in my_data[str(yyyy)] and
                        f"{str(dd)}" in my_data[str(yyyy)][str(mm)]):
                    my_data[str(yyyy)][str(mm)][str(dd)] = {'Jam lembur': jam_lembur,
                                                            'Perkalian jam lembur': calculation.hasil_perkalian_jam,
                                                            'Nominal uang lembur': calculation.hasil_uang_lemburan}
                    calculation.edit_data(my_data)
                else:
                    print("Waktu yang diminta tidak ada euyy,.")
            else:
                print("Masukan tidak sesuai format")
        except ValueError:
            print("Input yang dimasukkan salah euyy")
            print("Atau tanggal yang diminta tidak ada")
    else:
        print("Tidak ada yang bisa diedit")

def hapus_overtime():
    if calculation.cek_data_isi():
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
            print("Isikan sesuai data dengan format %d-%m-%Y gitu yaa,.")
            try:
                tgl = input()
                # Cek string menggunakan regular expresion (import re)
                #pattern_str = r'^\d{2}-\d{2}-\d{4}$'
                #if re.match(pattern_str, tgl):
                sptgl = calculation.spil_tgl(tgl)
                tg = sptgl[0]
                mm = sptgl[1]
                yyyy = sptgl[2]

                ddmmyyyy = datetime.date(yyyy, mm, tg)
                f_yyyy = ddmmyyyy.strftime('%d-%m-%Y')

                if tgl == f_yyyy:
                    if str(tg) in my_data[str(yyyy)][str(mm)]:
                        my_data[str(yyyy)][str(mm)].pop(str(tg))
                        calculation.hapus_data(my_data)
                        print(f"Data tanggal {tgl} dihapus")
                    else:
                        print("Input tidak sesuai data")
                else:
                    print("Format tidak sesuai permintaan")
                    print("Isikan sesuai data dan format wajib seperti ini ya => %d-%m-%Y")
            except ValueError:
                print("Input yang dimasukkan salah euyy")
                print("Atau tanggal yang diminta tidak ada")
        else:
            print("Input yang dimasukkan tidak sesuai")
    else:
        print("Tidak ada data yang bisa dihapus")

def input_gaji_pokok():
    print("Silahkan masukkan gaji pokoknya")
    gapok = input()
    calculation.input_gapok(gapok)