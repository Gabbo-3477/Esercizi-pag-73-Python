cifre = []
resti = []
convert = -1
numero = int(input("Inserisci numero da convertire in binario:"))
a = numero
while True:
    if numero == 0:
        break
    else:     
        resto = numero % 2
        resti.append(resto)        
        numero = numero//2
resti.reverse()
restitot = len(resti)-1
while True:    
    potenza = pow(10, restitot)
    cifra = resti[convert +1] * potenza
    restitot = restitot - 1 
    convert = convert + 1
    cifre.append(cifra)
    if restitot == -1:
        break
numerobinario = sum(cifre)
print("Il numeroecimale ",a,"in numero binario è",numerobinario)    
