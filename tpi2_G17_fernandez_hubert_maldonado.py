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
        
    @staticmethod
    def mostrar_lista_libros(lista: list):
        """Dada una lista de libros las imprime con el formato: {nro de libro}. [{leido}] - {titulo} ({anio}) - {autor} - {genero}.
        Si la lista esta vacia, imprime el mensaje 'Lista de Libros vacia.'"""
        if len(lista) == 0:
            print('Lista de Libros vacia.')
        else:
            aux = 1 # Contador auxiliar
            for l in lista:
                print(f"{aux}. {l}")
                aux += 1
        
class Biblioteca():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []
        
    def __len__(self):
        return len(self.libros)
        
    def agregar_libro(self):
        """Solicita los datos al usuario y agrega el nuevo libro a la colección."""
        self.libros.append(Libro.pedir_libro())
        
    def mostrar_libros(self):
        """Imprime la lista completa con todos los datos. Indica si está vacía."""
        print(f"=== {len(self)} libros ===")
        if len(self) == 0:
            print(f"No hay ningun libro en la biblioteca \"{self.nombre}\".")
        else:
            Libro.mostrar_lista_libros(self.libros)
    
    def buscar_por_autor(self, autor: str) -> list:
        """Recibe un nombre de autor y retorna todos sus libros. Es case-sensitive .lower(). Usa una comprensión de lista."""
        autor = autor.lower()
        return list(filter(lambda l: l.autor.lower() == autor, self.libros))

    def filtrar_por_genero(self, genero: str) -> list:
        """Recibe un género y retorna la sublista correspondiente usando filter(). Es case-sensitive .lower()."""
        genero = genero.lower()
        return list(filter(lambda l: l.genero.lower() == genero, self.libros))
    
    def estadisticas(self):
        """Muestra: total de libros, cantidad leídos, géneros únicos y el libro más reciente."""
        print("=== ESTADISTICAS ===")
        print(f"- Total de Libros: {len(self)}.")
        print(f"- Cantidad de Libros Leidos: {len(list(filter(lambda l: l.leido, self.libros)))}.")
        #print(f"- Cantidad de Libros Leidos: {len(titulos_leidos(self))}.")    --> Si se usara el modulo_funcionañ
        if len(self) > 0:
            #libros_aux = libros_por_anio(self)  # Libros ordenados de menor a mayor anio    (Funcion de modulo_funcional.py)
            libros_aux = sorted(self.libros, key=lambda libro: libro.anio)
            print(f"- Libro mas reciente: {libros_aux[-1]}.")
      
class BibliotecaEspecializada(Biblioteca):
    def __init__(self, nombre: str, especialidad: str):
        super().__init__(nombre)
        self.especialidad = especialidad
        
    def estadisticas(self):
        super().estadisticas()
        print(f"- Especialidad de la Biblioteca: \"{self.especialidad}\".")