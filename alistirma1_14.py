liste1=[]
for i in range(1,121213):
    for j in range(1,121213):
        if i*j == 121212 and (i>=j):
            liste1.append(i-j)
            liste1.sort()
            if liste1[0]== i-j :
                print(i, j)
