import calendar
import datetime


class Overtime:
    __dt = datetime.date.today()
    __lima_hari_kerja = True
    data = {}

    def __init__(self, tahun=__dt.year, bulan=__dt.month, tanggal=__dt.day):
        self.kalender = calendar.weekday(tahun, bulan, tanggal)
        kon = datetime.date(tahun, bulan, tanggal)
        self.data_hari = {kon.strftime('%d') : {}}
        self.data_bulan = {}
        self.data_tahun = {}

    def upah(self, gaji_pokok):
        self.upah_per_jam =  gaji_pokok * 1 / 173

    def lima_hari_kerja(self, jam_lembur:int):
        def weekday():
            jam_pertama = jam_lembur / jam_lembur * 1.5
            jam_selanjutnya = (jam_lembur - 1) * 2
            return jam_pertama + jam_selanjutnya
        def weekend():
            delapan_jam = jam_lembur * 2
            jam_ke_sembilan = jam_lembur / jam_lembur * 3 if jam_lembur > 8 else 0
            jam_selanjutnya = (jam_lembur - 9) * 4 if jam_lembur > 9 else 0
            return delapan_jam + jam_ke_sembilan + jam_selanjutnya
        if self.kalender == 5 or self.kalender == 6:
            self.data_hari['perkalian jam'] = weekend()
            self.data_hari['perkalian upah'] = weekend() * self.upah_per_jam
        else:
            self.data_hari['perkalian jam'] = weekday()
            self.data_hari['perkalian upah'] = weekday() * self.upah_per_jam

    def enam_hari_kerja(self):
        def weekday():
            jam_pertama = 1.5 * self.upah_per_jam
            jam_selanjutnya = 2 * self.upah_per_jam

        def weekend():
            tujuh_jam = 2 * self.upah_per_jam
            jam_ke_delapan = 3 * self.upah_per_jam
            jam_selanjutnya = 4 * self.upah_per_jam