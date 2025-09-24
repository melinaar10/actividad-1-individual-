"""
Funciones para ordenar y mostrar los resultados en forma de tabla.
"""

def ordenar_por_puntos(acum: dict) # --> list[tuple[str, dict]]
    equipos = list(acum.items())                                   # pasa el diccionario a lista de tuplas
    equipos.sort(key=lambda item: item[1]["total"], reverse=True)  #mira el valor del campo total que está dentro del diccionario.
    return equipos

#devuelve una lista de equipos ordenados por "total" descendente

def mostrar_tabla(acum: dict, ronda_nro: int, mejor: tuple[str,int]) #--> None

#Imprime la tabla con innovacion, presentacion,errores,mejores y puntos totales.
#Resalta el mejor equipo de esa ronda




''' EJEMPLO DE SALIDA ESPERADA
=== Resultados después de la Ronda 2 ===
Mejor de la ronda: Equipo A (puntaje 12)

Equipo      Innov  Pres   Err  Mej    Total  
--------------------------------------------------
Equipo A    5      3      1    2      20    <==
Equipo B    4      2      0    0      14

'''