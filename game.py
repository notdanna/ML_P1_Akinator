import json

# Colores ANSI para resaltar texto en la terminal
VERDE = '\033[92m'    
AMARILLO = '\033[93m' 
RESET = '\033[0m'     
TAB = "   "          

# Función para cargar un archivo JSON y devolver su contenido como diccionario
def cargar_arbol(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

# Función recursiva para recorrer el árbol de decisiones
def jugar(nodo, archivos, nivel=0, contador=[0]):
    # Caso base: si el nodo contiene un resultado final
    if "resultado" in nodo:
        print(f"{TAB * nivel}➜ {VERDE}{nodo['resultado']}{RESET}")  #
        print(f"\n{AMARILLO}Total de preguntas realizadas: {contador[0]}{RESET}\n") 
        return True
    
    # Incrementa el contador de preguntas
    contador[0] += 1
    # Muestra la pregunta en pantalla con el nivel de indentación
    print(f"\n{TAB * nivel}{AMARILLO}[P:{contador[0]}]{RESET} {nodo['pregunta']} (s/n): ", end="")
    respuesta = input().lower()  

    # Según la respuesta, sigue por la rama "si" o "no" del árbol
    if respuesta.startswith("s"):
        return jugar(nodo["si"], archivos, nivel + 1, contador)
    else:
        return jugar(nodo["no"], archivos, nivel + 1, contador)

# Lista de archivos JSON a usar (solo el principal)
archivos = ["handler.json"]
# Se carga el árbol de decisión principal desde el JSON
arbol_principal = cargar_arbol(archivos[0])

print("Akinateando...\n")
# Inicia el recorrido del árbol de decisiones
jugar(arbol_principal, archivos)
