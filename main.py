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

                if opcionLista == 1:
                    pass
                    #insertar codigo con ArrayList
                elif opcionLista == 2:
                    pass
                    #insertar codigo con LinkedList
                
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

                        if operacionLista == 1:
                            pass
                        elif operacionLista == 2:
                            pass
                        elif operacionLista == 3:
                            pass
                        elif operacionLista == 4:
                            pass
                        elif operacionLista == 5:
                            pass
                        elif operacionLista == 6:
                            pass
                        elif operacionLista == 7:
                            pass
                        elif operacionLista == 8:
                            pass
                        elif operacionLista == 9:
                            pass
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

                symbol = ' '

                if opcionPila == 1:
                    pass
                    #insertar codigo de Pila
                if opcionPila == 2:
                    pass
                    #insertar codigo Pila

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
                            pass
                        elif operacionesPila == 2:
                            pass
                        elif operacionesPila == 3:
                            pass
                        elif operacionesPila == 4:
                            pass
                        elif operacionesPila == 5:
                            pass
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


