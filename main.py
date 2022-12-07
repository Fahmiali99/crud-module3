from functools import reduce

def login():
    arr_user = ([["admin", "admin123", "admin"], ["user", "user123", "user"]])

    print("\n" "*** LOGIN ACCOUNT****" "\n")
    username = input("Username : " "\t")
    password = input("Password : " "\t")

    test = bool
    while test:
        for x in arr_user:
            if username == x[0] and password == x[1] and x[2] == "admin":
                print("\n" + "*** Welcome to Teacher is Admin ***")
                admin()
                break
            elif username == x[0] and password == x[1] and x[2] == "user":
                print("\n" + "*** Welcome to User ***")
                user()
                break
    return test


def admin():
    min = input("\n"
                "1. Input Nilai \n"
                "2. Read Siswa \n"
                "3. Hapus \n"
                "4. Edit \n"
                "5. Logout \n"

                "Masukkan Inputan: ")

    if min == "1":
        create()

    elif min == "2":
        read()
        admin()

    elif min == "3":
        read()
        dlt = int(input("pilih Barang yang ingin dihapus: "))
        delete(hapus, dlt)

    elif min == "4":
        read()
        up = int(input("Pilih yang ingin diupdate: "))
        update(upt, up)

    elif min == "5":
        login()


def create():

    global nilaiUlangan
    name = input("\nMasukkan Nama : ")
    uas = input("\nMasukkan UAS : ")
    ula = int(input("Masukkan jumlah ulangan: "))
    if ula <= 3:
        total = 0
        lis = []

        for i in range(ula):
            nilai = input("Nilai : ")

            if nilai:
                lis.insert(-1, nilai)
                total += i

            convert = list(map(int, lis))
            nilaiUlangan = reduce(lambda x, y: x + y, convert)


    else:
        print("Inputan Melebihi Max")

    hasil = (float(uas) + float(nilaiUlangan)) / 2

    if name and uas and ula:
        arr_data.insert(0,
                        ["{ " + "Nama : " + name, "Ujian : " + format(nilaiUlangan) + ", Uas : " + uas + ", Hasil : " + format(hasil) + " }"])
        check()
        admin()
    else:
        print("Data kosong")
        login()


def read():
    print("")
    no = 0
    for i in arr_data:
        C = list(map(lambda x: f"ID : {no} " + x, " "))
        print(C, i)
        no += 1

def check():
    even_numbers_iterator = filter(read(), "")
    even_numbers = list(even_numbers_iterator)

    print(even_numbers)



# Delete ---------------------
def hapus(dlt):
    s = 0
    if s >= len(arr_data[0]):
        print("Tidak ada")
        user()
    else:
        del arr_data[dlt]
    sukses()

def sukses():
    print("Berhasil di hapus")
    admin()

def delete(x, y):
    return x(y)

# Edit ---------------------
def update(x, y):
    return x(y)

def upt(up):
    global nilaiUlangan
    x = 0

    if x >= len(arr_data[0]):
        print("Tidak ada")
        admin()
    else:
        print("Edit Data Siswa & Nilai")
        name = input("\nMasukkan Edit Nama : ")
        uas = input("\nMasukkan Edit UAS : ")
        ula = int(input("Masukkan Jumlah Ulangan (Edit): "))
        if ula <= 3:
            total = 0
            lis = []
            for i in range(ula):
                nilai = input("Edit Nilai : ")

                if nilai:
                    lis.insert(-1, nilai)
                    total += i

                convert = list(map(int, lis))
                nilaiUlangan = reduce(lambda x, y: x + y, convert)


        else:
            print("Inputan Melebihi Max")
        hasil = (float(uas) + float(nilaiUlangan)) / 2

        for i in range(len(arr_data)):
            if arr_data.pop(up)[0][up]:
                if name and uas and ula:
                    arr_data.insert(0,
                                    ["{ " + "Nama : " + name,
                                     "Ujian : " + format(nilaiUlangan) + ", Uas : " + uas + ", Hasil : " + format(
                                         hasil) + " }"])
                    admin()

# -----------USER
def user():
    ser = input("\n"
                "1. Info Nilai \n"
                "2. Logout \n"
                "Masukkan Inputan: ")
    if ser == "1":
        read()
    elif ser == "2":
        login()


arr_data = []
login()



