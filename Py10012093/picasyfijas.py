import random
numero=[]
while len(numero) < 3:
   digito = random.randint(0,9)
   if digito not in numero:
         numero.append(digito)
print( numero)

while True:
    intento = input('Ingrese un numero de 3 digitos')
    usuario = []
    for i in intento:
        if int(i) not in usuario:
            usuario.append(int(i))
    if len(usuario) != len(numero):
        print("intento no valido")
    else:
        break
    
print (intento)


u=0
fijas=0
picas=0
while u < len(usuario):
    if numero[u] == usuario[u]:
        fijas +=1
    else:
        n=0
        while n < len(numero):
            if numero[n] == usuario[u]:
                 picas +=1
            n +=1
    u +=1


print (fijas)
print (picas)
