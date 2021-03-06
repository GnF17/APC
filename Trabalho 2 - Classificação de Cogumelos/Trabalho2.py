import math

d = 22
k = input()
nTrain, nTest = input().split(" ")
xTrain = []
yTrain = []
xTest = []
y = []
desvio_padrao = []


cap_shape = {"b":0, "c": 1, "x":2, "f":3, "k":4, "s":5}
cap_surface = {"f": 0, "g":1, "y":2, "s":3}
cap_color = {"n":0, "b":1, "c":2, "g":3, "r":4, "p":5, "u":6, "e":7, "w":8, "y":9}
bruises = {"t":0, "f":1}
odor = {"a":0, "l":1, "c":2, "y":3, "f":4, "m":5, "n":6, "p":7, "s":8}
gill_attachment = {"a":0, "d":1, "f":2, "n":3}
gill_spacing = {"c":0, "w":1, "d":2}
gill_size = {"b":0, "n":1}
gill_color = {"k":0, "n":1, "b":2, "h":3, "g":4, "r":5, "o":6, "p":7, "u":8, "e":9, "w":10, "y":11}
stalk_shape = {"e":0, "t":1}
stalk_root = {"b":0, "c":1, "u":2, "e":3, "z":4, "r":5, "?":6}
stalk_surface_above_ring = {"f":0, "y":1, "k":2, "s":3}
stalk_surface_below_ring = {"f":0, "y":1, "k":2, "s":3}
stalk_color_above_ring = {"n":0, "b":1, "c":2, "g":3, "o":4, "p":5, "e":6, "w":7, "y":8}
stalk_color_below_ring = {"n":0, "b":1, "c":2, "g":3, "o":4, "p":5, "e":6, "w":7, "y":8}
veil_typee = {"p":0, "u":1}
veil_color =  {"n":0, "o":1, "w":2, "y":3}
ring_number = {"n":0, "o":1, "t":2}
ring_typee = {"c":0, "e":1, "f":2, "l":3, "n":4, "p":5, "s":6, "z":7}
spore_print_color = {"k":0, "n":1, "b":2, "h":3, "r":4, "o":5, "u":6, "w":7, "y":8}
population = {"a":0, "c":1, "n":2, "s":3, "v":4, "y":5}
habitat = {"g":0, "l":1, "m":2, "p":3, "u":4, "w":5, "d":6}

def replace (x,y): 
    for i in cap_shape:
        if i==x[y][0]:
            x[y][0] = cap_shape.get(i,-1)
    for i in cap_surface:
        if i==x[y][1]:
            x[y][1] = cap_surface.get(i,-1)
    for i in cap_color:
        if i==x[y][2]:
            x[y][2] = cap_color.get(i,-1)
    for i in bruises:
        if i==x[y][3]:
            x[y][3] = bruises.get(i,-1)
    for i in odor:
        if i==x[y][4]:
            x[y][4] = odor.get(i,-1)
    for i in gill_attachment:
        if i==x[y][5]:
            x[y][5] = gill_attachment.get(i,-1)
    for i in gill_spacing:
        if i==x[y][6]:
            x[y][6] = gill_spacing.get(i,-1)
    for i in gill_size:
        if i==x[y][7]:
            x[y][7] = gill_size.get(i,-1)
    for i in gill_color:
        if i==x[y][8]:
            x[y][8] = gill_color.get(i,-1)
    for i in stalk_shape:
        if i==x[y][9]:
            x[y][9] = stalk_shape.get(i,-1)
    for i in stalk_root:
        if i==x[y][10]:
            x[y][10] = stalk_root.get(i,-1)
    for i in stalk_surface_above_ring:
        if i==x[y][11]:
            x[y][11] = stalk_surface_above_ring.get(i,-1)
    for i in stalk_surface_below_ring:
        if i==x[y][12]:
            x[y][12] = stalk_surface_below_ring.get(i,-1)
    for i in stalk_color_above_ring:
        if i==x[y][13]:
            x[y][13] = stalk_color_above_ring.get(i,-1)
    for i in stalk_color_below_ring:
        if i==x[y][14]:
            x[y][14] = stalk_color_below_ring.get(i,-1)
    for i in veil_typee:
        if i==x[y][15]:
            x[y][15] = veil_typee.get(i,-1)
    for i in veil_color:
        if i==x[y][16]:
            x[y][16] = veil_color.get(i,-1)
    for i in ring_number:
        if i==x[y][17]:
            x[y][17] = ring_number.get(i,-1)
    for i in ring_typee:
        if i==x[y][18]:
            x[y][18] = ring_typee.get(i,-1)
    for i in spore_print_color:
        if i==x[y][19]:
            x[y][19] = spore_print_color.get(i,-1)
    for i in population:
        if i==x[y][20]:
            x[y][20] = population.get(i,-1)
    for i in habitat:
        if i==x[y][21]:
            x[y][21] = habitat.get(i,-1)

def insertReplace (n, x):
    for y in range (int(n)):
        x.append(input().split(" "))
        replace(x,y)

insertReplace(nTrain,xTrain)

for i in range (22):
    media = 0
    for j in xTrain:
        media += j[i]
    y.append(media/int(nTrain))

for i in range (22):
    dp = 0
    for j in xTrain:
        dp += (j[i]-y[i])**2
    desvio_padrao.append(math.sqrt(dp/int(nTrain)))

for i in range (22):
    if desvio_padrao[i]==0:
        for j in xTrain:
            j[i] = 0
    else:
        for j in xTrain:
            j[i] = (j[i]-y[i])/desvio_padrao[i]

for i in range (int(nTrain)):
    yTrain.append(input())

insertReplace(int(nTest),xTest)

for i in range (22):
    if desvio_padrao[i]==0:
        for j in xTest:
            j[i] = 0
    else:
        for j in xTest:
            j[i] = (j[i]-y[i])/desvio_padrao[i]

def returnDis(x):
    return x["distancia"]

for z in xTest:
    dis = []
    qtdP = 0
    qtdE = 0

    for i in range (int(nTrain)):
        distancia = int(0) 

        for j in range (22):
            distancia += (xTrain[i][j]-z[j])**2
            
        dis.append({"distancia": math.sqrt(distancia), "rotulo": yTrain[i]})

    dis.sort(key=returnDis)
    
    for i in range (int(k)):
        if dis[i]["rotulo"]=="p":
            qtdP+=1
        else:
            qtdE+=1

    if qtdE>qtdP:
        print("e")
    else:
        print("p")  
