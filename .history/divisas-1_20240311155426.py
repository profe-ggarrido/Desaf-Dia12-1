import sys, os
def limpiar():
    os.system('cls') if os.name == 'nt' else 'clear'



# VALORES DE CONVERSION MONEDAS

sol_peru = sys.argv[1]
peso_arge = sys.argv[2]
dola_usa = sys.argv[3]

#print(int(sol_peru) * 2, int(peso_arge) * 3, int(dola_usa) // 2)

sol_peru = float(sys.argv[1])  # Convertir a float
peso_arge = float(sys.argv[2])  # Convertir a float
dola_usa = float(sys.argv[3])  # Convertir a float

# Realizar las operaciones
resultado_sol = sol_peru * 2
resultado_peso = peso_arge * 3
resultado_dolar = dola_usa / 2


print(f"Resultado en soles: {resultado_sol}")
print(f"Resultado en pesos argentinos: {resultado_peso}")
print(f"Resultado en dólares estadounidenses: {resultado_dolar}")

#limpiar()