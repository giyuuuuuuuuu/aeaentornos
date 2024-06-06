import json


class Libreria:
    """
    Clase que representa una librería virtual.

    Permite realizar operaciones como añadir, buscar, modificar y eliminar libros,
    así como guardar y cargar la colección desde un archivo.
    """

    def __init__(self):
        """
        Inicializa la librería virtual.

        Crea una lista vacía para almacenar los libros.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la librería.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Un mensaje indicando si el libro se ha añadido correctamente.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Una lista con los libros que coinciden con el título especificado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por el nombre del autor.

        Args:
            autor (str): El nombre del autor a buscar.

        Returns:
            list: Una lista con los libros escritos por el autor especificado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la librería por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Un mensaje indicando si el libro se ha eliminado correctamente.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            archivo (str): La ruta del archivo JSON donde se guardarán los libros.

        Returns:
        
        """
    
    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"



mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))