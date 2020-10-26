from datetime import date 

def tarefa1(qtd, data): #porcentagem de matriculados/formados e outras situacoes
    cursando=0
    outras=0
    for i in range (int(qtd)):
        if data[i][5]=="2" or data[i][5]=="6":
            cursando+=1
        elif data[i][5]!="2" and data[i][5]!="6":
            outras+=1
    #cursando=(cursando*100)/qtd
    #outras=(outras*100)/qtd
    print(f"matriculados ou formados:{(cursando*100)/qtd :5.1f}")
    print(f"alunos em outras situacoes:{(outras*100)/qtd :5.1f}")

def tarefa2(qtd, data): #porcentagem do sexo masculino e feminino
    feminino=0
    masculino=0
    for i in range (qtd):
        if data[i][4]=="1":
            feminino+=1
        elif data[i][4]!="1":
            masculino+=1
    #feminino=(feminino*100)/qtd
    #masculino=(masculino*100)/qtd
    print(f"sexo masculino:{(masculino*100)/qtd :5.1f}")
    print(f"sexo feminino:{(feminino*100)/qtd :5.1f}")

def tarefa3(qtd, data): #media de anos desde ingresso
    media = 0
    for i in range (qtd):
        if int(data[i][0])=="2018":
            media+=1
        elif int(data[i][0])!="2018" and int(data[i][0])!="2019": 
            media+=(2019-int(data[i][0]))
    print(f"media de anos desde ingresso:{media/qtd :5.1f}")

def tarefa4(qtd, data): #quantidade de nascidos em cada dia da semana
    segunda = 0
    terca = 0
    quarta = 0
    quinta = 0
    sexta = 0
    sabado = 0
    domingo = 0
    for i in range (qtd):
        if date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==0:
            segunda+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==1:
            terca+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==2:
            quarta+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==3:
            quinta+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==4:
            sexta+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==5:
            sabado+=1
        elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==6:
            domingo+=1
    print(f"domingo:{(domingo*100)/qtd :5.1f}")
    print(f"segunda:{(segunda*100)/qtd :5.1f}")
    print(f"terca:{(terca*100)/qtd :5.1f}")
    print(f"quarta:{(quarta*100)/qtd :5.1f}")
    print(f"quinta:{(quinta*100)/qtd :5.1f}")
    print(f"sexta:{(sexta*100)/qtd :5.1f}")
    print(f"sabado:{(sabado*100)/qtd :5.1f}")

def tarefa5(qtd, data): #porcentagem de matriculados/formados e outras situações baseado no sexo  
    femininoMatri = 0
    femininoOutras = 0
    masculinoMatri = 0
    masculinoOutras = 0
    feminino = 0
    masculino = 0
    for i in range (qtd):
        if data[i][4]=="1" and (data[i][5]=="2" or data[i][5]=="6"):
            femininoMatri+=1
            feminino+=1
        elif data[i][4]=="1" and (data[i][5]!="2" or data[i][5]!="6"):
            femininoOutras+=1
            feminino+=1
        elif data[i][4]!="1" and (data[i][5]=="2" or data[i][5]=="6"):
            masculinoMatri+=1
            masculino+=1
        elif data[i][4]!="1" and (data[i][5]!="2" or data[i][5]!="6"):
            masculinoOutras+=1
            masculino+=1
    
    print(f"dentre masculinos:\nmatriculados ou formados:{(masculinoMatri*100)/masculino :5.1f}\nalunos em outras situacoes:{(masculinoOutras*100)/masculino :5.1f}")
    print(f"dentre femininos:\nmatriculados ou formados:{(femininoMatri*100)/feminino :5.1f}\nalunos em outras situacoes:{(femininoOutras*100)/feminino :5.1f}")

def tarefa6(qtd, data): #tempo de curso separado em alunos regulares e não regulares
    mediaRegulares = 0
    mediaNaoRegulares = 0
    regulares = 0
    naoRegulares = 0
    for i in range (int(qtd)):
        if data[i][5]=="2" or data[i][5]=="6":
            regulares+=1
            if data[i][0]=="2018":
                mediaRegulares+=1
            elif data[i][0]!="2018" and data[i][0]!="2019":  
                mediaRegulares+=(2019-int(data[i][0]))
        elif data[i][5]!="2" and data[i][5]!="6":
            naoRegulares+=1
            if data[i][0]=="2018":
                mediaNaoRegulares+=1
            elif data[i][0]!="2018" and data[i][0]!="2019":  
                mediaNaoRegulares+=(2019-int(data[i][0]))
    if regulares==0:
        regulares = 1
    if naoRegulares==0:
        naoRegulares = 1
    print(f"entre matriculados ou formados:\nmedia de anos desde ingresso:{mediaRegulares/regulares :5.1f}\ndentre alunos em outras situacoes:\nmedia de anos desde ingresso:{mediaNaoRegulares/naoRegulares :5.1f}")

