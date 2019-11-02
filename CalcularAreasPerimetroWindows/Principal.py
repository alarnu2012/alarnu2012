from tkinter import *
from figuras import *


class AppFiguras:

    def calcular(self):
        valores_p1 = [int(x) for x in self.punto1.get().split(",")]
        valores_p2 = [int(x) for x in self.punto2.get().split(",")]

        p1 = Punto(valores_p1[0],valores_p1[1])
        p2 = Punto(valores_p2[0],valores_p2[1])
        cuadrado = Cuadrado(p1,p2)
        circulo = Circulo(p1,p2)
        triangulo = Triangulo(p1,p2)
        rectangulo = Rectangulo(p1,p2)
            
       
        print (self.variable.get())
        
        if self.variable.get() == 1:         
            cuadrado.calcular_()
            self.valor_area.set("Area : " + str(cuadrado.area))
            self.valor_perimetro.set("Perimetro = " + str(cuadrado.perimetro))
            
        if self.variable.get() == 2:
            circulo.calcular_()
            self.valor_area.set("Area : " + str(circulo.area))
            self.valor_perimetro.set("Perimetro = " + str(circulo.perimetro))
            
        if self.variable.get() == 3:
            triangulo.calcular_()
            self.valor_area.set("Area : " + str(triangulo.area))
            self.valor_perimetro.set("Perimetro = " + str(triangulo.perimetro))
    
        if self.variable.get() == 4:
            rectangulo.calcular_()
            self.valor_area.set("Area : " + str(rectangulo.area))
            self.valor_perimetro.set("Perimetro = " + str(rectangulo.perimetro))
   
            

    def __init__(self, myParent):

        self.frame = Frame(myParent)
        self.frame.pack()

        self.label1 = Label(self.frame, text="Ingrese Punto 1:")
        self.label1.grid(row=0, column=0)
        self.punto1 = StringVar(self.frame)
        self.entry1 = Entry(self.frame, textvariable=self.punto1)
        self.entry1.grid(row=0, column=1)

        self.label1 = Label(self.frame, text="Ingrese Punto 2:")
        self.label1.grid(row=1, column=0)
        self.punto2 = StringVar(self.frame)
        self.entry1 = Entry(self.frame, textvariable=self.punto2)
        self.entry1.grid(row=1, column=1)

        self.label1 = Label(self.frame, text="Seleccion Tipo de Grafica")
        self.label1.grid(row=8, column=8)

        self.variable = IntVar()
        
        self.opcfig1 = Radiobutton(text="Cuadrado", variable=self.variable, value=1,activebackground="#555555", activeforeground="#AAAAAA")
        self.opcfig2 = Radiobutton(text="Circulo", variable=self.variable, value=2,activebackground="#555555", activeforeground="#AAAAAA")
        self.opcfig3 = Radiobutton(text="Triangulo", variable=self.variable, value=3,activebackground="#555555", activeforeground="#AAAAAA")
        self.opcfig4 = Radiobutton(text="Rectangulo", variable=self.variable, value=4,activebackground="#555555", activeforeground="#AAAAAA")
        self.opcfig1.pack()
        self.opcfig2.pack()
        self.opcfig3.pack()
        self.opcfig4.pack()
 

        boton = Button(root, text="Calcular", command=self.calcular).pack()

        self.valor_area = StringVar()
        self.valor_area.set("Area : ")
        self.labelsalida1 = Label(self.frame, textvariable=self.valor_area)
        self.labelsalida1.grid(row=11, column=8)


        self.valor_perimetro = StringVar()
        self.valor_perimetro.set("Perimetro : ")
        self.labelsalida2 = Label(self.frame, textvariable=self.valor_perimetro) 
        self.labelsalida2.grid(row=12, column=8)





root = Tk()
app = AppFiguras(root)
root.geometry('500x500')
root.mainloop()
