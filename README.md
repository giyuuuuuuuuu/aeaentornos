Descripción del proyecto:

Este proyecto consiste en un sistema de gestión de librería virtual en Python que permite a los usuarios realizar operaciones como añadir, buscar, modificar y eliminar libros, así como guardar y cargar la colección desde un archivo.

Funcionalidades:

Añadir libros: Permite agregar nuevos libros a la librería, especificando el título, autor, género y año de publicación.
Buscar libros: Permite buscar libros por título o por nombre del autor.
Modificar libros: Permite modificar la información de los libros existentes, como el título, el autor, el género o el año de publicación.
Eliminar libros: Permite eliminar libros de la librería por su título.
Guardar colección: Permite guardar la colección de libros en un archivo JSON.
Cargar colección: Permite cargar una colección de libros desde un archivo JSON.
Código:

El código está escrito en Python y se encuentra organizado en un único archivo llamado libreria.py. El código sigue las convenciones de estilo PEP 8 y PEP 257 para mejorar su legibilidad y mantenibilidad.

Pruebas unitarias:

El código incluye un conjunto completo de pruebas unitarias que utilizan el módulo unittest de Python para verificar la funcionalidad de cada método en la clase de gestión de la librería.

Control de versiones:

El código se encuentra alojado en un repositorio de GitHub en la siguiente dirección: [https://github.com/index](https://github.com/giyuuuuuuuuu/aeaentornos/new/main?filename=README.md)

Instalación:

Para instalar el código, se debe seguir los siguientes pasos:

Clonar el repositorio:
git clone https://github.com/index

Instalar las dependencias:

pip install -r requirements.txt

Uso:

Para utilizar el código, se debe importar la clase Libreria y crear una instancia de la misma. A continuación, se pueden utilizar los métodos de la clase para realizar las operaciones deseadas.

from libreria import Libreria

# Crear una instancia de la clase Libreria
libreria = Libreria()

# Añadir un libro
libreria.anadir_libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 1967)

# Buscar libros por título
libros = libreria.buscar_libro("Cien años de soledad")
print(libros)

# Modificar un libro
libreria.modificar_libro("Cien años de soledad", anio=1981)

# Eliminar un libro
libreria.eliminar_libro("El Principito")

# Guardar la colección en un archivo
libreria.guardar_libros("libreria.json")

# Cargar la colección desde un archivo
libreria.cargar_libros("libreria.json")

