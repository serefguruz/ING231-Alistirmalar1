for i in range(0,2005):
    i=str(i)
    rt=0
    for b in range(len(i)):
        rt = rt+ int(i[b])
    if rt == 2005 - int(i):
            print(i)
    
