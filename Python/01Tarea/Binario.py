def binario_decimal():
    binario = input("Ingresar el número binario: ")
    decimal = 0
    longitud_binario = len(binario)
    
    for i in range(longitud_binario):
        digito = int(binario[longitud_binario - 1 - i])
        decimal += digito * (2 ** i)

    print(f"{decimal} en binario es: {binario}")

def decimal_binario():
    decimal_b = int(input("Ingresar el número decimal: "))
    if decimal_b == 0:
        print(f"0 en decimal es 0")
        return

    binario_d = ""
    while decimal_b > 0:
        binario_d = str(decimal_b % 2) + binario_d
        decimal_b = decimal_b // 2

    print(f"{decimal_b} como binario es {binario_d}")

def main():
    while True:
        print("Seleccionar lo deseado: ")
        print("1- Conversión de Binario a Decimal")
        print("2- Conversion de Decimal a Binario")
        print("3- Salir")

        opcion = input("Seleccione lo deseado: ")

        if opcion == "1":
            binario_decimal()

        elif opcion == "2":
            decimal_binario()

        elif opcion == "3":
            print("Fin")
            break

        else: 
            print("Opcion no valida")

main()
