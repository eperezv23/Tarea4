import csv


def cargar_desde_csv(arbol, nombre_archivo):
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            cantidad = 0

            for fila in lector:
                for dato in fila:
                    dato = dato.strip()
                    if dato:
                        arbol.insertar(int(dato))
                        cantidad += 1

            return True, cantidad
    except FileNotFoundError:
        return False, "Archivo no encontrado."
    except ValueError:
        return False, "El CSV contiene datos no numéricos."
    except Exception as e:
        return False, f"Error inesperado: {e}"


def generar_dot(arbol, nombre_salida="arbol_avl.dot"):
    try:
        with open(nombre_salida, "w", encoding="utf-8") as archivo:
            archivo.write("digraph AVL {\n")
            archivo.write("    node [shape=circle];\n")

            if arbol.raiz is None:
                archivo.write("\n")
            else:
                _escribir_nodos(arbol.raiz, archivo)

            archivo.write("}\n")

        return True, f"Archivo Graphviz generado: {nombre_salida}"
    except Exception as e:
        return False, f"No se pudo generar el archivo DOT: {e}"


def _escribir_nodos(nodo, archivo):
    if nodo is None:
        return

    if nodo.izquierdo:
        archivo.write(f'    "{nodo.valor}" -> "{nodo.izquierdo.valor}";\n')
        _escribir_nodos(nodo.izquierdo, archivo)

    if nodo.derecho:
        archivo.write(f'    "{nodo.valor}" -> "{nodo.derecho.valor}";\n')
        _escribir_nodos(nodo.derecho, archivo)