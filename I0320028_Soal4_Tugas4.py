usia = 21
x = int(input("Berapa usia anda : "))
if usia <= x :
    print("Anda memenuhi syarat usia")
    y = str(input("Apakah anda sudah lulus ujian kualifikasi (Y/T) ?"))
    if y == "Y" :
        print("Anda dapat mendaftar di kursus")
    elif y == "T" :
        print("Anda tidak dapat mendaftar di kursus")

else:
    print("Anda tidak memenuhi syarat usia")