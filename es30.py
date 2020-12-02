c = 1
numero = []
potenza = 2
lungcifra = int(input("Da quante cifre è composto un numero binario?"))
print("Le cifre 0 o 1 vanno inserite da dastra")
cifra = int(input("Inserisci cifra: "))
if cifra == 1:
    prodotto = cifra
    numero.append(prodotto)
while True:
    if c == lungcifra:
        break
    else:  
        cifra = int(input("Inserisci cifra successiva: "))
        c = c + 1
        if cifra == 1:
            prodotto = cifra*potenza
            numero.append(prodotto)
        potenza = potenza*2
print("Il numero binario che hai inserito in numero decimale è", sum(numero)) 