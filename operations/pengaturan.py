import configparser

pengaturan = configparser.ConfigParser()

pengaturan['DEFAULT']['gapok'] = '0'

def simpan_pengaturan():
    with open('config.ini', 'w') as simpan:
        pengaturan.write(simpan)
    simpan.close()

def load_pengaturan():
    pengaturan.read('config.ini')
    pengaturan.sections()
    return pengaturan