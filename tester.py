from operations import calculation

#print("{} jam".format(calculation.jumlah_jam_asli(13,14)))
#print(calculation.format_rupiah(calculation.jumlah_uang_lembur()))
"""
a = calculation.ambil_data()
th =[]
bl = []
tgl = []
dari = '12/01/2024'
sampai = '14/12/2025'

cari_th = list(range(int(dari[6:10]), int(sampai[6:10]) + 1))
cari_bl = list(range(int(dari[3:5]), int(sampai[3:5]) + 1))
cari_tgl = list(range(int(dari[:2]), int(sampai[:2]) + 1))

for thn in a:
    th.append(thn)
    for bln in a[thn]:
        bl.append(bln)
        for tanggal in a[thn][bln]:
            tgl.append(tanggal)

print(f"Data dari {dari} sampai {sampai}: ")
for cth in cari_th:
    if str(cth) in th:
        print(f'{cth} aya di a')
        for cbl in cari_bl:
            if str(cbl) in bl:
                print(f'{cbl} aya di a[th]')
                for ctgl in cari_tgl:
                    if str(ctgl) in tgl:
                        print(f'{ctgl} aya di a[th][bl]')
"""

p = calculation.jumlah_jam_asli('01/01/2024', '12/01/2025')

print(p)