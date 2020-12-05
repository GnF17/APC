a = open(input(), 'r')
arquivo = a.readlines()
x = 0
if arquivo[0].strip()=="P1":
    for i in range (1,len(arquivo)):
        if arquivo[i][0]=="#" or arquivo[i][0]!="0" and arquivo[i][0]!="1":
            continue
        else:
            x+=arquivo[i].count('1')
elif arquivo[0].strip()=="P2":
    j = 0
    while arquivo[j][0]=="#":
        j+=1
    max_value = int(int(arquivo[j+3])/2)
    for i in range (j+4,len(arquivo)):
        try:
            arq = arquivo[i].split('  ')
            arq[-1] = arq[-1].strip()
            for y in range (len(arq)):
                try:
                    if int(arq[y].strip())>max_value:
                        x+=1
                except:
                    ar = arq[y].split(" ")
                    for b in range (len(ar)):
                        if int(ar[b].strip())>max_value:
                            x+=1
        except:
            continue
else:
    aux = 0
    s = 0
    i = -1
    while i<(len(arquivo)-2):
        i+=1
        if arquivo[i][0]!="#" and aux<=2:
            #print(i)
            aux+=1
            if aux==3:
                max_value = int(int(arquivo[i])/2)
        elif arquivo[i][0]=="#":
            continue
        else:
            arq = []
            for y in range (0,len(arquivo[i]),4):
                arq.append(arquivo[i][y:y+4].strip())
            if arq[0]=="#":
                continue
            elif len(arq)<3:
                if int((int(arquivo[i])+int(arquivo[i+1])+int(arquivo[i+2]))/3)>max_value:
                    x+=1
                i+=2
                #print("esse ",i)
            elif int((int(arq[0])+int(arq[1])+int(arq[2]))/3)>max_value and len(arq)>=3:
                x+=1
print(x)
a.close()
