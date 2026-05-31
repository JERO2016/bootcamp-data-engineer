# leccion_01.py
# Lección 01 — Estructuras de datos y Big-O
# Bootcamp Data Engineer Jr. | JERO2016

# Analiza un catálogo de empleados y retorna un resumen.

# Args:
    # empleados: Lista de dicts con datos de empleados.

# Returns:
    # Dict con las siguientes claves:
    # - "total": int — total de registros (incluyendo duplicados)
    # - "unicos": int — cantidad de RFCs únicos
    # - "duplicados": list[str] — RFCs que aparecen más de una vez
    # - "activos": int — empleados únicos con activo=True
    # - "por_departamento": dict[str, int] — {departamento: conteo de registros}
    # - "sueldo_promedio_activos": float — promedio de sueldo de empleados activos únicos

# Restricciones:
    # - NO uses pandas, numpy ni ninguna librería externa
    # - Solo estructuras nativas: list, dict, set, tuple
    # - La detección de duplicados debe ser O(n), no O(n²)


# Dataset de prueba — empleados con datos típicos de nómina
EMPLEADOS = [
    {"rfc": "TAOA870601", "nombre": "Ana Torres",    "departamento": "Nómina",  "sueldo": 18000, "activo": True},
    {"rfc": "ROLU920315", "nombre": "Luis Roca",     "departamento": "RH",      "sueldo": 22000, "activo": True},
    {"rfc": "TAOA870601", "nombre": "Ana Torres",    "departamento": "Nómina",  "sueldo": 18000, "activo": True},  # duplicado
    {"rfc": "GOPM881120", "nombre": "María Gómez",   "departamento": "RH",      "sueldo": 19500, "activo": False},
    {"rfc": "NUER950420", "nombre": "Pedro Núñez",   "departamento": "Nómina",  "sueldo": 21000, "activo": True},
    {"rfc": "HEML780312", "nombre": "Laura Herrera", "departamento": "Finanzas","sueldo": 25000, "activo": True},
    {"rfc": "ROLU920315", "nombre": "Luis Roca",     "departamento": "RH",      "sueldo": 22000, "activo": True},  # duplicado
    {"rfc": "CAGR910805", "nombre": "Jorge Castro",  "departamento": "Nómina",  "sueldo": 17500, "activo": True},
    {"rfc": "MOPE850220", "nombre": "Sara Morales",  "departamento": "Finanzas","sueldo": 28000, "activo": False},
    {"rfc": "VIJA960715", "nombre": "Diego Vidal",   "departamento": "RH",      "sueldo": 20000, "activo": True},
]

# Tu código aquí


def analizar_catalogo(empleados: list) -> dict:

# Paso 1: preparar acumuladores
    total = 0
    rfcs_vistos = set()
    rfcs_duplicados = set()
    activos_unicos = {}
    por_departamento = {}
    
# Paso 2: recorrer la lista    
    for empleado in empleados:
        
        rfc =  empleado["rfc"]
        departamento = empleado["departamento"]
        sueldo = empleado["sueldo"]
        activo = empleado["activo"]
        
# Paso 3: contar el total de registros
        total += 1
        
# Paso 4: Detectar únicos y duplicados
        if rfc in rfcs_vistos:
            rfcs_duplicados.add(rfc)
        else:
            rfcs_vistos.add(rfc)

# Paso 5: Contar por departamento
        por_departamento[departamento] = por_departamento.get(departamento, 0) + 1
        
# Paso 6: Registrar empleados activos únicos
        if activo == True:
            activos_unicos[rfc] = sueldo
    
# Paso 7: Calcular promedio de sueldos de activos únicos
    sueldos_activos = list(activos_unicos.values())
    if len(sueldos_activos) > 0:
        promedio = sum(sueldos_activos)/len(sueldos_activos)
    else:
        promedio = 0.0

# Paso 8: Construir y retornar resultados
    return {
        "total": total,
        "unicos": len(rfcs_vistos),
        "duplicados": list(rfcs_duplicados),
        "activos": len(activos_unicos),
        "por_departamento": por_departamento,
        "sueldo_promedio_activos": promedio
    }
    

def main():
    resultado = analizar_catalogo(EMPLEADOS)

    print("=" * 50)
    print("ANÁLISIS DE CATÁLOGO DE EMPLEADOS")
    print("=" * 50)
    print(f"Total de registros:       {resultado['total']}")
    print(f"RFCs únicos:              {resultado['unicos']}")
    print(f"RFCs duplicados:          {resultado['duplicados']}")
    print(f"Empleados activos únicos: {resultado['activos']}")
    print(f"Sueldo promedio activos:  ${resultado['sueldo_promedio_activos']:,.2f}")
    print(f"\nPor departamento:")
    for depto, conteo in resultado['por_departamento'].items():
        print(f"  {depto}: {conteo} registros")


if __name__ == "__main__":
    main()