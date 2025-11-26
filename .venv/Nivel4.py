"""

Nivel 4: Retos
15.Número primo
o Pide un número y determina si es primo usando un bucle.
16.Adivina el número
Fundamentos de programación en Python
UT3: Estructuras de control
o Juego donde el usuario tiene que adivinar un número secreto entre
1 y 100.
17.Conversor de temperaturas
o Muestra una tabla de conversión de °C a °F del 0 al 100 en pasos
de 10.
18.Simulación de cajero automático
o Pide un importe y muestra cuántos billetes de cada tipo se
necesitan (500, 200, 100…).
19.Animación de carga
o Simula una barra de carga con print() y time.sleep().


"""
import sys
import time


def numerosPrimos():

   print("Introduce un numero para saber si es primo")
   numero = int(input())

   for i in range(2, numero):
       if numero % i == 0:
           print(f"{numero} no es primo")
           break
   else:
       print(f"{numero} es primo")

numerosPrimos()


def adivinaNumero():
   import random
   #mediante el metodo random generamos un numero aleatorio entre 1 y 100
   numero = random.randint(1, 100)
   #lo dejo para que se pueda comprobar el numero aleatorio
   print(numero)

   print("Adivina el numero entre 1 y 100")
   adivina = int(input())

   if adivina == numero:
       print("Ganaste")
   else:
       print("Perdiste")

adivinaNumero()



def conversorTemperatura():
   print("Tabla de Conversión de Temperatura")
   print("-" * 35)
   print("Celsius °C - Fahrenheit °F")

   # Itera de 0 a 100, con pasos de 10
   for celsius in range(0, 101, 10):
       #formula para la conversion
       fahrenheit = (celsius * 9 / 5) + 32

       print(f"| {celsius:12} | {fahrenheit:15.1f} |")

       print("-" * 35)

conversorTemperatura()


def simulacionCajero():
   billetes = [500, 200, 100, 50, 20, 10, 5]

   while True:
       try:
           # Le pedimos el importe al usuario
           importe = int(input("Introduce el importe total"))
           if importe < 5:
               print("El importe debe ser 5€ o más.")
               continue
           break
       except ValueError:
           print("Por favor, introduce un número entero.")

   restante = importe
   print(f"\nImporte a desglosar: {restante} €")
   print("-" * 30)


   for valor in billetes:

       cantidad = restante // valor

       if cantidad > 0:

           print(f"-> {cantidad} billetes de {valor}€")

           #Actualiza el restante
           restante = restante % valor


   if restante > 0:
       print(f"\n* Resto no cubierto (menos de 5€): {restante}€")

   print("-" * 30)
   print("Desglose completado.")

simulacionCajero()


#Este ejercicio no sabia hacerlo y he tenido que buscarlo
def simular_barra_carga(pasos=10, duracion_paso=0.3):
   """
   Simula una barra de carga simple con print() y time.sleep().
   """

   ancho_barra = 30  # Ancho total de la barra (ej: 30 caracteres)

   print("\nIniciando proceso...")

   for i in range(pasos + 1):
       # Calcular el porcentaje y el número de caracteres llenos
       porcentaje = (i / pasos) * 100
       lleno = int(ancho_barra * i / pasos)
       vacio = ancho_barra - lleno

       # Construir la barra de carga: [######-----]
       barra = "[" + "#" * lleno + "-" * vacio + "]"

       # El caracter '\r' (retorno de carro) permite sobrescribir la línea
       # anterior, creando el efecto de "carga".
       # 'end=""' evita el salto de línea.
       # sys.stdout.flush() fuerza la impresión inmediata.
       sys.stdout.write(f"\rCargando: {barra} {porcentaje:.0f}%")
       sys.stdout.flush()

       # Esperar la duración especificada antes del siguiente paso
       time.sleep(duracion_paso)

   print("\nProceso completado. ✅")

simular_barra_carga()