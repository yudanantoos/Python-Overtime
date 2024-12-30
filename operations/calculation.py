import json
import os.path
import calendar
from . import pengaturan

databasenya = pengaturan.load_pengaturan()['DEFAULT']['DataFile']
hasil_perkalian_jam = 0
hasil_uang_lemburan = 0

def cek_database():
    if not os.path.isdir(pengaturan.load_pengaturan()['DEFAULT']['DataDir']) and not os.path.exists(databasenya):
        os.mkdir(pengaturan.load_pengaturan()['DEFAULT']['DataDir'])
        penyimpanan_data = {}
        pd = json.dumps(penyimpanan_data)
        with open(databasenya,'w') as fley:
            fley.write(pd)
        fley.close()
        print('ok')
    else:
        print('not ok')

def ambil_data():
    cek_database()
    with open(databasenya, 'r') as buka:
        g = buka.readline()
    penyimpanan = json.loads(g)
    buka.close()
    return penyimpanan

def input_data(penyimpanan):
    s = json.dumps(penyimpanan)
    with open(databasenya, 'w') as simpan:
        simpan.write(s)
        if simpan.writable():
            print("Data lembur berhasil disimpan")
        else:
            print("Ada kesalahan, data lembur belum tersimpan")
    simpan.close()

def edit_data(edit):
    cek_database()
    if len(ambil_data()) != 0:
        s = json.dumps(edit)
        with open(databasenya, 'r+') as simpan:
            simpan.write(s)
            if simpan.writable():
                print("Data lembur berhasil diedit dan disimpan")
            else:
                print("Ada kesalahan, data lembur belum diedit dan tersimpan")
        simpan.close()
    else:
        print("Belum ada data yang bisa diedit")

def hapus_data(hapus):
    cek_database()
    if len(ambil_data()) != 0:
        s = json.dumps(hapus)
        with open(databasenya, 'w') as hp:
            hp.write(s)
            if hp.writable():
                print("Data lembur berhasil dihapus")
            else:
                print("Ada kesalahan, data lembur belum terhapus")
        hp.close()
    else:
        print("Belum ada data yang bisa dihapus")

def ambil_gapok():
    """
    cek_database()
    with open(database_gapok, 'r') as baca:
        lihat = baca.readline()
    konversi = json.loads(lihat)
    baca.close()
    return float(konversi['Gapok'])
    """
    data = float(pengaturan.load_pengaturan()['DEFAULT']['Gapok'])
    return data


def input_gapok(gapok):
    """
    tampung = {'Gapok': gapok}
    js = json.dumps(tampung)
    with open(database_gapok, 'w') as simpan:
        simpan.write(js)
        if simpan.writable():
            print("Gapok berhasil disimpan")
        else:
            print("Ada kesalahan, gapok belum tersimpan")
    simpan.close()
    """
    pengaturan.pengaturan['DEFAULT']['Gapok'] = gapok
    pengaturan.simpan_pengaturan()
    if pengaturan.load_pengaturan()['DEFAULT']['Gapok'] == gapok:
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