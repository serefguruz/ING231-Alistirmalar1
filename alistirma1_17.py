girdi=int(input("Sayı giriniz  >>  "))
if len(str(girdi))==3:
    if str(girdi)[0]==str(girdi)[2]:
        print("Bu bir palindromik sayıdır.")
    else:
        print("Bu bir palindromik sayı değildir.")
elif len(str(girdi))==4:
    if str(girdi)[0]==str(girdi)[3]and str(girdi)[1]==str(girdi)[2]:
        print("Bu bir palindromik sayıdır.")
    else:
        print("Bu bir palindromik sayı değildir.")
else:
    print("Lütfen 3 ve 4 basamaklı sayı girin!")

