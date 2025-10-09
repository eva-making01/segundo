
cola = []  # Se inicia una lista vacía para simular una cola (estructura FIFO).

# --- Funciones básicas ---

def esta_vacia(cola):
    return len(cola) == 0  # Retorna True 

def encolar(cola, elemento):  
    cola.append(elemento)  # Usamos append para añadir el nuevo elemento al final.
    print(f"Se encoló: {elemento}")  

def desencolar(cola):  
    if not esta_vacia(cola):  
        elemento = cola.pop(0)  # Se elimina y guarda el primer elemento (índice 0).
        print(f"Se desencoló: {elemento}")  # Se informa qué elemento fue desencolado.
        return elemento  
    else:
        print("La cola está vacía. No se puede desencolar.")  # Si no hay elementos, se informa.

def ver_frente(cola):  
    if not esta_vacia(cola):  # Verifica que la cola no esté vacía.
        print(f"Elemento al frente: {cola[0]}")  # Muestra el primer elemento (el más antiguo).
        return cola[0]  
    else:
        print("La cola está vacía.")  

def mostrar_cola(cola):  # Muestra todos los elementos en la cola.
    print("Estado actual de la cola:", cola)  # Se imprime la lista completa.

# --- Uso paso a paso ---

print("¿La cola está vacía?", esta_vacia(cola))  # Se verifica si la cola está vacía (True al inicio).

encolar(cola, "Persona 1")  # Se agrega "Persona 1" 
encolar(cola, "Persona 2")  # Se agrega "Persona 2" 
encolar(cola, "Persona 3")  # Se agrega "Persona 3"

mostrar_cola(cola)  # Muestra el estado actual de la cola

ver_frente(cola)  # Muestra el primer elemento

desencolar(cola)  # Se elimina "Persona 1"
mostrar_cola(cola)  

desencolar(cola)  # Elimina 
desencolar(cola)  # Elimina 
desencolar(cola)  # Intenta eliminar un elemento

print("¿La cola está vacía?", esta_vacia(cola))  # Verifica de nuevo si está vacía 

