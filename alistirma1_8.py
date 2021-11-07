adet=0
for i in range(100,999,2):
    if not(str(i)[0]!=str(i)[1]and str(i)[1]!=str(i)[2]and str(i)[0]!=str(i)[2]):
       adet+=1
print(adet)    
