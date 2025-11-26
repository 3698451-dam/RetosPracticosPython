"""
Nivel 3: Aplicaciones reales
10.Procesar una lista de alumnos
o Dada una lista de nombres, muestra solo los que empiezan por
vocal.
11.Simulación de intentos de login
o Permite 3 intentos para introducir usuario y contraseña correctos.
12.Generador de contraseñas
o Genera 5 contraseñas aleatorias de 8 caracteres usando un bucle.
13.Filtrar archivos por extensión
o Dada una lista de nombres de archivo, muestra solo los .pdf.
14.Contador de palabras
o Pide una frase y cuenta cuántas palabras contiene.
"""

import random
import string

nombres = ["Marisa", "Felipa", "Alberta", "Petra"]


def nombresConVocal(nombres):
    for nombre in nombres:
        if nombre[0] in "aeiouAEIOU":
            print("El nombre que contiene una vocal es: ", nombre, "\n")


nombresConVocal(nombres)

print("Fin del programa")

print("--------------------\n")


def intentosLogin():

    print("Tienes 3 intentos para introducir tus datos")

    intentos = 3
    contador = 1

    for i in range(intentos):
        print("introduce tu usuario")
        usuario = input()
        print("introduce tu contraseña")
        key = input()

        if usuario == "admin" and key == "1234":
            print("Bienvenido")
            break

        else:
            print(
                "Las claves no coinciden, te quedan ",
                intentos - contador,
                " intentos \n",
            )
            contador += 1

    else:
        print("Lo siento te has quedado sin intentos\n")


intentosLogin()

print("Fin del programa")

print("--------------------\n")


def generadorKeys():

    # le vamos a decir que queremos letras y numeros por eso importamos todo el paquete string
    caracteres = string.ascii_letters + string.digits

    # declaramos la longitud de la clave
    longitudClave = 8

    for key in range(5):
        # usamos random para generar de forma aleatoria los caracteres
        # usamos la funcion join para unir los caracteres aleatorios
        randomKey = "".join(random.choice(caracteres) for i in range(longitudClave))
        print("Las claves generadas son: ", randomKey, "\n")


generadorKeys()

print("Fin del programa")

print("--------------------\n")


def filtroExtension():
    archivos = [
        "informe.docx",
        "tarea1.pdf",
        "presupuesto.xlsx",
        "contrato.pdf",
        "foto.jpg",
    ]

    # Filtramos los archivos que terminan en .pdf
    archivos_pdf = []

    # recorremos la lista archivos
    for nombre_archivo in archivos:
        # si termina en .pdf lo agregamos al final de la lista con append
        if nombre_archivo.endswith(".pdf"):
            archivos_pdf.append(nombre_archivo)

    print(archivos_pdf)


filtroExtension()

print("Fin del programa")

print("--------------------\n")


def contadorPalabras():

    print("Introduce una frase:")
    frase = input()

    # con .split vamos a separar la frase en palabras
    palabras = frase.split()

    # con "len" vamos a contar cuantas palabras tiene la frase
    print("La frase tiene ", len(palabras), "palabras")
