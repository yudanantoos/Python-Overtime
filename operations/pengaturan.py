import configparser
import os

pengaturan = configparser.ConfigParser()
pengaturan['DEFAULT'] = {'DataDir' : '../Data',
                         'DataFile' : '%(datadir)s/data-overtime.json',
                         'Gapok' : 0}

def simpan_pengaturan():
    with open('config.ini', 'w') as simpan:
        pengaturan.write(simpan)

def load_pengaturan():
    pengaturan.read('tes.ini')
    pengaturan.sections()
    return pengaturan