import unittest
from aeaentornos import Libreria


class TestAnadirLibro(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro_valido(self):
        titulo = "Cien años de soledad"
        autor = "Gabriel Garcia Marquez"
        genero = "Novela"
        anio = 1967

        resultado = self.libreria.anadir_libro(titulo, autor, genero, anio)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0], {'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})

    def test_anadir_libro_titulo_vacio(self):
        titulo = ""
        autor = "Gabriel Garcia Marquez"
        genero = "Novela"
        anio = 1967

        with self.assertRaises(ValueError):
            self.libreria.anadir_libro(titulo, autor, genero, anio)

    def test_anadir_libro_autor_vacio(self):
        titulo = "Cien años de soledad"
        autor = ""
        genero = "Novela"
        anio = 1967

        with self.assertRaises(ValueError):
            self.libreria.anadir_libro(titulo, autor, genero, anio)

    def test_anadir_libro_genero_vacio(self):
        titulo = "Cien años de soledad"
        autor = "Gabriel Garcia Marquez"
        genero = ""
        anio = 1967

        with self.assertRaises(ValueError):
            self.libreria.anadir_libro(titulo, autor, genero, anio)

    def test_anadir_libro_anio_no_numerico(self):
        titulo = "Cien años de soledad"
        autor = "Gabriel Garcia Marquez"
        genero = "Novela"
        anio = "1967"

        with self.assertRaises(TypeError):
            self.libreria.anadir_libro(titulo, autor, genero, anio)


class TestBuscarLibro(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 1967)
        self.libreria.anadir_libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", 1943)

    def test_buscar_libro_titulo_exacto(self):
        titulo = "Cien años de soledad"
        libros = self.libreria.buscar_libro(titulo)
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0], {'titulo': titulo, 'autor': 'Gabriel Garcia Marquez', 'genero': 'Novela', 'anio': 1967})

    def test_buscar_libro_titulo_minusculas(self):
        titulo = "cien años de soledad"
        libros = self.libreria.buscar_libro(titulo)
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0], {'titulo': "Cien años de soledad", 'autor': 'Gabriel Garcia Marquez', 'genero': 'Novela', 'anio': 1967})

    def test_buscar_libro_titulo_no_encontrado(self):
        titulo = "El Quijote"
        libros = self.libreria.buscar_libro(titulo)
        self.assertEqual(len(libros), 0)

class TestBuscarPorAutor(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 1967)
        self.libreria.anadir_libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", 1943)
        self.libreria.anadir_libro("Crónica de una muerte anunciada", "Gabriel Garcia Marquez", "Novela", 1981)

