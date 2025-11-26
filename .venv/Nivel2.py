"""
5. Números pares del 1 al 20
o Usa continue para saltar los impares.
6. Busca el primer múltiplo de 7 mayor que 100
o Usa un bucle while y break.
7. Contador de vocales
o Pide una palabra y cuenta cuántas vocales tiene.
8. Menú interactivo
o Crea un menú con opciones (1. Saludar, 2. Sumar, 3. Salir) que se
repita hasta que el usuario elija salir.
9. Bucle con else
o Recorre una lista de números y busca el 0. Si no lo encuentra,
muestra un mensaje con else.
"""


def pares():
    for i in range(2, 21, 2):  # inicio, fin, paso
        print(i)


pares()

print("Fin del programa")

print("--------------------\n")


def multiplo7():
    resultado = 0
    multiplo = 0
    i = 1

    while resultado < 100:
        multiplo = i
        resultado = multiplo * i
        i += 1

    print(f"El primer múltiplo de 7 que da un resultado mayor a 100 es: {multiplo}")


multiplo7()

print("Fin del programa")

print("--------------------\n")


def contadorVocales():
    print("Introduce una palabra:")
    palabra = input().lower()

    vocales = "aeiou"
    contador = 0

    for letra in palabra:  # se asigna cada letra de la palabra a la variable temporal letra
        if letra in vocales:
            contador += 1

    print("La palabra tiene ", contador, "vocales")


contadorVocales()

print("Fin del programa")

print("--------------------\n")


def menuInteractivo():
    print("Elige una de estas opciones:")
    # mientras sea verdadero lo repite
    while True:
        print("1. Saludar")
        print("2. Sumar")
        print("3. Salir")

        opcion = input("Introduce una opcion")
        if opcion == "1":
            print("Hola")
        elif opcion == "2":
            print("Suma")
        # en el caso de que no seleccione la opcion 3 sale del bucle
        else:
            break


menuInteractivo()

print("Fin del programa")

print("--------------------\n")


def bucleElse():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in lista:
        if i == 0:
            break
        else:
            print("El numero 0 no se encuentra en la lista")


bucleElse()

print("Fin del programa")

print("--------------------\n")
