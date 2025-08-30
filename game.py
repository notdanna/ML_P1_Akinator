import json

def cargar_arbol(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def jugar(nodo, archivos):
    if "resultado" in nodo:
        print(f"Resultado: {nodo['resultado']}")
        return True
    if "redirigir" in nodo:
        nuevo_arbol = cargar_arbol(nodo["redirigir"])
        return jugar(nuevo_arbol, archivos)
    respuesta = input(f"{nodo['pregunta']} (s/n): ").lower()
    if respuesta.startswith("s"):
        return jugar(nodo["si"], archivos)
    else:
        return jugar(nodo["no"], archivos)

archivos = ["handler.json"]
arbol_principal = cargar_arbol(archivos[0])
jugar(arbol_principal, archivos)