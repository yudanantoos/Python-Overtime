import datetime
import json
import os.path
import calendar
from . import pengaturan

databasenya = pengaturan.load_pengaturan()['DEFAULT']['datafile']
hasil_perkalian_jam = 0
hasil_uang_lemburan = 0

def cek_data_isi():
    if not os.path.isdir(pengaturan.load_pengaturan()['DEFAULT']['datadir']):
        os.mkdir(pengaturan.load_pengaturan()['DEFAULT']['datadir'])

    if not os.path.exists(databasenya):
        penyimpanan_data = {}
        pd = json.dumps(penyimpanan_data)
        with open(databasenya,'w') as fley:
            fley.write(pd)
        fley.close()

    penyimpanan_data = ambil_data()
    try:
        if len(penyimpanan_data) > 0:
            return True
    except TypeError:
        print("Error TypeError")

def ambil_data():
    try:
        with open(databasenya, 'r') as buka:
            g = buka.readline()
        penyimpanan = json.loads(g)
        buka.close()
        return penyimpanan
    except json.JSONDecodeError:
        print("Ada kesalahan pada file .json")

def simpan_data(simpan):
    s = json.dumps(simpan)
    with open(databasenya, 'w') as save:
        save.write(s)
        if save.writable():
            return True
        save.close()

def input_data(penyimpanan):
    if simpan_data(penyimpanan):
        print("Data lembur berhasil diinput dan disimpan")
    else:
        print("Ada kesalahan, data lembur belum tersimpan")

def edit_data(edit):
    #cek_database()
    if len(ambil_data()) > 0:
        if simpan_data(edit):
            print("Data lembur berhasil diedit dan disimpan")
        else:
            print("Ada kesalahan, data lembur belum diedit dan tersimpan")
    else:
        print("Belum ada data yang bisa diedit")

def hapus_data(hapus):
    #cek_database()
    if len(ambil_data()) > 0:
        if simpan_data(hapus):
            print("Data lembur berhasil dihapus")
        else:
            print("Ada kesalahan, data lembur belum terhapus")
    else:
        print("Belum ada data yang bisa dihapus")

def ambil_gapok():
    return float(pengaturan.load_pengaturan()['DEFAULT']['gapok'])

def input_gapok(gapok):
    pengaturan.pengaturan['DEFAULT']['gapok'] = gapok
    pengaturan.simpan_pengaturan()
    if pengaturan.load_pengaturan()['DEFAULT']['gapok'] == gapok:
        print("Gapok berhasil disimpan")
        print(f'Gapok saat ini: {format_rupiah(pengaturan.load_pengaturan()['DEFAULT']['gapok'])}')
        print("Kalau mau edit gapok langsung di file config.ini ya,.")
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
    rubah = 'Rp {:,.2f}'.format(float(nominal))
    return rubah

def spil_tgl(tglblnthn): #1-1-2025, 1-01-2025, 01-01-2025
    tgl = []
    if len(tglblnthn) == 10:
        tgl.append(tglblnthn[:2])
        tgl.append(tglblnthn[3:5])
        tgl.append(tglblnthn[6:])
        return tgl
    else:
        return tgl.append("Salah input tanggal")

def jumlah_jam_asli(dari_tgl='01-01-1970', sampai_tgl='31-12-2125'):
    ambil_list_jam_asli = ambil_data()
    tampung_hasil = 0
    if cek_data_isi():
        drtgl = spil_tgl(dari_tgl)
        sptgl = spil_tgl(sampai_tgl)
        fromtgl = datetime.date(int(drtgl[2]),int(drtgl[1]),int(drtgl[0]))
        untiltgl = datetime.date(int(sptgl[2]),int(sptgl[1]),int(sptgl[0]))

        while fromtgl <= untiltgl:
            cektgl = fromtgl.strftime('%d')
            cekbln = fromtgl.strftime('%m')
            cekthn = fromtgl.strftime('%Y')
            if (cekthn in ambil_list_jam_asli and
                cekbln in ambil_list_jam_asli[cekthn] and
                cektgl in ambil_list_jam_asli[cekthn][cekbln]):
                tampung_hasil += ambil_list_jam_asli[cekthn][cekbln][cektgl]['Jam lembur']
            fromtgl += datetime.timedelta(days=1)
        return tampung_hasil

def jumlah_uang_lembur(dari_tgl='01-01-1970', sampai_tgl='31-12-2125'):
    ambil_list_jam_asli = ambil_data()
    tampung_hasil = 0
    if cek_data_isi():
        drtgl = spil_tgl(dari_tgl)
        sptgl = spil_tgl(sampai_tgl)
        fromtgl = datetime.date(int(drtgl[2]), int(drtgl[1]), int(drtgl[0]))
        untiltgl = datetime.date(int(sptgl[2]), int(sptgl[1]), int(sptgl[0]))

        while fromtgl <= untiltgl:
            cektgl = fromtgl.strftime('%d')
            cekbln = fromtgl.strftime('%m')
            cekthn = fromtgl.strftime('%Y')
            if (cekthn in ambil_list_jam_asli and
                    cekbln in ambil_list_jam_asli[cekthn] and
                    cektgl in ambil_list_jam_asli[cekthn][cekbln]):
                tampung_hasil += ambil_list_jam_asli[cekthn][cekbln][cektgl]['Nominal uang lembur']
            fromtgl += datetime.timedelta(days=1)
        return tampung_hasil

def sortir(data):
    data_tahun = {}
    data_bulan = {}
    data_hari = {}

