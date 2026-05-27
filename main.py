from tpi2_G17_fernandez_hubert_maldonado import *
from modulo_funcional import *

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

print('='*5, "Inicializar Biblioteca Especializadad", '='*5)
bib = BibliotecaEspecializada(str(input("Ingrese el nombre de la biblioteca especializada: ")),
                               str(input("Ingrese la especialidad de la biblioteca: ")))

print(f"Biblioteca \"{bib.nombre}\" inicializada con exito!")
print('=' * 40)

print("***** SISTEMA DE GESTION DE BIBLIOTECA PERSONAL *****")

print('=' * 40)

while True:
    mostrar_opciones()
    
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
        genero_aux = str(input("Ingrese el genero de el/los libros: "))
        print(f"=== LIBROS DEL GENERO \"{genero_aux}\" ===")
        Libro.mostrar_lista_libros(bib.filtrar_por_genero(genero_aux))
        print('=' * 40)

    elif(op == 5):
        # Marcar libro como leído
        if len(bib) == 0:
            print(f"No hay ningun libro en la biblioteca \"{bib.nombre}\".")
        else:
            bib.mostrar_libros()
            print('='*10)
            n_aux = pedir_entre(f"Ingrese el numero del libro a marcar como leido (1, {len(bib)}): ", 1, len(bib))
            bib.libros[n_aux-1].marcar_leido()
            print(f"El Libro == {bib.libros[n_aux-1]} == fue marcado como leido exitosamente!")            
        print('=' * 40)

    elif(op == 6):
        # Ver estadísticas
        bib.estadisticas()
        print('=' * 40)

    elif(op == 7):
        # Exportar resumen
        print("=== RESUMEN BIBLIOTECA ===")
        print(f"== {len(bib)} libros ==")
        if len(bib) > 0: print(resumen_coleccion(bib))
        print('=' * 40)

    elif(op == 8):
        # Salir
        print("Programa Finalizado.")
        print("Gracias por usar el Sistema de gestion de biblioteca personal!!!")
        break


# Reflexión comparativa

# ─ Pregunta 1
# Comparen agregar_libro() del TPI 1 con el método agregar() de Biblioteca.
#
# En el TPI 1, agregar_libro() era una función completamente
# independiente. No recibía la lista como parámetro — la lista "biblioteca"
# era una variable global, y el resultado de la función se agregaba desde
# el bucle principal:
#
#   def agregar_libro() -> dict:
#       libro = {"titulo": str(input(...)), "autor": str(input(...)), ...}
#       ...
#       return libro
#   # y en el menú:
#   biblioteca.append(agregar_libro())
#
# agregar_libro() no sabía nada sobre la colección: sólo construía un diccionario y lo devolvía. La responsabilidad de insertarlo
# en la lista quedaba en el código del menú. Cualquier parte del programa
# podía llamar a biblioteca.append() directamente sin pasar por ninguna
# validación, porque la lista era global y accesible desde cualquier lado.
#
# En el TPI 2, agregar() es un método de la clase Biblioteca:
#
#   def agregar(self, libro):
#       self.libros.append(libro)
#
# Ahora la colección (self.libros) es un atributo del objeto, y la única
# forma de insertar un libro es a través de este método. La diferencia
# conceptual es el encapsulamiento. Une los datos y las operaciones. También
# simplifica la extensibilidad y la legibilidad.

# ─ Pregunta 2
# ¿Qué ventaja concreta trajo usar herencia en BibliotecaEspecializada?
#
# BibliotecaEspecializada necesita todo lo que ya hace Biblioteca y solo extiende estadisticas() para mostrar la especialidad.
# Con herencia, eso se logra así:
#
#   class BibliotecaEspecializada(Biblioteca):
#       def __init__(self, nombre, especialidad):
#           super().__init__(nombre)
#           self.especialidad = especialidad
#
#       def estadisticas(self):
#           super().estadisticas()   # reutiliza las 4 líneas del padre
#           print(f"  Especialidad : {self.especialidad}")
#
# Agregar(), buscar_por_autor() y filtrar_por_genero() se heredan sin
# escribir ni una línea extra.
#
# Sin herencia, la única alternativa limpia sería composición:
#   self.base = Biblioteca(nombre)
# y habría que delegar manualmente cada método:
#   def agregar(self, libro): return self.base.agregar(libro)
#   def buscar_por_autor(self, autor): return self.base.buscar_por_autor(autor)
#   
# Esto sólo duplica código innecesario.

# ─ Pregunta 3
# ¿Es lo mismo aplicar filter()/map() sobre objetos Libro que sobre dicts?
#
# En el TPI 1 (G17) ya usábamos filter() y map(), pero sobre diccionarios.
# Por ejemplo, en estadisticas():
#
#   len(list(filter(lambda libro: libro["leido"] == True, libros)))
#
# y en exportar_resumen():
#
#   map(lambda l: f"{l['titulo']} - {l['autor']} - ({l['anio']}) ...", libros)
#
# El acceso era por clave de string: l["titulo"], l["autor"], l["leido"].
# Escribir mal una clave (l["titluo"]) provoca un KeyError en tiempo de
# ejecución, y no hay ninguna garantía de que el diccionario tenga las claves
# esperadas — cualquier append() con un dict mal formado rompería todo.
#
# En el TPI 2, las mismas operaciones se hacen sobre objetos Libro (modulo_funcional.py):
#
#   filter(lambda libro: libro.leido, biblioteca.libros)
#   map(lambda libro: libro.titulo, leidos)
#   map(formatear_libro, biblioteca.libros)
#
# El acceso es por atributo. Si el atributo no
# existe, el error es un AttributeError. Además, toda la lógica de
# representación puede centralizarse en __str__ de Libro, en vez de
# repetir el formato dentro de cada lambda como hacíamos en exportar_resumen()
# del TPI 1.
#
# def exportar_resumen(libros: list):
#    #Lista de strings usando map
#    resumenes = list(map(lambda l: f"{l['titulo']} - {l['autor']} - ({l['anio']}) - {l['genero']} - {'Leido' if l['leido'] else 'No leido'}", libros))
#
#    for linea in resumenes:
#        print(linea)