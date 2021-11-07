toplam=0
for i in range(10000,100000):
    i=str(i)
    if i[0]+i[1]==i[3]+i[4]:
        toplam+=1
print(toplam)
