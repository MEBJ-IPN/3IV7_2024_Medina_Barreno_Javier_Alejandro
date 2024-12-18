import tkinter as tk
from tkinter import messagebox, simpledialog
import os

campeones = []

def cargar_datos():
    if os.path.exists("champs.txt"):
        with open("champs.txt", "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 9:
                    nombre = partes[0]
                    clase = partes[1]
                    precio_azul = partes[2]
                    precio_rp = partes[3]
                    total_hp = partes[4]
                    recurso = partes[5]
                    tipo_rango = partes[6]
                    fecha_lanzamiento = partes[7]
                    habilidades = partes[8:]
                    campeon = {
                        "nombre": nombre,
                        "clase": clase,
                        "precio_azul": precio_azul,
                        "precio_rp": precio_rp,
                        "total_hp": total_hp,
                        "recurso": recurso,
                        "tipo_rango": tipo_rango,
                        "fecha_lanzamiento": fecha_lanzamiento,
                        "habilidades": habilidades
                    }
                    campeones.append(campeon)

def guardar_datos():
    with open("champs.txt", "w") as f:
        for campeon in campeones:
            f.write(f"{campeon['nombre']},{campeon['clase']},{campeon['precio_azul']},{campeon['precio_rp']},{campeon['total_hp']},{campeon['recurso']},{campeon['tipo_rango']},{campeon['fecha_lanzamiento']},{','.join(campeon['habilidades'])}\n")

def registrar_campeon():
    nombre = simpledialog.askstring("Entrada", "Ingresa el nombre del campeón: ")
    clase = simpledialog.askstring("Entrada", "Ingresa la clase del campeón: ")
    pa = simpledialog.askstring("Entrada", "Ingresa el precio en esencia azul del campeón: ")
    rp = simpledialog.askstring("Entrada", "Ingresa el precio en RP del campeón: ")
    hp = simpledialog.askstring("Entrada", "Ingresa HP total del campeón: ")
    recurso = simpledialog.askstring("Entrada", "Ingresa el tipo de recurso que utiliza el campeón: ")
    tpr = simpledialog.askstring("Entrada", "Ingresa el tipo de rango del campeón: ")
    flz = simpledialog.askstring("Entrada", "Ingresa la fecha de lanzamiento del campeón (dd/mm/aaaa): ")

    habilidades = []
    for i in range(1, 6):
        habilidad = simpledialog.askstring("Entrada", f"Ingrese la habilidad {i} del campeón:")
        habilidades.append(habilidad)

    campeon = {
        "nombre": nombre,
        "clase": clase,
        "precio_azul": pa,
        "precio_rp": rp,
        "total_hp": hp,
        "recurso": recurso,
        "tipo_rango": tpr,
        "fecha_lanzamiento": flz,
        "habilidades": habilidades
    }
    campeones.append(campeon)
    guardar_datos()
    messagebox.showinfo("Éxito", "Campeón registrado exitosamente")

def consultar_campeon():
    if not campeones:
        messagebox.showinfo("Consulta", "No hay campeones registrados")
    else:
        # Scrollbar hecha por ChatGPT :D
        consultar_window = tk.Toplevel()
        consultar_window.title("Consulta de Campeones")
        
        text_area = tk.Text(consultar_window, width=80, height=20, wrap=tk.WORD, font=("Arial", 12))
        text_area.pack(padx=10, pady=10)

        scrollbar = tk.Scrollbar(consultar_window, orient=tk.VERTICAL, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        info = "Lista de Campeones:\n\n"
        for campeon in campeones:
            info += f"Nombre: {campeon['nombre']}, Clase: {campeon['clase']}, Precio Esencia Azul: {campeon['precio_azul']}, Precio RP: {campeon['precio_rp']}, Total HP: {campeon['total_hp']}, Recurso: {campeon['recurso']}, Tipo de Rango: {campeon['tipo_rango']}, Fecha de Lanzamiento: {campeon['fecha_lanzamiento']}, Habilidades: {', '.join(campeon['habilidades'])}\n\n"

        text_area.insert(tk.END, info)
        text_area.config(state=tk.DISABLED)

def editar_campeon():
    nombre = simpledialog.askstring("Entrada", "Ingrese el nombre del campeón que desea editar: ")
    for campeon in campeones:
        if campeon['nombre'] == nombre:
            campeon['clase'] = simpledialog.askstring("Entrada", "Ingresa la nueva clase o deja en blanco para mantener:", initialvalue=campeon['clase']) or campeon['clase']
            campeon['precio_azul'] = simpledialog.askstring("Entrada", "Ingresa el nuevo precio en Esencia Azul o deja en blanco:", initialvalue=campeon['precio_azul']) or campeon['precio_azul']
            campeon['precio_rp'] = simpledialog.askstring("Entrada", "Ingresa el nuevo precio en RP o deja en blanco:", initialvalue=campeon['precio_rp']) or campeon['precio_rp']
            campeon['total_hp'] = simpledialog.askstring("Entrada", "Ingresa la nueva HP o deja en blanco:", initialvalue=campeon['total_hp']) or campeon['total_hp']
            campeon['recurso'] = simpledialog.askstring("Entrada", "Ingresa el nuevo recurso o deja en blanco:", initialvalue=campeon['recurso']) or campeon['recurso']
            campeon['tipo_rango'] = simpledialog.askstring("Entrada", "Ingresa el nuevo tipo de rango o deja en blanco:", initialvalue=campeon['tipo_rango']) or campeon['tipo_rango']
            campeon['fecha_lanzamiento'] = simpledialog.askstring("Entrada", "Ingresa la nueva fecha de lanzamiento o deja en blanco:", initialvalue=campeon['fecha_lanzamiento']) or campeon['fecha_lanzamiento']
            for i in range(5):
                nueva_habilidad = simpledialog.askstring("Entrada", f"Ingrese la nueva habilidad {i+1} o deja en blanco para mantener:", initialvalue=campeon['habilidades'][i])
                if nueva_habilidad:
                    campeon['habilidades'][i] = nueva_habilidad
            guardar_datos()
            messagebox.showinfo("Éxito", "Campeón editado exitosamente")
            return
    messagebox.showinfo("Error", "Campeón no encontrado")

def eliminar_campeon():
    nombre = simpledialog.askstring("Entrada", "Ingrese el nombre del campeón que desea eliminar: ")
    for campeon in campeones:
        if campeon['nombre'] == nombre:
            campeones.remove(campeon)
            guardar_datos()
            messagebox.showinfo("Éxito", "Campeón eliminado exitosamente")
            return
    messagebox.showinfo("Error", "Campeón no encontrado")

def main():
    cargar_datos()
    
    root = tk.Tk()
    root.title("Gestión de Campeones")
    
    root.config(bg='#0e1b29') 
    root.geometry("300x400")  

    button_style = {
        'width': 20,
        'height': 2,
        'font': ('Arial', 12),
        'bg': '#1f3042',
        'fg': '#FFD700',  
        'activebackground': '#6c8ebf',  
        'activeforeground': 'white',  
        'relief': 'solid',
        'bd': 2
    }

    tk.Button(root, text="Registrar Campeón", command=registrar_campeon, **button_style).pack(pady=10)
    tk.Button(root, text="Consultar Campeones", command=consultar_campeon, **button_style).pack(pady=10)
    tk.Button(root, text="Editar Campeón", command=editar_campeon, **button_style).pack(pady=10)
    tk.Button(root, text="Eliminar Campeón", command=eliminar_campeon, **button_style).pack(pady=10)
    tk.Button(root, text="Salir", command=root.quit, **button_style).pack(pady=10)

    root.mainloop()

main()
