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


