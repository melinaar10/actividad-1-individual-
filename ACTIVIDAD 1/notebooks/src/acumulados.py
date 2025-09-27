"""
Contiene funciones para inicializar y actualizar los acumulados por equipo.
"""

def resetear_valores(): #-> diccionario
    return {"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}

def inicializar_acumulados(evaluaciones):   
    equipos = evaluaciones[0].keys()
    acumulados = dict(map(lambda equipo: (equipo, resetear_valores()), equipos))    #map recorre la lista de equipos(nombres), lambda recibe el argumento del nombre del equipo,
    return acumulados                                                               #y con el diccionario reseteado por la función, crea una tupla ("Nombre Equipo",{"innovacion":0,"errores":0,...}), luego esa lista de tuplas es dict()
                                                                                                          
def actualizar_acumulados(acum: dict, ronda: dict, mejor: str) -> dict: 
    for equipo in ronda:
        acum[equipo]["innovacion"] += ronda[equipo]["innovacion"]
        acum[equipo]["presentacion"] += ronda[equipo]["presentacion"]

        if (equipo == mejor):
            acum[equipo]["mejores"] += 1

        acum[equipo]["total"] += (ronda[equipo]["innovacion"]*3 + ronda[equipo]["presentacion"]*1)

        if ronda[equipo]["errores"]:
            acum[equipo]["errores"] += 1
            acum[equipo]["total"] -= 1

#acum es un diccionario {nombre_equipo: acumulados entre todas las rondas}