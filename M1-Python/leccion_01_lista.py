# Crear una lista
empleados = ["Ana Torres", "Luis Roca", "Carlos Gómez", "Ana Torres"]

# Acceder por posición (el índice empieza en 0, no en 1)

print(empleados[0]) # "Ana Torres" - el primero
print(empleados[2]) # "Carlos Gómez" - el tercero
print(empleados[-1]) # "Ana Torres" - el último (índice negativo = desde el final)

# Agregar elementos 
empleados.append("María Núñez") # Al final - rápido
empleados.insert(0, "Director RH") # Al inicio - lento


# Quitar elementos
empleados.remove("Luis Roca") # Busca y quita la primera ocurrencia
ultimo = empleados.pop() # Quita y retorna el último elemento


# Verificar si algo si algo existe
if "Ana Torres" in empleados:
    print("Está en lista")

# Tamaño de la lista
print(len(empleados)) # Número de empleados


# Rebanar (slicing) - obtener una parte de la lista
primeros_tres = empleados[0:3] # del índice 0 al 2 (el 3 no se incluye)
desde_el_segundo = empleados[1:] # del índice 1 hasta el final


print(empleados)