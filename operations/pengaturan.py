import configparser

pengaturan = configparser.ConfigParser()

pengaturan['DEFAULT']['Gapok'] = '0'

def simpan_pengaturan():
    with open('config.ini', 'w') as simpan:
        pengaturan.write(simpan)

def load_pengaturan():
    pengaturan.read('config.ini')
    pengaturan.sections()
    return pengaturan