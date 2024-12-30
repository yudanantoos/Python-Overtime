import operations

def menu():
    # Menu
    print("")
    print("=" * 45 + " OVERTIME " + "=" * 45)
    print("Silahkan Pilih Menu")
    print("1. Data Overtime")
    print("2. Input Overtime")
    print("3. Edit Overtime")
    print("4. Hapus Overtime")
    print("5. Input Gapok")
    print("6. Exit Program")

def back_to_menu():
    print("Ketik nol (0) untuk kembali ke menu\t\t||\t\tKetik satu (1) untuk keluar program")
    i = input()
    if i == '0':
        menu()
    elif i == '1':
        print("Program ditutup!")
        exit()
    else:
        print("Pilih angka yang sudah ditentukan!")
        back_to_menu()

menu()
while True:
    print("Input pilihan:")
    masukan = input()
    if masukan == '1':
        operations.operation.data_overtime()
        back_to_menu()
    elif masukan == '2':
        operations.operation.input_overtime()
        back_to_menu()
    elif masukan == '3':
        operations.operation.edit_overtime()
        back_to_menu()
    elif masukan == '4':
        operations.operation.hapus_overtime()
        back_to_menu()
    elif masukan == '5':
        operations.operation.input_gaji_pokok()
        back_to_menu()
    elif masukan == '6':
        print("Program ditutup!")
        exit()
    else:
        print("Kamu salah memasukkan perintah!")
        back_to_menu()