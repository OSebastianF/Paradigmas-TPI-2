# TRABAJO PRÁCTICO INTEGRADOR 2 - GRUPO 17
# 5977582 - Osvaldo Sebastian Fernandez Coronel
# 6216581 - Mario David Maldonado Gomez
# 5266908 - Tim Julian Hubert Wiebe

from datetime import datetime # Se usa en pedir_libro() para validacion de anio 
def pedir_entre(msg: str, min: int, max: int) -> int:
	while True:
		try:
			n = int(input(msg))
			if n < min or n > max:
				raise ValueError
		except ValueError:
			print(f'ERROR. No se ingreso un numero valido ({min} - {max}).')
		else:
			return n

class Libro():
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.leido = False
        
    def __str__(self) -> str:
        return f"[{'✔' if self.leido else '✘'}] \"{self.titulo}\" ({self.anio}) - {self.autor} - {self.genero}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def marcar_leido(self):
        """Marca el libro como leido."""
        self.leido = True
        
    @classmethod
    def pedir_libro(cls): # -> Libro: (Puede crear error 'NameError: name 'Libro is not defined')
        """Pide al usuario los datos de un libro y lo retorna en un objeto de la clase Libro"""
        titulo = str(input('Ingrese el titulo del libro: '))
        autor = str(input(f'Ingrese el nombre del autor de \"{titulo}\": '))
        anio = pedir_entre(f'Ingrese el anio de salida del libro \"{titulo}\": ', 0, datetime.now().year)
        genero = str(input(f'Ingrese el genero del libro \"{titulo}\": '))
        return cls(titulo, autor, anio, genero)
        
class Biblioteca():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []
        
    def agregar_libro(self):
        """Solicita los datos al usuario y agrega el nuevo libro a la colección."""
        self.libros.append(Libro.pedir_libro())
        
    def mostrar_libros(self):
        """Imprime la lista completa con todos los datos. Indica si está vacía."""
        pass
    
    def buscar_por_autor(self, autor: str) -> list:
        """Recibe un nombre de autor y retorna todos sus libros. Es case-sensitive .lower(). Usa una comprensión de lista."""
        pass

    def filtrar_por_genero(self, genero: str) -> list:
        """Recibe un género y retorna la sublista correspondiente usando filter(). Es case-sensitive .lower()."""
        pass
    
    def estadisticas(self):
        """Muestra: total de libros, cantidad leídos, géneros únicos y el libro más reciente."""
        pass
      
class BibliotecaEspecializada(Biblioteca):
    def __init__(self, nombre: str, especialidad: str):
        super().__init__(nombre)
        self.especialidad = especialidad
        
    def estadisticas(self):
        super().estadisticas()
        # TODO: Extender agregando 'especialidad'