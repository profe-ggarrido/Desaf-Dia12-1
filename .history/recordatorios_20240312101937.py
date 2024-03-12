# DESAFIO CON MANEJO DE DICCIONARIOS
# Disponibilizar estos elementos en Python

from unidecode import unidecode

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Nuevo evento a agregar
nuevo_evento = ['2021-02-02', '06:00', 'Empezar el año']

# Agregar el nuevo evento a la lista
recordatorios.append(nuevo_evento)

# Imprimir la lista actualizada
for evento in recordatorios:
    print(evento)



# Output
#print(recordatorios)
