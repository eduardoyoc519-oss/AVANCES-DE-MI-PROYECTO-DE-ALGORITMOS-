

def mostrar_cursos(lista_de_cursos):
    print("\n lista de cursos")
    if not lista_de_cursos:
        print("no hay cursos en la lista.")
    else:
        # usamos un ciclo para imprimir cada curso con un numero
        for i, curso in enumerate(lista_de_cursos):
            print(f"{i + 1}. {curso}")
    print(" - \n")

def agregar_curso(lista_de_cursos, nombre_del_curso):
    if nombre_del_curso: # revisa si el usuario escribio algo
        lista_de_cursos.append(nombre_del_curso)
        print(f"listo se agrego el curso: '{nombre_del_curso}'.")
    else:
        print("error: no ingresaste un nombre valido.")
    return lista_de_cursos

def eliminar_curso(lista_de_cursos, nombre_del_curso):
    if nombre_del_curso: # revisa si el usuario escribio algo
        try:
            # el metodo .remove() busca el elemento y lo borra.
            # si no lo encuentra, produce un error (valueerror).
            lista_de_cursos.remove(nombre_del_curso)
            print(f"listo se elimino el curso: '{nombre_del_curso}'.")
        except ValueError:
            print(f"error: el curso '{nombre_del_curso}' no se encontro en la lista.")
    else:
        print("error: no ingresaste un nombre valido.")
    return lista_de_cursos