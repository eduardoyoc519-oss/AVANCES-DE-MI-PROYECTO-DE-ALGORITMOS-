proyecto 04: gestor de elementos (cursos)
 conceptos aplicados 
1.  **listas (lists)**: usamos una lista de python para almacenar los nombres de los cursos. esta es la estructura de datos principal de nuestro programa. veras como anadir (`append`) y quitar (`remove`) elementos de ella.
2.  **funciones (functions)**: el codigo esta organizado en funciones pequenas y claras (`mostrar_cursos`, `agregar_curso`, `eliminar_curso`). cada funcion tiene una unica responsabilidad. esto hace que el codigo sea mas facil de leer, entender y reutilizar.
3.  **modularizacion (modularization)**: para mantener el codigo organizado, lo hemos dividido en dos archivos:
* `EliminacionCursos.py`: es el punto de entrada. contiene el menu principal y la logica de interaccion con el usuario.
* `cursos.py`: actua como un "modulo" que contiene todas las funciones especificas para manipular la lista. el archivo ` EliminacionCursos.py ` importa este modulo para poder usar sus funciones. esta separacion es una practica muy comun en programacion para proyectos mas grandes.
4.  **manejo de errores (error handling)**: en la funcion `eliminar_curso`, usamos un bloque `try...except`. esto nos permite manejar de forma segura el caso en que un usuario intente eliminar un curso que no existe en la lista, evitando que el programa se detenga por un error.

¿como funciona el codigo?
el proyecto se puede adaptar para manejar cualquier tipo de elemento,
* **`main.py` (el director de orquesta)**:
1.  inicia con una lista de elementos (en este caso, `mis_cursos`).
2.  entra en un ciclo infinito (`while true`) para mostrarle al usuario un menu de opciones.
3.  espera a que el usuario elija una opcion.
4.  dependiendo de la eleccion, "llama" a la funcion correcta del modulo `cursos.py` para que haga el trabajo.
5.  si el usuario elige salir, el ciclo se rompe y el programa termina.

* **` EliminacionCursos.py ` (la caja de herramientas)**:
1.  **`mostrar_cursos(lista)`**: recibe cualquier lista y la imprime de forma ordenada.
2.  **`agregar_curso(lista, elemento)`**: recibe una lista y un nuevo elemento, lo anade al final y devuelve la lista actualizada.
3.  **`eliminar_curso(lista, elemento)`**: recibe una lista y un elemento a borrar. intenta quitarlo y devuelve la lista actualizada. si el elemento no existe, informa al usuario sin que el programa falle.
Y listo eso es algo que se le agregara al proyecto