def tarefa7(qtd, data): #quantidade de nascidos em cada dia da semana de acordo com o sexo
    feminino = 0
    masculino = 0
    domingoF = 0
    segundaF = 0
    tercaF = 0
    quartaF = 0
    quintaF = 0
    sextaF = 0
    sabadoF = 0
    domingoM = 0
    segundaM = 0
    tercaM = 0
    quartaM = 0
    quintaM = 0
    sextaM = 0
    sabadoM = 0
    for i in range (qtd):
        if data[i][4]=="1":
            feminino+=1
            if date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==0:
                segundaF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==1:
                tercaF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==2:
                quartaF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==3:
                quintaF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==4:
                sextaF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==5:
                sabadoF+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==6:
                domingoF+=1
        elif data[i][4]!="1":
            masculino+=1
            if date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==0:
                segundaM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==1:
                tercaM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==2:
                quartaM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==3:
                quintaM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==4:
                sextaM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==5:
                sabadoM+=1
            elif date(year=int(data[i][3]), month=int(data[i][2]), day=int(data[i][1])).weekday()==6:
                domingoM+=1
    if masculino==0:
        masculino = 1
    if feminino==0:
        feminino = 1
    print(f"dentre masculinos:\ndomingo:{(domingoM*100)/masculino :5.1f}\nsegunda:{(segundaM*100)/masculino :5.1f}\nterca:{(tercaM*100)/masculino :5.1f}\nquarta:{(quartaM*100)/masculino :5.1f}\nquinta:{(quintaM*100)/masculino :5.1f}\nsexta:{(sextaM*100)/masculino :5.1f}\nsabado:{(sabadoM*100)/masculino :5.1f}")
    print(f"dentre femininos:\ndomingo:{(domingoF*100)/feminino :5.1f}\nsegunda:{(segundaF*100)/feminino :5.1f}\nterca:{(tercaF*100)/feminino :5.1f}\nquarta:{(quartaF*100)/feminino :5.1f}\nquinta:{(quintaF*100)/feminino :5.1f}\nsexta:{(sextaF*100)/feminino :5.1f}\nsabado:{(sabadoF*100)/feminino :5.1f}")

def dados(qtd): #armazenamento dos dados
    data = []
    for i in range (int(qtd)):
        data.append(input().split(" ")) #A lista data contem várias listas com os valores inseridos em cada linha (lista)
       #Para imprimir usar o índice: lista[numero da lista (referente a qtd de linhas inseridas)][posição dentro da segunda lista]
       #Ex.: data[0][2] -> terceiro valor da primeira lista
    
    #refazer com dicionário, talvez seja mais fácil
    '''if i<qtd:
        i++
        data.append(input().split(" ")) #adiciona os valores lidos em uma lista
        #Lista ou tupla
        data(qtd-1)'''
    return data

def optionInput(t): #armazenamento do número correspondente a escolha
    option = t
    return int(option) 
    #return global option

def qtdInput(n): #armazenamento do número correspondente a quantidade de linhas que serão inseridas
    qtd = n
    return int(qtd)
    #return global qtd

def switchOption(option, qtd, data): #escolha da opção de acordo com a entrada
    if option==1:
        tarefa1(qtd, data)
    if option==2:
        tarefa2(qtd, data)
    if option==3:
        tarefa3(qtd, data)
    if option==4:
        tarefa4(qtd, data)
    if option==5:
        tarefa5(qtd, data)
    if option==6:
        tarefa6(qtd, data)
    if option==7:
        tarefa7(qtd, data)

def init(): #inicializacao do programa
    option = optionInput(input())
    qtd = qtdInput(input())
    data = dados(qtd) # -> parametro tem que ser a qtd, mas precisa arrumar um jeito dela virar global
    switchOption(option, qtd, data)
    #switchOption(optionInput(input()))

init()