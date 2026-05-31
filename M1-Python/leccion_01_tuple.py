# Crear una tupla - con paréntesis
configuracion_bd = ("localhost", 5432, "nomina_bd")
coordenadas = (19.4326, -99.1332)

# Acceder igual que una lista
host = configuracion_bd[0]
puerto = configuracion_bd[1]

print(host)
print(puerto)

# Intentar modificar truena - esto es intencional
# configuracion_bs[0] = TypeError: 'Tuple' object does not support item assignment

# Las funciones de python frecuentemente retornan tuplas
def calcular_sdi(sueldo_mensual, dias_aguinaldo, prima_vacacional):
    sd = sueldo_mensual / 30
    fi = 1 + (dias_aguinaldo/365) + (12/365) * (prima_vacacional / 100)
    sdi = sd * fi
    return sd, fi, sdi      # retorna una tupla implícita

sd, fi, sdi = calcular_sdi(18000, 15, 25)
print(f"SD: {sd:.2f}, FI: {fi:.4f}, SDI: {sdi:.2f}")