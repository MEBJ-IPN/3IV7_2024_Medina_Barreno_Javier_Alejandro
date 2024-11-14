import tkinter as tk
from tkinter import messagebox, simpledialog

import os

ARCHIVO = "alumnos.txt"

alumnos = []


def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 6:
                    boleta = partes[0]
                    nombre = partes[1]
                    apellido_paterno = partes[2]
                    apellido_materno = partes[3]
                    fecha_nacimiento = partes[4]
                    calificaciones  = list(map(float, partes[5:]))
                    alumno = {
                        "boleta" : boleta,
                        "nombre" : nombre,
                        "apellido_paterno" : appat,
                        "apellido_materno" : apmat,
                        "fecha_nacimiento" : fecnac,
                        "calificaciones" : calificaciones
                    }
                    alumnos.append(alumno)

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for alumno in alumnos:
            f.write(f"{alumno['boleta']},{alumno['nombre']},{alumno['apellido_paterno']},{alumno['apellido_materno']},{alumno['fecha_nacimiento']}, {','.join(map(str,alumno['calificaciones']))}\n")

def registrar_alumno():
    boleta = simpledialog.askstring("Entrada","Ingresa la boleta del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    appat = input("Ingresa el apellido paterno del alumno: ")
    apmat = input("Ingresa el apellido materno del alumno: ")
    fecnac = input("Ingresa la fecha de nacimiento(dd/mm/aaaa) del alumno: ")

    calificaciones = []
    for i in range(1,4):
        calificacionparcial = float(input("Ingrese la calificacion del parcial: "))
        calificaciones.append(calificacionparcial)

    alumno = {
        "boleta" : boleta,
        "nombre" : nombre,
        "apellido_paterno" : appat,
        "apellido_materno" : apmat,
        "fecha_nacimiento" : fecnac,
        "calificaciones" : calificaciones
    }

    alumnos.append(alumno)
    guardar_datos()
    messagebox.showinfo("Exito", "Alumno registrado exitosamente")

def consultar_alumnos() :
    if not alumnos :
        print("No hay registros solo juguito contigo")
    else :
        print("Lista de Alumnos: \n")
        for alumno in alumnos :
            print(f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']}{alumno['apellido_paterno']}{alumno['apellido_materno']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Calificaciones: {alumno['calificaciones']} \n" )

def editar_alumno() :
    boleta = input("Ingrese la boleta del alumnos que desea editar: ")
    for alumno in alumnos :
        if alumno['boleta'] == boleta :
            alumno['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para mantener el actual:") or alumno['nombre']
            alumno['apellido_paterno'] = input("Ingresa el nuevo apellido paterno o presiona Enter para mantener el actual:") or alumno['apellido_paterno']
            alumno['apellido_materno'] = input("Ingresa el nuevo apellido materno o presiona Enter para mantener el actual:") or alumno['apellido_materno']
            alumno['fecha_nacimiento'] = input("Ingresa la nueva fecha de nacimiento o presiona Enter para mantener el actual:") or alumno['fecha_nacimiento']
            for i in range(3) :
                nueva_calificacion = input("Ingresa ela nueva calificacion o presiona Enter para mantener el actual:")
                if nueva_calificacion: 
                    alumno['calificaciones'][i] = float(nueva_calificacion)
    return
    print("No hay mas alumnos")

def eliminar_alumno():
    print("esto es parte del examen")

def main() :
    while True:
        print("Menu de Gestión de Proximos Extras")
        print("1.- Registrar Alumno")
        print("2.- Consultar lista de Alumnos")
        print("3.- Editar Alumno")
        print("4.- Eliminar Alumno")
        print("5.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1" :
            registrar_alumno()
        elif opcion == "2" :
            consultar_alumnos()
        elif opcion == "3" :
            editar_alumno()
        elif opcion == "4" :
            eliminar_alumno()
        elif opcion == "5" :
            print("Ayos")
            break
        else : 
            print("opcion no valida")
main()
