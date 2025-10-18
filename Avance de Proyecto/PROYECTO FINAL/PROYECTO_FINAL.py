import os #Este import tiene la funcion de limpiar la terminal para que se vea mas limpio todo 
# --- ESTRUCTURAS DE DATOS ---
cursos = []
historial_acciones = []  # Pila para el historial (LIFO)   #lista para ir ordenando 
solicitudes_revision = []  # Cola para revisiones (FIFO)

# --- FUNCIONES DEL CRUD DE CURSOS ---
def agregar_curso():
    """Agrega un nuevo curso a la lista de cursos."""
    nombre_curso = input("Ingrese el nombre del nuevo curso: ")
    cursos.append({"nombre": nombre_curso, "estudiantes": []})
    registrar_accion(f"Se agrego el curso: {nombre_curso}")
    print(f"¡Curso '{nombre_curso}' agregado con exito!")

def eliminar_curso():
    """Elimina un curso existente."""
    mostrar_cursos()
    if not cursos:
        return
    try:
        idx = int(input("Ingrese el numero del curso a eliminar: ")) - 1
        if 0 <= idx < len(cursos):
            curso_eliminado = cursos.pop(idx)
            registrar_accion(f"Se elimino el curso: {curso_eliminado['nombre']}")
            print(f"¡Curso '{curso_eliminado['nombre']}' eliminado con exito!")
        else:
            print("Numero de curso no válido.")
    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero.")


def mostrar_cursos():
    """Muestra todos los cursos registrados."""
    print("\n--- Cursos Disponibles ---")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for i, curso in enumerate(cursos):
            print(f"{i + 1}. {curso['nombre']}")
    print("-" * 25)

# --- FUNCIONES DE GESTIÓN DE ESTUDIANTES Y NOTAS ---

def gestionar_curso():
    """Permite gestionar los estudiantes y notas de un curso especifico."""
    mostrar_cursos()
    if not cursos:
        return
    try:
        idx_curso = int(input("Seleccione el numero del curso a gestionar: ")) - 1
        if 0 <= idx_curso < len(cursos):
            menu_gestion_estudiantes(idx_curso)
        else:
            print("Numero de curso no valido.")
    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero.")


