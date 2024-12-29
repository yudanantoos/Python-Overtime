import os.path

def check_dir():
    if not os.path.isdir('Data'):
        os.mkdir('Data')
        print("Direktori 'Data' dibuat")
    else:
        print("Direktori 'Data' sudah ada")