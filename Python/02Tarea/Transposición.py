def ingresar_matriz(tamaño):
    matriz = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            valor = float(input(f"Elemento [{i+1}],[{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def transponer3x3(matriz):
    matriz_trans = []
    for j in range(3):
        fila = []
        for i in range(3):
            fila.append(matriz[i][j])
        matriz_trans.append(fila)
    return matriz_trans

def transponer5x5(matriz):
    matriz_trans = []
    for j in range(5):
        fila = []
        for i in range(5):
            fila.append(matriz[i][j])
        matriz_trans.append(fila)
    return matriz_trans

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    while True:
        print("Qué se desea hacer?")
        print("1- Ingresar matriz 3x3")
        print("2- Ingresar matriz 5x5")
        print("3- Salir")

        opcion = input("Seleccionar lo deseado: ")

        if opcion == "1":
            matriz3x3 = ingresar_matriz(3)
            mtrans3x3 = transponer3x3(matriz3x3)
            
            print("Matriz original 3x3: ")
            imprimir_matriz(matriz3x3)
            print("Matriz transpuesta 3x3: ")
            imprimir_matriz(mtrans3x3)

        elif opcion == "2":
            matriz5x5 = ingresar_matriz(5)
            mtrans5x5 = transponer5x5(matriz5x5)
            
            print("Matriz original 5x5: ")
            imprimir_matriz(matriz5x5)
            print("Matriz transpuesta 5x5: ")
            imprimir_matriz(mtrans5x5)

        elif opcion == "3":
            print("Fin")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

main()
