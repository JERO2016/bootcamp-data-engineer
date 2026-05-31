# Crear un diccionario
empleado = {
    "rfc": "TAOA870601",
    "nombre": "Ana Torres",
    "departamento": "Nómina",
    "sueldo_mensual": 18000,
    "activo": True
}

# Acceder a un valor por su clave
print(empleado["nombre"])             # "Ana Torres"
print(empleado["sueldo_mensual"])     # "18000"

# Acceso seguro - si la clave no existe, retorna None en vez de error
print(empleado.get("telefono"))         # None (no existe, pero no truena)
print(empleado.get("telefono", "N/A"))  # "N/A" valor por defecto

# Agregar o modificar 
empleado["email"] = "ana.torres@empresa.com"    # Nueva clave
empleado["sueldo_mensual"] = 20000              # modificar existente

# Verificar si una clave existe
if "rfc" in empleado:
    print ("Tiene un RFC registrado")
    
# Quitar una clave
del empleado["activo"]
sueldo = empleado.pop("sueldo_mensual")     # Quita y retorna el valor

# Recorrer claves y valores
for clave, valor in empleado.items():
    print(f"{clave}: {valor}")
    
# Solo las claves
for clave in empleado.keys():
    print(clave)
    
# Solo los valores
for valor in empleado.values():
    print(valor)


# Un dict de dicts - patrón muy común en RRHH:

# Catálogo de empleados indexado por RFC
catalogo = {
    "TAOA870601": {"nombre": "Ana Torres", "departamento": "Nómina", "sueldo": 18000},
    "ROLU920315": {"nombre": "Luis Roca",   "departamento": "RH",    "sueldo": 22000},
    "GOPM881120": {"nombre": "María Gómez", "departamento": "RH",    "sueldo": 19500},
}

# Buscar un empleado por RFC - instantáneo, sin importar cuántos haya
rfc_buscado = "ROLU920315"
if rfc_buscado in catalogo:
    emp = catalogo[rfc_buscado]
    print(f"Empleado: {emp['nombre']}, Depto: {emp['departamento']} ")