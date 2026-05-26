from tpi2_G17_fernandez_hubert_maldonado import *
from modulo_funcional import *

# TODO: Implementar los metodos y agregarlos en las opciones
"""El menú del TPI 1 se mantiene, pero ahora opera sobre instancias de BibliotecaEspecializada. Al iniciarse el
programa, se le solicita al usuario el nombre y la especialidad de la biblioteca."""

def mostrar_opciones():
    print("1. Agregar libro")
    print("2. Mostrar todos los libros")
    print("3. Buscar por autor")
    print("4. Filtrar por género")
    print("5. Marcar libro como leído")
    print("6. Ver estadísticas")
    print("7. Exportar resumen")
    print("8. Salir")
    print('=' * 40)
    
# Inicio del programa

# TODO: Inicializar la biblioteca
print('='*5, "Inicializar Biblioteca Especializadad", '='*5)
bib = BibliotecaEspecializada(str(input("Ingrese el nombre de la biblioteca especializada: ")),
                               str(input("Ingrese la especialidad de la biblioteca: ")))

print(f"Biblioteca \"{bib.nombre}\" inicializada con exito!")
print('=' * 40)

print("***** SISTEMA DE GESTION DE BIBLIOTECA PERSONAL *****")

print('=' * 40)

while True:
    mostrar_opciones()
    
    """while True:
        try:
            op = int(input('Ingrese la opcion a ejecutar (1-8): '))
            if (op < 1) or (op > 8):
                raise ValueError
        except ValueError:
            print('ERROR (ValueError). No se ingreso una opcion valida (1-8).')
        else:
            break"""
    # Se usa la funcion definida en el archivo principal 
    op = pedir_entre('Ingrese la opcion a ejecutar (1-8): ', 1, 8)
    
    print('=' * 40)

    if(op == 1):
        # Agregar Libro
        bib.agregar_libro()
        print("Libro aniadido con exito!")
        print('=' * 40)

    elif(op == 2):
        # Mostrar todos los libros
        bib.mostrar_libros()
        print('=' * 40)

    elif(op == 3):
        # Buscar por autor
        autor_aux = str(input("Ingrese el nombre del autor: "))
        print(f"=== LIBROS DEL AUTOR \"{autor_aux}\" ===")
        Libro.mostrar_lista_libros(bib.buscar_por_autor(autor_aux))
        print('=' * 40)

    elif(op == 4):
        # Buscar por genero
        genero_aux = input("Ingrese el genero de el/los libros: ")
        print(f"=== LIBROS DEL GENERO \"{genero_aux}\" ===")
        Libro.mostrar_lista_libros(bib.filtrar_por_genero(genero_aux))
        print('=' * 40)

    elif(op == 5):
        # Marcar libro como leído
        titulo = input("Ingrese el título del libro: ")
        print('=' * 40)

    elif(op == 6):
        # Ver estadísticas
        print('=' * 40)

    elif(op == 7):
        # Exportar resumen
        print("Cantidad de Libros:")
        print('=' * 40)

    elif(op == 8):
        # Salir
        print("Programa Finalizado.")
        print("Gracias por usar el Sistema de gestion de biblioteca personal!!!")
        break