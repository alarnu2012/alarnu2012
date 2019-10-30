import random
#------------------------------------------------------------
i=0
grupoAf=[]
grupoBf=[]
tabla  =[]
tablaux=[]
grupoAx=[]
grupoBx=[]
#------------------------------------------------------------
while i < 8 :
    equipos = str(input('Ingrese Equipo posicion Nro. : ' + str(i+1) + ': ' ))
    tablaux.append(equipos.upper())

    if i==0:
        grupoAf.append(tablaux[i])
    else:
        if i== 1:
            grupoBf.append(tablaux[i])
        else:
            tabla.append(tablaux[i])        
    
    i=i+1
#------------------------------------------------------------    
while True:
    1
    i=1
    grupoAf=[]
    grupoBf=[]    
    grupoAx=[]
    grupoBx=[]
    grupoAf.append(tablaux[0])
    grupoBf.append(tablaux[1])
    while i <= 6:
        if  (i%2 != 0):
            digito = random.randint(1,2)
            if digito == 1:
                grupoAx.append(i)
            else:
                grupoBx.append(i)                     
        else:
            if digito == 1:
                grupoBx.append(i)
                digito = 2
            else:
                grupoAx.append(i)
                digito = 1
        i = i + 1        
    #------------------------------------------------------------
    x=0
    ind = len(grupoAx)
    while x < ind:    
        pos = (grupoAx[x])    
        grupoAf.append(tabla[pos-1])
        pos = (grupoBx[x])    
        grupoBf.append(tabla[pos-1])    
        x=x+1
    #------------------------------------------------------------
    print  ('====================================================================================')
    print  ('====================================================================================')
    print ('Equipos: ' + str(tablaux))     
    print ('Grupo A: ' + str(grupoAf))
    print ('Grupo B: ' + str(grupoBf))
    print  ('====================================================================================')
    print  ('====================================================================================')
    
    simular = input('Desea realizar otra simulación Si o No ? = ')
    if simular.upper() == 'N':
        break
print ('Fin')    
    

  
