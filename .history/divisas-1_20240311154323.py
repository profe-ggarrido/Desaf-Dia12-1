import sys, os
def limpiar():
    os.system('cls') if os.name == 'nt' else 'clear'
limpiar()


# VALORES DE CONVERSION MONEDAS

sol_peru = sys.argv[1]
peso_arge = sys.argv[2]
dola_usa = sys.argv[3]

#print(int(sol_peru) * 2, int(peso_arge) * 3, int(dola_usa) // 2)

sol_peru = float(sys.argv[1])  # Convertir a float
peso_arge = float(sys.argv[2])  # Convertir a float
dola_usa = float(sys.argv[3])  # Convertir a float



