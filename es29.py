listan = []
listamax = []
listamin = []
listaesc = []
verifica = True
città = 0
tempmax = 0
tempmin = 0
tempesc = 0
print("Quant'è il valore dell'escursione termica da prefissare?")
valpref = int(input())

while verifica == True:
    città += 1
    tempmax += 1
    tempmin += 1
    tempesc += 0
    print("nome della città", città,"? ")
    nomi = input()
    listan.append(nomi)
    print("Qual'è la  temperatura massima registrata a", nomi,"? ")
    temp1 = int(input())
    listamax.append(temp1)
    print("Qual'è la  temperatura minima registrata a", nomi,"? ")
    temp2 = int(input())
    listamin.append(temp2)
    esctermica = temp1 - temp2
    if esctermica > valpref:
         listaesc.append(esctermica)
    else:
         pass
    numxuscire = int(input("Se hai concluso l'elenco digita 0, se vuoi continuare premi qualsiasi tasto: "))
    if numxuscire == 0:
        verifica = False
    else:
        pass
    listaesc.reverse()
print("Le escursioni massime prefissate sono:", listaesc[:])