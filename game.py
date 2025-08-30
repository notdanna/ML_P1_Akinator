import json

# Colores ANSI
VERDE = '\033[92m'
AMARILLO = '\033[93m'
RESET = '\033[0m'
TAB = "   "  # 4 espacios para indentación

def cargar_arbol(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def jugar(nodo, archivos, nivel=0, contador=[0]):
    if "resultado" in nodo:
        print(f"{TAB * nivel}➜ {VERDE}{nodo['resultado']}{RESET}")
        print(f"\n{AMARILLO}Total de preguntas realizadas: {contador[0]}{RESET}\n")
        return True
    
    if "redirigir" in nodo:
        nuevo_arbol = cargar_arbol(nodo["redirigir"])
        return jugar(nuevo_arbol, archivos, nivel, contador)
    
    contador[0] += 1
    print(f"\n{TAB * nivel}{AMARILLO}[P:{contador[0]}]{RESET} {nodo['pregunta']} (s/n): ", end="")
    respuesta = input().lower()
    if respuesta.startswith("s"):
        return jugar(nodo["si"], archivos, nivel + 1, contador)
    else:
        return jugar(nodo["no"], archivos, nivel + 1, contador)

archivos = ["handler.json"]
arbol_principal = cargar_arbol(archivos[0])
print("Akinateando...\n")
jugar(arbol_principal, archivos)