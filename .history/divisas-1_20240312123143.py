#CALCULO Y OONVERSION DE DIVISAS

import sys, os
def limpiar():
    os.system('cls') if os.name == 'nt' else 'clear'


limpiar()       #LLAMADA LA F. DE LIMPIAR LA TERMINAL
# VALORES DE CONVERSION MONEDAS

sol_peru = sys.argv[1]
peso_arge = sys.argv[2]
dola_usa = sys.argv[3]
clp_conversion = sys.argv[4] #paso de plata chilena para convertir


#print(int(sol_peru) * 2, int(peso_arge) * 3, int(dola_usa) // 2)

sol_peru = float(sys.argv[1])  # Convertir a float
peso_arge = float(sys.argv[2])  # Convertir a float
dola_usa = float(sys.argv[3])  # Convertir a float por la division

#
clp_conversion = float(sys.argv[4])

# Realizar las operaciones
resultado_sol = sol_peru * clp_conversion
resultado_peso = peso_arge * clp_conversion
resultado_dolar = dola_usa * clp_conversion


print("******************************************************")
print("**************R E S U L T A D O S********************")
print(f"Tus resultado para:$ \033[1m{clp_conversion}\033[0m")
print(f"\033[41mEn soles pé:\033[0m \033[1m{resultado_sol}\033[0m")
print(f"\033[42mPa los CHÉ argentinos:\033[0m \033[1m{resultado_peso}\033[0m")
print(f"\033[43mY en dólares gringos:\033[0m \033[1m{resultado_dolar}\033[0m")

#