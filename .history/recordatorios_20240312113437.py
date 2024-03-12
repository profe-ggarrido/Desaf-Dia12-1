# DESAFIO CON MANEJO DE DICCIONARIOS
# Disponibilizar estos elementos en Python

from unidecode import unidecode

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#PUNTO 1: Nuevo evento a agregar
nuevo_evento = ['2021-02-02', '06:00', 'Empezar el año']

# Agregar el nuevo evento a la lista
recordatorios.append(nuevo_evento)  #AGREGO LA NUEVA FECHA


# PUNTO 2 CAMBIO/MOFIFICACION DE LISTAS
# Nuevo evento a agregar (corrección)
nuevo_evento = ['2021-07-16', '13:00', 'No hacer nada es feriado']

# Reemplazar el evento incorrecto/modificado en la lista
for i, evento in enumerate(recordatorios):  #conversion a objeto ENUMERADO PARA ITERARLO
    if evento[0] == '2021-07-15':   # BUSCANDO POR FECHA
        recordatorios[i] = nuevo_evento


#PUNTO 3 : ELIMINACION DEL DIA DEL TRABAJO (1 MAYO 2021)

# Fecha a eliminar
fecha_a_eliminar = '2021-05-01'

# Filtrar los elementos que no coinciden con la fecha a eliminar
recordatorios = [evento for evento in recordatorios if evento[0] != fecha_a_eliminar]



# Ordenar la lista de recordatorios por la fecha (primer componente)
recordatorios.sort(key=lambda x: x[0])


# Imprimir la lista actualizada
for evento in recordatorios:
    print(evento)



# Output
print("*************************************************")
print(f"Ya no tenemos el dia: {fecha_a_eliminar}, luego nps quedan: ")
print(recordatorios[0])
