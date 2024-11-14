import math

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2*(base+altura)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura)/2
    perimetro = lado1 + lado2+ lado3
    return area, perimetro


def esfera(radio):
    volumen = (4/3)*math.pi*radio**3
    return volumen

def menu():
    print("Guten morgen, bienvenido a python con funciones")
    print ("Choose an option:")
    print("A.- Area y Perimetro del Rectangulo")
    print("B.- Area y Perimetro del Triangulo")
    print("C.- Volumen de la esfera")

#programa

menu()
opcion = input("Itroduce la opcion a desear: ").upper()

if opcion == "A":
    base = float (input("Introduce la base: "))
    altura = float (input("Introduce la altura: "))
    area, perimetro = rectangulo(base, altura)
    print("El area es de: ", area)
    print("El perimetro es de: ", perimetro)
    
elif opcion == "B":
    base = float (input("Introduce la base: "))
    altura = float (input("Introduce la altura: "))
    lado1 = float (input("Introduce el valor del lado 1: "))
    lado2 = float (input("Introduce el valor del lado 2: "))
    lado3 = float (input("Introduce el valor del lado 3: "))
    area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
    print("El area es de: ", area)
    print("El perimetro es de: ", perimetro)

elif opcion == "C":
    radio = float (input("Introduce el radio: "))
    volumen = esfera(radio)
    print ("El volumen es de: ", volumen)

else:
    print ("Opcion no valida.")

#Ejercicio deberan convertir un numero decimal en binario y de binario en decimal

binario = str()

