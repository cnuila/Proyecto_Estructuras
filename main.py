from Alumno import *
from Simbolo import *
from ArrayList import *
from ArrayStack import *
from LinkedStack import *
from Cola import *

#verifica que se una entrada valida
def verificarEntrada(entrada):
    if str(entrada).isdigit():
        return entrada
    else:
        return -1

def imprimirLinkedStack(index,nodo):
    isinstance(nodo,Node)
    if nodo.getSiguiente() is None:
        print(index,")",nodo.getData())
    else:
        print(index,")",nodo.getData())
        imprimirLinkedStack(index+1,nodo.getSiguiente())

def main():

    menuPrincipal = 0

    while menuPrincipal != 4 :
        print("------------------------------------------------")
        print("1. Trabajar con Listas","2. Trabajar con Pilas",
        "3. Trabajar con Colas","4. Salir",sep='\n')
        menuPrincipal = int(verificarEntrada(input("Ingrese su opcion: ")))

        if menuPrincipal == 1:

            opcionLista = 0
            while opcionLista != 3:
                print("------------------------------------------------")
                print("Menu Tipo de Lista","   1. Trabajar con ArrayList",
                    "   2. Trabajar con LinkedList",
                    "   3. Regresar al Menu Principal",sep='\n')

                opcionLista = int(verificarEntrada(input("Ingrese su opcion: ")))                
                
                if opcionLista == 1 or opcionLista == 2:
                    operacionLista = 0

                    while operacionLista != 10:
                        print("------------------------------------------------")
                        print("Operaciones de Listas","   1. Insertar Elemento",
                        "   2. Imprimir Elementos",
                        "   3. Buscar Elemento",
                        "   4. Borrar Elemento",
                        "   5. Ver si esta vacia",
                        "   6. Obtener Elemento por Posicion",
                        "   7. Obetener Siguiente",
                        "   8. Obtener Anterior",
                        "   9. Borrar todos los Elementos(Anula)",
                        "  10. Regresar al Menu Principal",sep='\n')
                        operacionLista = int(verificarEntrada(input("Ingrese su opcion: ")))

                        arraylist = ArrayList()
                        
                        if operacionLista == 1:
                            opcioningresar = 0
                            while opcioningresar != 2:
                                #datos del alumno y posición
                                numeroCuenta = int(input("Ingrese el número de cuenta del alumno: "))
                                nombre = str(input("Ingrese el nombre del alumno: "))
                                dato = Alumno(numeroCuenta, nombre)
                                posicion = int(input("Ingrese la posicion en la que desea insertar el elemento, la lista empieza en 1: "))
                                posicion = posicion-1
                                nuevoSize = arraylist.size
                                if (posicion <= nuevoSize) and (posicion >= 0):
                                    condicion = arraylist.inserta(dato, posicion)
                                    if condicion:
                                        print("El elemento fue agregado exitosamente")
                                    else:
                                        print("El elemento no fue agregado. Ingrese una posicion valida")
                                else:
                                    print("La posicion que ha ingresado no es valida")                                
                                print("----------------------------","1. Ingresar nuevo elemento","2. Regresar al menu", sep='\n')
                                opcioningresar = int(input("Ingrese una opcion: "))
                            #termina el while para ingresar otro elemento
                        #termina la primera opcion - agregar
                        elif operacionLista == 2:
                            if opcionLista == 1:
                                if arraylist.vacia() == 0:
                                    print("La lista esta vacia")
                                else:
                                    for i in range(arraylist.size,0,1):
                                        print(arraylist.size - i + 1,")",arraylist.arreglo[i])
                            if opcionLista == 2:
                                pass
                        #termina la segunda opcion - listar los elementos
                        elif operacionLista == 3:
                            if opcionLista == 1:
                                numeroCuenta = int(input("Ingrese el número de cuenta del alumno: "))
                                nombre = str(input("Ingrese el nombre del alumno: "))
                                dato = Alumno(numeroCuenta, nombre)
                                posicion = 3000
                                posicion = arraylist.buscar(dato)
                                if posicion != 3000:
                                    nuevaPosicion = int(posicion+1)
                                    print("La posicion del alumno es: ", nuevaPosicion+1)
                                else:
                                    print("El alumno no se encuentra en la lista.")
                            if opcionLista == 2:
                                #código de linkedlist
                                pass
                        #termina la segunda opcion - buscar un elemento
                        elif operacionLista == 4:
                            if opcionLista == 1:
                                posicion = int(input("Ingrese la posición del elemento que desea eliminar: "))
                                posicion = posicion-1
                                nuevoSize = arraylist.size
                                if (posicion <= nuevoSize) and (posicion >= 0):
                                    print("El elemento fue borrado exitosamente, ", arraylist.borrarElemento(posicion))
                            if opcionLista == 2:
                                #código de linkedlist
                                pass
                        #termina la segunda opcion - buscar un elemento
                        elif operacionLista == 5:
                            if opcionLista == 1:
                                listaVacia = arraylist.vacia()
                                if listaVacia != 0:
                                    print("La lista no esta vacia")
                                else:
                                    print("La lista esta vacia")
                            if opcionLista == 2:
                                #codigo de likedlist
                                pass
                        #termina la quinta opcion - ver si la lista esta vacia
                        elif operacionLista == 6:
                            if opcionLista == 1:
                                posicion = int(input("Ingrese la posicion del elemento: "))
                                nuevoSize = arraylist.size
                                nuevaPosicion = posicion-1
                                if (nuevaPosicion <= nuevoSize) and (nuevaPosicion >= 0):
                                    #elemento = arraylist.elementoPosicion(nuevaPosicion)
                                    #if(elemento != None):
                                    print("El elemento que se encuentra en la posicion ",nuevaPosicion, " es: ",arraylist.elementoPosicion(nuevaPosicion))
                            else:
                                print("La posicion que ha ingresado no es valida")
                            if opcionLista == 2:
                                #codigo de likedlist
                                pass
                        #termina la sexta opcion - obtener un elemento
                        elif operacionLista == 7:
                            if opcionLista == 1:
                                posicion = int(input("Ingrese la posicion del elemento: "))
                                nuevoSize = arraylist.size+1
                                if (posicion <= nuevoSize) and (posicion >= 0):
                                    elemento = arraylist.obtenerSiguiente(posicion)
                                    if elemento != None:
                                        print("El siguiente elemento de la posicion ", posicion, " es: ", elemento)
                                    else:
                                        print("EL elemento siguiente esta vacio")
                                else:
                                    print("La posicion que ha ingresado no es valida")
                            if opcionLista == 2:
                                #codigo de likedlist
                                pass
                        #termina la septima opcion - obtener el siguiente elemento
                        elif operacionLista == 8:
                            if opcionLista == 1:
                                posicion = int(input("Ingrese la posicion del elemento: "))
                                nuevoSize = arraylist.size+1
                                if (posicion <= nuevoSize) and (posicion >= 0):
                                    elemento = arraylist.obtenerAnterior(posicion)
                                    if elemento != None:
                                        print("El elemento anterior de la posicion ", posicion, " es: ", elemento)
                                    else:
                                        print("La posicion anterior esta vacia")
                                else:
                                    print("La posicion que ha ingresado no es valida")
                            if opcionLista == 2:
                                #codigo de likedlist
                                pass
                        #termina la octava opcion - obtener el anterior
                        elif operacionLista == 9:
                            if opcionLista == 1:
                                arraylist.anula()
                                print("La lista fue borrada exitosamente")
                            if opcionLista == 2:
                                #codigo de likedlist
                                pass
                        #termina la novena opcion - borrar todos los elementos
                        elif operacionLista == 10:
                            opcionLista = 3
                    #termina while operacion lista
            #termina while opcion listas
        elif menuPrincipal == 2:

            opcionPila = 0
            while opcionPila != 3:
                print("------------------------------------------------")
                print("Menu Tipo de Pila","   1. Trabajar con ArrayStack",
                    "   2. Trabajar con LinkedStack",
                    "   3. Regresar al Menu Principal",sep='\n')

                opcionPila = int(verificarEntrada(input("Ingrese su opcion: ")))

                pilaArray = ArrayStack()

                pilaNodos = LinkedStack()

                if opcionPila == 1 or opcionPila == 2:
                    operacionesPila = 0
                    
                    while operacionesPila != 6:
                        print("------------------------------------------------")
                        print("Operaciones de Pilas","   1. Empujar(Push)",
                        "   2. Sacar(Pop)",
                        "   3. Ver Tope(Peek)",
                        "   4. Verificar si esta vacia",
                        "   5. Imprimir elementos",
                        "   6. Regresar al Menu Principal",sep='\n')
                        operacionesPila = int(verificarEntrada(input("Ingrese su opcion: ")))

                        if operacionesPila == 1:

                            print()
                            symboloTemp = str(input("Ingrese su simbolo(solo se tomara el primer caracter en caso de ingresar un cadena): "))[0]
                            simbolo = Simbolo(symboloTemp)

                            if opcionPila == 1:
                                pilaArray.empuja(simbolo)

                            if opcionPila == 2:
                                pilaNodos.empuja(simbolo)

                        elif operacionesPila == 2:

                            if opcionPila == 1:
                                if pilaArray.vacia():
                                    print("La pila esta vacia, no hay elementos para sacar")
                                else:
                                    print("El elemento eliminado fue",pilaArray.saca())
                            
                            if opcionPila == 2:
                                if pilaNodos.vacia():
                                    print("La pila esta vacia, no hay elementos para sacar")
                                else:
                                    print("El elemento eliminado fue ",pilaNodos.saca())

                        elif operacionesPila == 3:

                            if opcionPila == 1:
                                if pilaArray.vacia():
                                    print("La pila esta vacia, no hay tope")
                                else:
                                    print("El tope es",pilaArray.tope())

                            if opcionPila == 2:
                                if pilaNodos.vacia():
                                    print("La pila esta vacia, no hay tope")
                                else:
                                    print("El tope es",pilaNodos.tope())
                                
                        elif operacionesPila == 4:

                            if (opcionPila == 1 and pilaArray.vacia()) or (opcionPila == 2 and pilaNodos.vacia()):
                                print("La pila esta vacia")
                            else:
                                print("La pila no esta vacia")
                            
                        elif operacionesPila == 5:
                            
                            if opcionPila == 1:
                                if pilaArray.vacia():
                                    print("La pila esta vacia")
                                else:
                                    for i in range(pilaArray.size,0,-1):
                                        print(pilaArray.size - i + 1,")",pilaArray.arreglo[i-1])
                            
                            if opcionPila == 2:
                                if pilaNodos.vacia():
                                    print("La pila esta vacia")
                                else:
                                    nodeTemp = pilaNodos.inicio
                                    imprimirLinkedStack(1,nodeTemp)

                        elif operacionesPila == 6:
                            opcionPila = 3
                    #termina while operaciones pila
            #termina while pila
        elif menuPrincipal == 3:
            linkedqueue=LinkedQueue()
            arrayqueue=ArrayQueue()
            opcionCola = 0
            while opcionCola != 3:
                print("------------------------------------------------")
                print("Menu Tipo de Cola","   1. Trabajar con ArrayQueue",
                    "   2. Trabajar con LinkedQueue",
                    "   3. Regresar al Menu Principal",sep='\n')
                
                opcionCola = int(verificarEntrada(input("Ingrese su opcion: ")))

                if opcionCola == 1:
                    pass
                    #insetar codigo con arrayqueue
                if opcionCola == 2:
                    pass
                    #insertar codigo con linkedqueue
                
                if opcionCola == 1 or opcionCola == 2:
                    operacionCola = 0

                    while operacionCola != 6:
                        print("------------------------------------------------")
                        print("Operaciones de Colas","   1. Encolar(Queue)",
                        "   2. Desencolar(Dequeue)",
                        "   3. Ver Tope(Top)",
                        "   4. Verificar si esta vacia",
                        "   5. Imprimir elementos",
                        "   6. Regresar al Menu Principal",sep='\n')
                        operacionCola = int(verificarEntrada(input("Ingrese su opcion: ")))

                        if operacionCola == 1:
                            if opcionCola == 1:
                                #insetar codigo con arrayqueue
                                data=input("Ingrese el elemento a encolar")
                                arrayqueue.queue(data)
                            if opcionCola == 2:
                                #insertar codigo con linkedqueue
                                data=input("Ingrese el dato que desea en el nuevo nodo")
                                linkedqueue.queue(data)
                        elif operacionCola == 2:
                            if opcionCola == 1:
                                #insetar codigo con arrayqueue
                                arrayqueue.deQueue()
                            if opcionCola == 2:
                                #insertar codigo con linkedqueue
                                linkedqueue.deQueue()
                        elif operacionCola == 3:
                            if opcionCola == 1:
                                #insetar codigo con arrayqueue
                                print(arrayqueue.front())
                            if opcionCola == 2:
                                #insertar codigo con linkedqueue
                                print(linkedqueue.front())
                        elif operacionCola == 4:
                            if opcionCola == 1:
                                #insetar codigo con arrayqueue
                                arrayqueue.isEmpty()
                            if opcionCola == 2:
                                #insertar codigo con linkedqueue
                                linkedqueue.isEmpty()
                        elif operacionCola == 5:
                            if opcionCola == 1:
                                #insetar codigo con arrayqueue
                                arrayqueue.mostrar()
                            if opcionCola == 2:
                                #insertar codigo con linkedqueue
                                linkedqueue.mostrar(linkedqueue)
                        elif operacionCola == 6:
                            opcionCola = 3
                    #termina while operaciones cola
            #termina while colas
    #termina while menu principal


main()


