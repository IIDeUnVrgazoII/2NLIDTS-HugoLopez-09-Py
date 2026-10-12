class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

# Función Agregar elementos a la lista
def agregarNodo(cabeza_wrapper, valor):
    nuevoNodo = Nodo(valor)   # Creando el nuevo nodo
    
    # Obtenemos el nodo actual que está dentro de nuestro contenedor wrapper
    cabeza = cabeza_wrapper["nodo"]
    
    if cabeza is None:
        cabeza_wrapper["nodo"] = nuevoNodo
    else:
        actual = cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevoNodo

def imprimirLista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()

def borrarLista(cabeza_wrapper):
    cabeza = cabeza_wrapper["nodo"]
    while cabeza is not None:
        siguiente = cabeza.siguiente
        # En Python no existe 'delete', simplemente eliminamos la referencia
        print("Elemento borrado ")
        cabeza = siguiente
    
    # Vaciamos la cabeza para el código principal
    cabeza_wrapper["nodo"] = None

def main():
    print("Actividad 09 - Lista enlazada Simple\n")
    
    # Usamos un diccionario wrapper para simular el paso por referencia (Nodo*&)
    cabeza_wrapper = {"nodo": None} 
    
    try:
        tamanoLista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
    except ValueError:
        print("Cantidad de elementos no valida")
        return 1
        
    if tamanoLista <= 0:
        print("Cantidad de elementos no valida")
        return 1
        
    for i in range(tamanoLista):
        valor = int(input(f"Ingrese dato {i + 1}: "))
        # Invocamos nuestra funcion de agregar Nodo
        agregarNodo(cabeza_wrapper, valor)
        
    print("Imprimiendo Lista de numeros")
    imprimirLista(cabeza_wrapper["nodo"])
    
    borrarLista(cabeza_wrapper)
    
    return 0

if __name__ == "__main__":
    main()
