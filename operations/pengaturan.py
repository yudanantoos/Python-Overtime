import configparser

pengaturan = configparser.ConfigParser()
pengaturan['DEFAULT'] = {'DataDir' : '../Data',
                         'DataFile' : '${datadir}/data-overtime.json',
                         'Gapok' : 0}

def simpan_pengaturan():
    with open('tes.ini', 'w') as simpan:
        pengaturan.write(simpan)

def load_pengaturan():
    pengaturan.read('tes.ini')
    pengaturan.sections()
    return pengaturan