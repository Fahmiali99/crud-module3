data1 = ["21 hari 20 jam 9 menit 20 detik",
         "19 hari 14 jam 0 menit 13 detik",
         "1 hari 1 jam 1 menit 1 detik"]

data2 = ["3 minggu 3 hari 7 jam 21 menit",
         "5 minggu 5 hari 8 jam 11 menit",
         "7 minggu 1 hari 5 jam 33 menit"]


def dataSatu():
    time = []

    arr_days = []
    arr_hours = []
    arr_minutes = []
    arr_detik = []
    for sentence in data1:
        time.append(sentence.strip().split(' '))

    # print(time)
    # Days
    day1 = int(time[0][0])
    day2 = int(time[1][0])
    day3 = int(time[2][0])

    # Hours
    jam1 = int(time[0][2])
    jam2 = int(time[1][2])
    jam3 = int(time[2][2])

    # Minutes
    menit1 = int(time[0][4])
    menit2 = int(time[1][4])
    menit3 = int(time[2][4])

    # Seconds
    detik1 = int(time[0][6])
    detik2 = int(time[1][6])
    detik3 = int(time[2][6])


    # Rumus
    total_hari = day1 + day2 + day3
    total_jam = jam1 + jam2 + jam3
    total_menit = menit1 + menit2 + menit3
    total_detik = detik1 + detik2 + detik3

    #Get
    arr_days.append(total_hari)
    arr_hours.append(total_jam)
    arr_minutes.append(total_menit)
    arr_detik.append(total_detik)

    #Jumlahkan
    convert_day = sum(arr_days)
    convert_jam = sum(arr_hours)
    convert_menit = sum(arr_minutes)
    convert_detik = sum(arr_detik)


    #Convert
    hari = convert_day * 1440
    jam = convert_jam * 60
    menit = convert_menit
    detik = convert_detik * 0.0166667

    print("\n========== Data 1 ==========")
    print([hari, jam, menit, detik])

def dataDua():
    time = []

    arr_weeks = []
    arr_days = []
    arr_hours = []
    arr_minutes =[]

    for sentence in data2:
        time.append(sentence.strip().split(' '))

    #Weeks
    minggu1 = int(time[0][0])
    minggu2 = int(time[1][0])
    minggu3 = int(time[2][0])

    # Days
    day1 = int(time[0][2])
    day2 = int(time[1][2])
    day3 = int(time[2][2])

    # Hours
    jam1 = int(time[0][4])
    jam2 = int(time[1][4])
    jam3 = int(time[2][4])

    # Minutes
    menit1 = int(time[0][6])
    menit2 = int(time[1][6])
    menit3 = int(time[2][6])

    # Rumus
    total_minggu = minggu1 + minggu2 + minggu3
    total_hari = day1 + day2 + day3
    total_jam = jam1 + jam2 + jam3
    total_menit = menit1 + menit2 + menit3

    # Get
    arr_weeks.append(total_minggu)
    arr_days.append(total_hari)
    arr_hours.append(total_jam)
    arr_minutes.append(total_menit)

    # Jumlahkan
    convert_minggu = sum(arr_weeks)
    convert_day = sum(arr_days)
    convert_jam = sum(arr_hours)
    convert_menit = sum(arr_minutes)

    # Convert
    minggu = convert_minggu * 10080
    hari = convert_day * 1440
    jam = convert_jam * 60
    menit = convert_menit

    print("\n========== Data 2 ==========")
    print([minggu, hari, jam, menit])


def run():
    dataSatu()
    dataDua()


run()

