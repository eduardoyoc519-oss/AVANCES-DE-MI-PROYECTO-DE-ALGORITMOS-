Algoritmo RegistroNotasPromedio
	
    Definir nota Como Real // aqui definimos las variables para poder hacer los procesos
	
    Definir suma Como Real
    Definir promedio Como Real
    Definir cantidad Como Entero
    Definir continuar Como Caracter
    
    suma <- 0  // y aqui lo que hicimos fue colocarle un valor a estas variables
    cantidad <- 0
    
    Repetir // lo siguiente que realizamos aqui fue un bucle el cual nos pide el numeor de notas de 0 a 100 y donde tambien nos pregunta si uno quiere seguir agregando mas notas enteonces colo losac la letra s de si y este seguira y seguira hasta que uno le digoa n de no al darke lo que hara sera sacar el promedio del a notas, sumar las notas y las notas registradas 
        Escribir "Ingrese una nota entre 0 y 100"
        Leer nota
        
        Si nota >= 0 Y nota <= 100 Entonces
            suma <- suma + nota
            cantidad <- cantidad + 1
        SiNo
            Escribir "Error la nota debe se entre 0 y 100"
        FinSi
        
        Escribir "Desea ingresar otra nota S - N"
        Leer continuar
    Hasta Que continuar = "N" O continuar = "n"
    
    Si cantidad > 0 Entonces //este es el resultado que calcula el promedio y suma las cantidades al nosotros dalar al bucle de arriba que no, este nos dara los siguientes resultados 
        promedio <- suma / cantidad
        Escribir "Notas registradas ", cantidad
        Escribir "Suma de notas ", suma	
        Escribir "Promedio final ", promedio
    SiNo
        Escribir "No se registraron notas validas"
		
    FinSi
// la verdad no se si es haci inge pero yo eso entendi en el enunciado, si no pregunte perdon pero yo entinedo que eso es haci c:
FinAlgoritmo
