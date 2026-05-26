from tpi2_G17_fernandez_hubert_maldonado import *

def titulos_leidos(biblioteca: Biblioteca) -> list:
    """Retorna una lista con los títulos de los libros leídos usando filter() y map()."""

    libros = biblioteca.libros #para el linter

    leidos = filter(lambda libro: libro.leido, libros)
    titulos = map(lambda libro: libros.titulo, leidos)
    
    return list(titulos)
    

def resumen_coleccion(biblioteca: Biblioteca) -> str:
    """Genera un string con el resumen de cada libro usando map() y una función lambda o auxiliar"""

    libros = biblioteca.libros

    def formatear_libro(libro):
        estado = '✔' if libro.leido else '✘'
        return f'"{libro.titulo}" — {libro.autor} ({libro.anio}) [{libro.genero}] {estado}'
    
    resumenes = map(formatear_libro, libros)
    return "\n".join(resumenes)

def libros_por_anio(biblioteca: Biblioteca) -> list:
    """Retorna la lista de libros ordenada por año usando sorted() con key=lambda."""

    libros = biblioteca.libros

    return sorted(libros, key=lambda libro: libro.anio)