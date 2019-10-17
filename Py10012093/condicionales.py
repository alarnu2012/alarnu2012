import random
'''
#------------------------------------------------------- 
numero = int(input('Ingrese un numero :'))
if numero % 2 == 0:
    print("El numero es multiplo de 2")
elif numero % 3 ==0:
    print("El numero es multiplo de 3")
elif numero % 4 ==0:
    print("El numero es multiplo de 4")
elif numero % 5 ==0:
    print("El numero es multiplo de 5")
else:
   print("Elnumero no es multiplo de los anteriores")
#------------------------------------------------------- 
dia = int(input('Ingrese un numero de la semana:'))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Lunes")
elif dia == 3:
    print("Martes")
elif dia == 4:
    print("Miercoles")
elif dia == 5:
    print("Jueves")
elif dia == 6:
    print("Viernes")
elif dia == 7:
    print("Sabado")        
else:
   print("Ingrese un n umero de 1 a 7")
#-------------------------------------------------------
dia = int(input('Ingrese un numero de la semana:'))
dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
if dia < 1 or dia > 7:
    print("No es un dias valido")
else:
    print("El numero corresponde a " + dias[numero-1])
#-------------------------------------------------------
n1 = int(input("Ingrese Nro 1"))
n2 = int(input("Ingrese Nro 2"))
n3 = int(input("Ingrese Nro 1"))              
if n1 < n2 < n3:
     print('Fueron Ingresados Ascendentemente')
else:
    print('No fueron ingresados Ascendentemente')
#-------------------------------------------------------
conjunto = ['a','e','i','o','u']
char = input('Ingrese un caracter:')
if char in conjunto:
    print("es una vocal")
else:
    print("No es una vocal")
#-------------------------------------------------------  
palabra = input("Ingrese una Palabra : ")
caracter= input("Ingrese una caracter: ")
if caracter in palabra:
    print("El caractar si esta")
else:
    print("El caractar no esta")
#-------------------------------------------------------  
numero = int(input('ingrese un numero : '))
cont=0
while cont <= numero:  
    print (cont)
    cont +=1
#-------------------------------------------------------    
numero = int(input('ingrese un numero : '))
for i in range(numero + 1):
  print (i)
#-------------------------------------------------------     
conjunto = ['a','e','i','o','u']
for c in conjunto:
   print (c) 
cont = 0    
while cont < len(conjunto):  
    print(conjunto[cont])
    cont +=1
#-------------------------------------------------------'''
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
