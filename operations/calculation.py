import json
import os.path
import calendar
from . import pengaturan

databasenya = pengaturan.load_pengaturan()['DEFAULT']['datafile']
hasil_perkalian_jam = 0
hasil_uang_lemburan = 0

def cek_database():
    if not os.path.isdir(pengaturan.load_pengaturan()['DEFAULT']['datadir']) and not os.path.exists(databasenya):
        os.mkdir(pengaturan.load_pengaturan()['DEFAULT']['datadir'])
        penyimpanan_data = {}
        pd = json.dumps(penyimpanan_data)
        with open(databasenya,'w') as fley:
            fley.write(pd)
        fley.close()

def ambil_data():
    cek_database()
    with open(databasenya, 'r') as buka:
        g = buka.readline()
    penyimpanan = json.loads(g)
    buka.close()
    return penyimpanan

def simpan_data(simpan):
    s = json.dumps(simpan)
    with open(databasenya, 'w') as save:
        save.write(s)
        if save.writable():
            save.close()
            return True
        else:
            save.close()
            return False

def input_data(penyimpanan):
    if simpan_data(penyimpanan):
        print("Data lembur berhasil diinput dan disimpan")
    else:
        print("Ada kesalahan, data lembur belum tersimpan")

def edit_data(edit):
    cek_database()
    if len(ambil_data()) > 0:
        if simpan_data(edit):
            print("Data lembur berhasil diedit dan disimpan")
        else:
            print("Ada kesalahan, data lembur belum diedit dan tersimpan")
    else:
        print("Belum ada data yang bisa diedit")

def hapus_data(hapus):
    cek_database()
    if len(ambil_data()) > 0:
        if simpan_data(hapus):
            print("Data lembur berhasil dihapus")
        else:
            print("Ada kesalahan, data lembur belum terhapus")
    else:
        print("Belum ada data yang bisa dihapus")

def ambil_gapok():
    data = float(pengaturan.load_pengaturan()['DEFAULT']['gapok'])
    return data


def input_gapok(gapok):
    pengaturan.pengaturan['DEFAULT']['gapok'] = gapok
    pengaturan.simpan_pengaturan()
    if pengaturan.load_pengaturan()['DEFAULT']['gapok'] == gapok:
        print("Gapok berhasil disimpan")
    else:
        print("Ada kesalahan, gapok belum tersimpan")

def rumus(tahun, bulan, tanggal, jam_lembur):
    global hasil_perkalian_jam, hasil_uang_lemburan

    cal = calendar.weekday(int(tahun), int(bulan), int(tanggal))

    if cal == 5 or cal == 6:
        jam_pertama = 2
    else:
        jam_pertama = 1.5
    jam_selanjutnya = (jam_lembur - 1) * 2

    gaji_perjam = ambil_gapok() * 1 / 173
    hasil_perkalian_jam = jam_pertama + jam_selanjutnya
    hasil_uang_lemburan = gaji_perjam * hasil_perkalian_jam

def format_rupiah(nominal):
    rubah = 'Rp{:,.2f}'.format(nominal)
    return rubah