"""
1. Contador simple
o Muestra los números del 1 al 10 usando un bucle for.
2. Cuenta atrás
o Muestra los números del 10 al 1 usando range() con paso negativo.
3. Suma de los primeros 100 números
o Usa un bucle for para sumar del 1 al 100.
4. Validación de entrada
o Pide una contraseña hasta que el usuario escriba la correcta
(while).
"""


def contador():
    for i in range(1, 11):
        print(i)


contador()

print("Fin del programa")

print("--------------------\n")


def contador_atras():
    for i in range(10, 0, -1):
        print(i)

contador_atras()

print("Fin del programa")

print("--------------------\n")


def sumaBucleFor():
    # almacenamos el valor de la suma
    suma = 0
    for i in range(1, 101):
        suma += i
    print(suma)
    return suma


sumaBucleFor()

print("Fin del programa")

print("--------------------\n")


def validacionContraseña():
    key = 1234
    userKey = int(input("Introduce la key"))

    while userKey != key:
        userKey = int(input("La key es incorrecta, introduce la key nuevamente"))


validacionContraseña()
