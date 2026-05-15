import numpy as np

semestre = 2

#Se crea a lista de días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

#Establece el ancho
ancho = 10
ancho_total = (ancho + 3) * len(dias) + 1

calendarios = [
    {"semestre": "2", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "4", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "6", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "8", "calendario": np.full((3,5), "empty".ljust(30))}
]

titulo="wea"

texto_titulo = f" {titulo} | Semestre {calendarios[semestre]['semestre']} "
print(texto_titulo.center(ancho_total, " "))