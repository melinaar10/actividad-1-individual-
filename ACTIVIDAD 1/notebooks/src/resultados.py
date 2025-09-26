"""
Contiene funciones para ordenar los equipos y mostrar los resultados. 
Busqué como mostrar formatos ordenados
"""

def ordenar_por_puntos(acum: dict):  # --> list[tuple[str, dict]]
    equipos = list(acum.items())  # pasa el diccionario a lista de tuplas
    equipos.sort(key=lambda item: item[1]["total"], reverse=True)  # ordena por el campo total
    return equipos

def mostrar_tabla(acum: dict, ronda_nro: int, mejor: tuple[str, int]):  # --> None
    print("\n-------------------------------------------")
    print(f"Ronda {ronda_nro}")
    print(f"Mejor Equipo de la Ronda: {mejor[0]} ({mejor[1]} puntos)")
    print("-------------------------------------------")
    print("Equipo     Innovación  Presentación  Errores  Mejores  Total")

    equipos_ordenados = ordenar_por_puntos(acum)
    for nombre, datos in equipos_ordenados:
        print(f"{nombre:<10} {datos['innovacion']:^11} {datos['presentacion']:^13} "
              f"{datos['errores']:^7} {datos['mejores']:^8} {datos['total']:^6}")

# inciso extra: equipos sin errores
def equipos_sin_errores(acum: dict) -> list[str]:
    """Devuelve una lista con los nombres de equipos que nunca tuvieron errores."""
    return list(
        map(lambda item: item[0],
            filter(lambda item: item[1]["errores"] == 0, acum.items()))
    )

# inciso extra: top 2 equipos finales
def top_2_equipos(acum: dict) -> list[tuple[str, int]]:
    """Devuelve los dos equipos con más puntos totales (nombre, puntaje)."""
    equipos_ordenados = ordenar_por_puntos(acum)
    return [(nombre, datos["total"]) for nombre, datos in equipos_ordenados[:2]]
