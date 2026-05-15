# me dio una funcion muy bonita que grafica una barra de progreso en la terminal, la quite por que no se explicarla
# pero no quería perderla
# Si se quiere poner se pone justo despues del contador de iteraciones
    
#variables random que no sirven:
iteraciones = 0
pos = 0

#PRUEBA barra de progreso de chatty

#Actualiza la barra solo cada cierta cantidad de iteraciones
#para no afectar demasiado el rendimiento
if iteraciones % 10000 == 0:

    #Calcula el progreso de profundidad actual
    porcentaje_pos = pos / 60

    #Cantidad de bloques llenos de la barra (20 bloques)
    bloques = int(porcentaje_pos * 20)

    #Construcción visual de la barra
    barra = "*" * bloques + "-" * (20 - bloques)

    #Imprime sobre la misma línea
    print(
        f"\r[{barra}] "
        f"Posición: {pos}/60 | "
        f"Iteraciones: {iteraciones}",
        end=""
    )