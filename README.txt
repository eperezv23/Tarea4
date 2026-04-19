PROYECTO AVL

DESCRIPCIÓN DEL PROYECTO
Este proyecto consiste en la implementación de un programa interactivo en Python que permite trabajar con un Árbol AVL, el cual es una extensión de un Árbol Binario de Búsqueda (ABB).

El programa fue desarrollado para insertar, buscar, eliminar y visualizar datos dentro del árbol, manteniendo siempre su balance por medio de rotaciones.

OBJETIVOS
- Implementar un Árbol Binario de Búsqueda.
- Extender la clase ABB para crear la clase AVL usando herencia.
- Permitir la inserción, búsqueda y eliminación de elementos.
- Cargar datos desde archivos CSV.
- Generar una representación visual del árbol mediante Graphviz.

FUNCIONALIDADES DEL PROGRAMA
El programa cuenta con un menú interactivo en consola que permite realizar las siguientes acciones:

1. Insertar un número en el árbol.
2. Buscar un número en el árbol.
3. Eliminar un número del árbol.
4. Cargar datos desde un archivo CSV.
5. Generar un archivo .dot para visualizar el árbol en Graphviz.
6. Mostrar el recorrido inorden del árbol.
7. Salir del programa.

ESTRUCTURA DEL PROYECTO
Los archivos que conforman el proyecto son los siguientes:

- main.py: contiene el menú principal y la interacción con el usuario.
- nodo.py: define la estructura de cada nodo del árbol.
- abb.py: contiene la implementación del Árbol Binario de Búsqueda.
- avl.py: contiene la implementación del Árbol AVL heredando de ABB.
- utilidades.py: contiene funciones auxiliares, como carga desde CSV y generación de archivos Graphviz.
- datos1.csv, datos2.csv, datos3.csv: archivos de ejemplo para probar la carga de datos.

REQUISITOS
Para ejecutar el programa se necesita:

- Python 3 instalado.
- Graphviz instalado, en caso de querer generar la imagen del árbol.

EJECUCIÓN DEL PROGRAMA
Para ejecutar el programa se debe abrir la terminal en la carpeta del proyecto y escribir:

python main.py

CARGA DE ARCHIVOS CSV
Para cargar un archivo CSV se debe seleccionar la opción 4 del menú e ingresar el nombre del archivo, por ejemplo:

datos1.csv

Los archivos CSV deben estar en la misma carpeta del proyecto.

VISUALIZACIÓN CON GRAPHVIZ
El programa genera un archivo con extensión .dot, el cual luego puede convertirse a imagen usando Graphviz con el siguiente comando:

dot -Tpng arbol.dot -o arbol.png

También se pueden generar otros archivos como:

dot -Tpng ejemplo.dot -o ejemplo.png
dot -Tpng ejemplo1.dot -o ejemplo1.png

EJEMPLOS DE ARCHIVOS CSV
Se incluyen tres archivos CSV de ejemplo:

- datos1.csv
- datos2.csv
- datos3.csv

Estos archivos contienen números enteros que pueden ser cargados al árbol desde el menú interactivo.