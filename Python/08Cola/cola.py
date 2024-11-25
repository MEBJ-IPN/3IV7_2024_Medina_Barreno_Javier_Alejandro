def crear_cola():
    return[]

def encolar(cola, elemento):
    cola.append(elemento)

def esta_vacia(cola):
    return len(cola)==0

def desencolar(cola,elemento):
    if esta_vacia(cola):
        raise IndexError("Error: la cola esta vacia")
    return cola.pop(0)

def frente(cola):
    if esta_vacia(cola):
        raise IndexError("Error: la cola esta vacia")
    return cola[0]

def tamano(cola):
    return len(cola)

def mostrar_cola(cola):
    return f"Cola actual: {cola}"
