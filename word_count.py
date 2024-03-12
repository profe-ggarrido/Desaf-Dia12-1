# DESAFIO ESTRUCT DE DATOS - FUNCIONES P I
#---------------------------------------

#OPCIONES DE CONSOLA
#-------------------

import os

import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

"""
INDICACIONES GENERALES
Genere un archivo llamado word_count.py que importe un texto a Python y realice las 
siguientes tareas:
● Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres 
    distintos que componen un texto.
● Cuente el número de palabras distintas que componen el texto ingresado. 
    Para separar un texto por espacios puede utilizar el método .split("").
"""

#CONECTAR CON UN ARCHIVO, LUEGO DE ABRIT Y PROCESAR EN MODO LECTURA, SE CIERRA
# CONTROLAR SI EL ARCHIVO EXISTE O ESTA MA ESCRITO
try:   
    with open("lorem_ipsum.txt", "r") as file: 
        texto=file.read()

    # Contar palabras distintas
    palabras = texto.split()  # Dividir el texto en palabras
    palabras_distintas = set(palabras)  # Crear un conjunto de palabras únicas
    cantidad_palabras_distintas = len(palabras_distintas)
    print(f"Número de palabras distintas: {cantidad_palabras_distintas}")

    # Contar caracteres diferentes
    caracteres_distintos = set(texto)  # Crear un conjunto de caracteres únicos
    cantidad_caracteres_distintos = len(caracteres_distintos)
    print(f"Número de caracteres diferentes: {cantidad_caracteres_distintos}")


except FileNotFoundError:
    print("El archivo no se encontró....")


print("************** GAME OVER ******************")
