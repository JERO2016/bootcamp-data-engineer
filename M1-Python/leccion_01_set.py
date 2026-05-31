# Crear un set
rfcs_procesados = {"TAOA870601", "ROLU920315", "GOPM881120"}

# Agregar elementos
rfcs_procesados.add("NUER950420")
rfcs_procesados.add("TAOA870601")   # ya existe - lo ignora silenciosamente

print(rfcs_procesados)  # Sigue siendo los mismos 4 elementos, no 5

# Verificar si algo existe - 0(1), instantáneo
if "ROLU920315" in rfcs_procesados:
    print("Ya fue procesado")
    
# Quitar
rfcs_procesados.discard("GOPM881120") # Si no existe, no truena (a diferencia de remove)
print(rfcs_procesados)

# Convertir lista a set para eliminar duplicados
lista_con_dupes = ["TAOA870601", "ROLU920315", "TAOA870601", "GOPM881120", "ROLU920315"]
sin_duplicados = set(lista_con_dupes)
print(sin_duplicados)   # {'TAOA870601', 'ROLU920315', 'GOPM881120'}
print(len(lista_con_dupes))     # 5
print(len(sin_duplicados))      #3

# Operaciones de conjuntos - MUY útiles en ETL
empleados_ayer = {"TAOA870601", "ROLU920315", "GOPM881120"}
empleados_hoy  = {"ROLU920315", "GOPM881120", "NUER950420"}

nuevos_hoy = empleados_hoy - empleados_ayer         # diferencia: {'NUER950420'}
en_ambos_dias = empleados_hoy & empleados_ayer      # intersección: {'ROLU920315', 'GOPM881120'}
todos_los_dias = empleados_hoy | empleados_ayer     # unión: todos juntos sin duplicados
solo_en_uno = empleados_hoy ^ empleados_ayer        # diferencia simétrica: los que no coinciden

print(solo_en_uno)