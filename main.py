from avl import AVL
from utilidades import cargar_desde_csv, generar_dot


def mostrar_menu():
    print("\n===== MENÚ ÁRBOL AVL =====")
    print("1. Insertar número")
    print("2. Buscar número")
    print("3. Eliminar número")
    print("4. Cargar árbol desde CSV")
    print("5. Visualizar árbol en Graphviz (.dot)")
    print("6. Mostrar recorrido inorden")
    print("7. Salir")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")


def main():
    arbol = AVL()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            numero = leer_entero("Ingrese el número a insertar: ")
            arbol.insertar(numero)
            print(f"Número {numero} insertado correctamente.")

        elif opcion == "2":
            numero = leer_entero("Ingrese el número a buscar: ")
            encontrado = arbol.buscar(numero)
            if encontrado:
                print(f"El número {numero} SÍ está en el árbol.")
            else:
                print(f"El número {numero} NO está en el árbol.")

        elif opcion == "3":
            numero = leer_entero("Ingrese el número a eliminar: ")
            if arbol.buscar(numero):
                arbol.eliminar(numero)
                print(f"Número {numero} eliminado correctamente.")
            else:
                print(f"El número {numero} no existe en el árbol.")

        elif opcion == "4":
            nombre_archivo = input("Ingrese el nombre del archivo CSV: ").strip()
            exito, resultado = cargar_desde_csv(arbol, nombre_archivo)
            if exito:
                print(f"Se cargaron {resultado} valores desde el archivo.")
            else:
                print(f"Error: {resultado}")

        elif opcion == "5":
            nombre_salida = input("Ingrese el nombre del archivo .dot de salida (ej. arbol.dot): ").strip()
            if not nombre_salida:
                nombre_salida = "arbol_avl.dot"

            exito, mensaje = generar_dot(arbol, nombre_salida)
            print(mensaje)

            if exito:
                print("Para generar la imagen con Graphviz usa:")
                print(f'dot -Tpng {nombre_salida} -o arbol.png')

        elif opcion == "6":
            recorrido = arbol.inorden()
            print("Recorrido inorden:", recorrido)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()