def menu_gestion_estudiantes(idx_curso):
    """Muestra el menu para gestionar estudiantes dentro de un curso."""
    curso = cursos[idx_curso]
    nombre_curso = curso['nombre']
    
    while True:
        print(f"\nGestionando Curso: {nombre_curso}")
        print("1. Agregar estudiante y sus notas")
        print("2. Ver estudiantes y promedios")
        print("3. Ordenar estudiantes por nombre (Burbuja)")
        print("4. Ordenar estudiantes por promedio (Inserción)")
        print("5. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            agregar_estudiante(idx_curso)
        elif opcion == '2':
            ver_estudiantes(idx_curso)
        elif opcion == '3':
            ordenamiento_burbuja(curso['estudiantes'])
            registrar_accion(f"Se ordenaron por nombre los estudiantes de {nombre_curso}")
        elif opcion == '4':
            ordenamiento_insercion(curso['estudiantes'])
            registrar_accion(f"Se ordenaron por promedio los estudiantes de {nombre_curso}")
        elif opcion == '5':
            break
        else:
            print("Opcion no valida.")

def agregar_estudiante(idx_curso):
    """Agrega un estudiante con sus notas al curso."""
    nombre = input("Nombre del estudiante: ")
    try:
        notas_str = input("Ingrese las notas separadas por comas (tipo haci. 85,90,78): ")
        notas = [float(nota.strip()) for nota in notas_str.split(',')]
        promedio = sum(notas) / len(notas) if notas else 0
        
        cursos[idx_curso]['estudiantes'].append({
            "nombre": nombre,
            "notas": notas,
            "promedio": promedio
        })
        registrar_accion(f"Se agrego a {nombre} en {cursos[idx_curso]['nombre']}")
        print(f"Estudiante {nombre} agregado con un promedio de {promedio:.2f}. ")
    except ValueError:
        print("Error: Asegúrese de ingresar solo numeros para las notas.")

def ver_estudiantes(idx_curso):
    """Muestra los estudiantes de un curso con sus notas y promedio."""
    estudiantes = cursos[idx_curso]['estudiantes']
    print(f"\n--- Estudiantes de {cursos[idx_curso]['nombre']} ---")
    if not estudiantes:
        print("No hay estudiantes registrados en este curso.")
    else:
        for est in estudiantes:
            notas_str = ", ".join(map(str, est['notas']))
            print(f"- {est['nombre']} | Notas: [{notas_str}] | Promedio: {est['promedio']:.2f}")
    print("-" * 35)


# --- ALGORITMOS DE ORDENAMIENTO ---

def ordenamiento_burbuja(lista):
    """Ordena una lista de estudiantes por nombre usando el metodo de burbuja."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['nombre'].lower() > lista[j + 1]['nombre'].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Estudiantes ordenados por nombre.  alfabeticamente.")

def ordenamiento_insercion(lista):
    """Ordena una lista de estudiantes por promedio (descendente) usando insercion."""
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key['promedio'] > lista[j]['promedio']:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    print("Estudiantes ordenados por promedio.")

# --- FUNCIONES DE PILAS Y COLAS ---
def registrar_accion(accion):
    """Agrega una accion a la pila de historial."""
    historial_acciones.append(accion)

def ver_historial():
    """Muestra el historial de acciones (LIFO)."""
    print("\n--- Historial de Acciones (última a primera) ---")
    if not historial_acciones:
        print("No se han realizado acciones.")
    else:
        # Imprime desde el final para mostrar la última accion de primero
        for accion in reversed(historial_acciones):
            print(f"- {accion}")
    print("-" * 50)

def agregar_solicitud_revision():
    """Agrega una solicitud a la cola de revision."""
    estudiante = input("Nombre del estudiante que solicita revision: ")
    curso = input("Curso para el que solicita revisión: ")
    solicitud = f"Estudiante: {estudiante}, Curso: {curso}"
    solicitudes_revision.append(solicitud)
    registrar_accion(f"Se agregó una solicitud de revision para {estudiante}")
    print("Solicitud de revision agregada.")

def procesar_revision():
    """Procesa la primera solicitud en la cola (FIFO)."""
    if not solicitudes_revision:
        print("No hay solicitudes de revision pendientes.")
    else:
        solicitud_procesada = solicitudes_revision.pop(0)
        print(f"Procesando: {solicitud_procesada}")
        registrar_accion(f"Se proceso la solicitud de revision: {solicitud_procesada}")

# --- FUNCION PRINCIPAL Y MENÚ ---

def main():
    while True:
        print("\n===== SISTEMA DE GESTION ACADEMICA =====" )
        print("1. Agregar Curso" )
        print("2. Eliminar Curso" )
        print("3. Mostrar Cursos" )
        print("4. Gestionar un Curso (Estudiantes y Notas)" )
        print("5. Agregar Solicitud de Revision de Notas")
        print("6. Procesar Siguiente Solicitud de Revision" )
        print("7. Ver Historial de Acciones" )
        print("8. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            agregar_curso()
        elif opcion == '2':
            eliminar_curso()
        elif opcion == '3':
            mostrar_cursos()
        elif opcion == '4':
            gestionar_curso()
        elif opcion == '5':
            agregar_solicitud_revision()
        elif opcion == '6':
            procesar_revision()
        elif opcion == '7':
            ver_historial()
        elif opcion == '8':
            print("¡ Adiooooos hasta pronto !")
            break
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main() 
    #Este if lo utilice por que vi en un tiktok que decia que contiene la logica principal (main()) solo se inicie cuando el archivo es el programa principal, y no cuando es utilizado como una biblioteca de funciones.



