girdi=int(input("Sayı giriniz  >>  " ))

for b in range(2,girdi):
    if girdi%b== 0:
        print("Asal sayı değildir")
        break
else:
    print("Asal sayıdır")
