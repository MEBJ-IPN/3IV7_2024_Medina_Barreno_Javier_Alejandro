import tkinter as tk
from tkinter import messagebox
import time

def crear_interfaz(logica_ordenamiento):
    def ordenar_burbuja():
        ordenar("burbuja")

    def ordenar_seleccion():
        ordenar("seleccion")

    def ordenar_insercion():
        ordenar("insercion")

    def ordenar_merge_sort():
        ordenar("merge_sort")

    def ordenar_quick_sort():
        ordenar("quick_sort")

    def ordenar(metodo):
        try:
            lista_original = list(map(int, entry_lista.get().split(',')))
            if len(lista_original) > 40:
                messagebox.showerror("Error", "La lista no debe contener más de 40 elementos.")
                return

            lista = lista_original[:]
            inicio = time.time()
            lista = logica_ordenamiento[metodo](lista)
            fin = time.time()

            tiempo = fin - inicio
            messagebox.showinfo("Resultados", f"Lista original: {lista_original}\n"
                                              f"Lista ordenada: {lista}\n"
                                              f"Tiempo de ejecución: {tiempo:.6f} segundos")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa una lista válida de números separados por comas.")

    ventana = tk.Tk()
    ventana.title("Ordenamiento de Listas")

    tk.Label(ventana, text="Ingresa una lista de números (separados por comas):").pack(pady=5)
    entry_lista = tk.Entry(ventana, width=50)
    entry_lista.pack(pady=5)

    tk.Label(ventana, text="Selecciona un método de ordenamiento:").pack(pady=5)

    tk.Button(ventana, text="Burbuja", command=ordenar_burbuja).pack(pady=5)
    tk.Button(ventana, text="Selección", command=ordenar_seleccion).pack(pady=5)
    tk.Button(ventana, text="Inserción", command=ordenar_insercion).pack(pady=5)
    tk.Button(ventana, text="Merge Sort", command=ordenar_merge_sort).pack(pady=5)
    tk.Button(ventana, text="Quick Sort", command=ordenar_quick_sort).pack(pady=5)

    ventana.mainloop()
