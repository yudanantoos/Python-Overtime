import datetime

from operations import calculation

a = calculation.ambil_data()
print("Sebelum sortir:", a)

for th in a:
    tahun = list(a)
    tahun.sort()
    a = {i: a.get(i) for i in tahun}
    for bl in a.get(th):
        bulan = list(a.get(th))
        bulan.sort()
        a[th] = {u: a.get(th).get(u) for u in bulan}
        for tg in a.get(th).get(bl):
            tanggal = list(a.get(th).get(bl))
            tanggal.sort()
            a[th][bl] = {e: a.get(th).get(bl).get(e) for e in tanggal}

print("Sesudah sortir:", a)