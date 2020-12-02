lista1 = []
lista2 = []
verifica = True
studenti = 0
lanci = 0

while verifica == True:
    studenti += 1
    lanci += 1
    print("Nome persona ", studenti,"? ")
    nomi = input()
    lista.append(nomi)
    print("Lancio persona", studenti,"? ")
    lanci= int(input())
    lista2.append(lanci)
    interprog = int(input("Se vuoi interrompere il programma scrivi 0, se non vuoi interrompere il programma premi qualsiasi altro numero:"))
    if interprog == 0:
        verifica = False
    else:
        pass
    

lista2.reverse()

print("il lancio maggiore è", lista2[0])