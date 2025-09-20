# importamos el modulo 'cursos' para poder usar sus funciones.
import cursos

def mostrar_menu():
    """
    esta funcion solo imprime el menu de opciones.
    """
    print("bienvenido al gestor de cursos")
    print("selecciona una opcion:")
    print("1. ver todos los cursos")
    print("2. agregar un nuevo curso")
    print("3. eliminar un curso")
    print("4. salir del programa")

# --- aqui empieza el programa ---

# esta es nuestra lista principal de cursos.
# puedes empezar con los cursos que quieras.
mis_cursos = ["matematicas", "programacion", "historia", "quimica"]

# usamos un ciclo 'while true' para que el menu se muestre
# una y otra vez hasta que el usuario decida salir.
while True:
    mostrar_menu()
    opcion = input("escribe el numero de tu eleccion: ")

    # opcion 1: ver la lista de cursos
    if opcion == "1":
        # llamamos a la funcion que esta en el archivo cursos.py
        cursos.mostrar_cursos(mis_cursos)

    # opcion 2: agregar un nuevo curso
    elif opcion == "2":
        nuevo = input("escribe el nombre del curso que quieres agregar: ")
        # la funcion 'agregar_curso' nos devuelve la lista actualizada.
        mis_cursos = cursos.agregar_curso(mis_cursos, nuevo)

    # opcion 3: eliminar un curso
    elif opcion == "3":
        a_borrar = input("escribe el nombre del curso que quieres eliminar: ")
        # la funcion 'eliminar_curso' nos devuelve la lista actualizada.
        mis_cursos = cursos.eliminar_curso(mis_cursos, a_borrar)

    # opcion 4: salir del programa
    elif opcion == "4":
        print("¡hasta luego!")
        break # 'break' rompe el ciclo y termina el programa.

    # si el usuario escribe otra cosa
    else:
        print("\nopcion no valida. por favor, intenta de nuevo.\n")