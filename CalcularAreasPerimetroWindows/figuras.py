from punto import *
from math import pi

class Figura():
    def __init__(self,p1,p2):
        self.origen = p1
        self.destino = p2
        self.area = 0
        self.perimetro = 0
        
        

class Cuadrado(Figura):
    def calcular_(self):
        lado = self.origen.calcular_distancia(self.destino)
        self.area = lado * lado
        self.perimetro = lado * 4
        

class Circulo(Figura):
    def calcular_(self):
        radio = self.origen.calcular_distancia(self.destino)
        self.area = pi * (radio ** 2)
        self.perimetro  = 2 * pi  *  radio 
        

class Triangulo(Figura):
    def calcular_(self):
        temporal  = Punto(self.origen.x,self.destino.y)
        b = temporal.calcular_distancia(self.origen)
        a = temporal.calcular_distancia(self.destino)
        h = self.origen.calcular_distancia(self.destino)
        self.area = b * a / 2
        self.perimetro = a + b + h
    
            
        
class Rectangulo(Figura):
    def calcular_(self):
        temporal  = Punto(self.origen.x,self.destino.y)
        b = temporal.calcular_distancia(self.origen)
        a = temporal.calcular_distancia(self.destino)
        self.area = b * a
        self.perimetro = ( b * a) * 2
         
