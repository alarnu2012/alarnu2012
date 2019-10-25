from figuras import *

p1 = Punto(0,5)
p2 = Punto(5,10)

cuadrado = Cuadrado(p1,p2)
circulo = Circulo(p1,p2)
triangulo = Triangulo(p1,p2)
rectangulo = Rectangulo(p1,p2)

cuadrado.calcular_()
circulo.calcular_()
triangulo.calcular_()
rectangulo.calcular_()

print ("Area del cuadrado - > " + str(cuadrado.area))
print ("Area del Circulo - > " + str(circulo.area))
print ("Area del Triangulo - > " + str(triangulo.area))
print ("Area del Rectangulo - > " + str(rectangulo.area))


print ("Perimetro del cuadrado - > " + str(cuadrado.perimetro))
print ("Perimetro del Circulo - > " + str(circulo.perimetro))
print ("Perimetro del Triangulo - > " + str(triangulo.perimetro))
print ("Perimetro del Rectangulo - > " + str(rectangulo.perimetro))


