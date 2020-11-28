a = open(input(), 'r')
arquivo = a.readlines()
x = 0
if arquivo[0].strip()=="P1":
    print("P1")
    for i in range (1,len(arquivo)):
        if arquivo[i][0]=="#" or arquivo[i][0]!="0" and arquivo[i][0]!="1":
            continue
        else:
            x+=arquivo[i].count('1')
    print(x)
elif arquivo[0].strip()=="P2":
    print("P2")
    j = 0
    while arquivo[j][0]=="#":
        j+=1
    max_value = int(int(arquivo[j+3])/2)
    #print(int(max_value))
    for i in range (j+4,len(arquivo)):
        try:
            arq = arquivo[i].split('  ')
            arq[-1] = arq[-1].strip()
            #print(arq)
            for y in range (len(arq)):
                try:
                    if int(arq[y].strip())>max_value:
                        x+=1
                except:
                    ar = arq[y].split(" ")
                    #print(ar)
                    for b in range (len(ar)):
                        if int(ar[b].strip())>max_value:
                            x+=1
                #print(x)
        except:
            continue
else:
    print("P3") 
    j = 0         
    while arquivo[j][0]=="#":
        j+=1
    max_value = int(int(arquivo[j+3])/2)
    #print(int(max_value))
    '''for i in range (j+4,len(arquivo)):
        try:
            arq = arquivo[i].split('  ')
            arq[-1] = arq[-1].strip()
            #print(arq)
            for y in range (0,len(arq),3):
                try:
                    if ((int(arq[y].strip())+int(arq[y+1].strip)+int(arq[y+2].strip()))/3)>max_value:
                        x+=1
                except:
                    ar = arq[y].split(" ")
                    #print(ar)
                    for b in range (len(ar)):
                        if ((int(ar[b].strip())+int(arq[y+1].strip())+int(arq[y+2].strip()))/3)>max_value:
                            x+=1
                            y-=2
                #print(x)
        except:
            continue'''

print(x)
a.close()
