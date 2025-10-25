# Gestor de Notas Académicas
El proyecto es un Gestor de Notas Académicas implementado en Python, diseñado para simular las funcionalidades básicas de un sistema de registro de cursos y notas. 
Su principal objetivo es demostrar la aplicación práctica de diversas estructuras de datos y algoritmos fundamentales en la informática.

Estructuras de Datos Utilizadas:
· Lista de Diccionarios (cursos): Se utiliza como la estructura principal para el almacenamiento del dataset (conjunto de datos).
Cada elemento de la lista es un diccionario que representa un curso con dos campos clave: el nombre (cadena) y la nota (número real).
Esta estructura facilita el acceso, la modificación y la eliminación de registros individuales (CRUD).

·  Pila (historial_acciones): Implementada para gestionar el registro de cambios. Sigue la lógica LIFO (Último en Entrar, Primero en Salir). 
Permite al usuario consultar las acciones recientes de forma cronológica inversa, lo cual es ideal para auditar o deshacer acciones teóricas.

·  Cola (solicitudes_revision): Implementada para gestionar las peticiones de revisión de notas. Sigue la lógica FIFO (Primero en Entrar, Primero en Salir). 
Esto asegura que las solicitudes se procesen en el estricto orden en que fueron recibidas.

Funcionales: 	

1.Registrar un nuevo curso y nota.

2.Mostrar todas las notas registradas.

3.Calcular el promedio general de las notas.

4.Eliminar un curso existente.

5.Salir del sistema.

No funcionales:

1.El sistema se ejecutará en la consola utilizando el lenguaje Python.

2.No se deben utilizar librerías externas, solo estructuras básicas.

3.El menú debe ser interactivo y mantenerse activo mediante el uso de estructuras repetitivas.

4.El pseudocódigo debe usar bucles (`MIENTRAS`) y condicionales (`SI`, `SINO`).

