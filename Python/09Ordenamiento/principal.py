import ordenamiento
import vista

def main():
    logica_ordenamiento = {
        "burbuja": ordenamiento.burbuja,
        "seleccion": ordenamiento.seleccion_sort,
        "insercion": ordenamiento.insercion,
        "merge_sort": ordenamiento.merge_sort,
        "quick_sort": ordenamiento.quick_sort,
    }

    vista.crear_interfaz(logica_ordenamiento)

