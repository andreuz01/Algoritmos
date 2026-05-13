import numpy as np

#Función utilizada para debbugear e imprimir el calendario
def imprimir_calendario_debug(calendarios, semestre, titulo="CALENDARIO"):

    #Para borrar cada iteración
    #subprocess.run('cls', shell=True) #Para limpiar la pantalla al inicio de cada ejecución del código

    global debbugear
    if not debbugear:
        return

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    calendario = calendarios[semestre]["calendario"]

    ancho = 18
    ancho_total = (ancho + 3) * len(dias) + 1

    print("\n" + "=" * ancho_total)

    texto_titulo = f" {titulo} | Semestre {calendarios[semestre]['semestre']} "
    print(texto_titulo.center(ancho_total, "="))

    print("=" * ancho_total)

    # Encabezados
    for dia in dias:
        print(f"| {dia.center(ancho)}", end=" ")
    print("|")

    print("=" * ancho_total)

    # Filas
    for fila in range(calendario.shape[0]):

        for col in range(calendario.shape[1]):

            texto = str(calendario[fila][col]).strip()

            # Mejor visualización de vacíos
            if texto == "empty":
                texto = "-----"

            print(f"| {texto.center(ancho)}", end=" ")

        print("|")

    print("=" * ancho_total)
    print()


#from Proyecto_4 import *

#Aqui se guardan todas las listas de materias y profesores de prueba

profesores = [
    {"profesor": "Peniche", "horarios": [
        [True,  False,  False, True,  False],
        [False,  False,  True,  False, True],
        [False, True,  True,  True,  True]
    ]},

    {"profesor": "Aylin", "horarios": [
        [True,  False, True,  False,  True],
        [True,  True,  False, True,  False],
        [True,  True,  True,  False, False]
    ]},

    {"profesor": "Franklin", "horarios": [
        [False, True,  True,  False, True],
        [False,  True,  False, True,  True],
        [True,  False, True,  True,  False]
    ]},

    {"profesor": "Edson", "horarios": [
        [True,  True,  True,  False, True],
        [False, False,  True,  False,  True],
        [True,  False, True,  True,  False]
    ]},

    {"profesor": "Kenia", "horarios": [
        [True,  False, True,  True,  False],
        [False,  False,  True,  False, True],
        [False, True,  True,  True,  True]
    ]},

    {"profesor": "Vega", "horarios": [
        [False,  True,  False, False,  True],
        [False, True,  True,  True,  False],
        [True,  True,  False, True,  True]
    ]},

    {"profesor": "Bolio", "horarios": [
        [False, True,  True,  False,  False],
        [False,  False, True,  True,  True],
        [True,  True,  False, True,  True]
    ]},

    {"profesor": "Martinez", "horarios": [
        [True,  False, True,  True,  False],
        [True,  False,  False, False,  True],
        [False, True,  True,  False, True]
    ]},

    {"profesor": "Lopez", "horarios": [
        [True,  False,  False, True,  False],
        [False, True,  True,  True,  False],
        [True,  False, True,  False, True]
    ]},

    {"profesor": "Castro", "horarios": [
        [False, False,  True,  False, True],
        [True,  False, True,  True,  False],
        [True,  True,  False, True,  False]
    ]}
]

materias = [
    # Semestre 0
    {"materia": "Algebra",      "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[0], "salon": "151"},
    {"materia": "Calculo",      "bloques": 3, "computo": False,  "semestre": 0, "profesor": profesores[1], "salon": "151"},
    {"materia": "Redes",        "bloques": 2, "computo": True,  "semestre": 0, "profesor": profesores[2], "salon": "151"},
    {"materia": "Programacion", "bloques": 3, "computo": True,  "semestre": 0, "profesor": profesores[3], "salon": "151"},
    {"materia": "Ingles",       "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[4], "salon": "151"},
    {"materia": "Etica",        "bloques": 2, "computo": False, "semestre": 0, "profesor": profesores[5], "salon": "151"},

    # Semestre 1
    {"materia": "Algoritmos",   "bloques": 1, "computo": True, "semestre": 1, "profesor": profesores[6], "salon": "160"},
    {"materia": "Proyectos",    "bloques": 3, "computo": False, "semestre": 1, "profesor": profesores[7], "salon": "160"},
    {"materia": "Fisica",       "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[8], "salon": "160"},
    {"materia": "BasesDatos",   "bloques": 1, "computo": True,  "semestre": 1, "profesor": profesores[9], "salon": "160"},
    {"materia": "Circuitos",    "bloques": 3, "computo": True, "semestre": 1, "profesor": profesores[0], "salon": "160"},
    {"materia": "Probabilidad", "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[1], "salon": "160"},

    # Semestre 2
    {"materia": "Sistemas",     "bloques": 2, "computo": True, "semestre": 2, "profesor": profesores[2], "salon": "200"},
    {"materia": "Algebraa",     "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculoa",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 2, "computo": True,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 1, "computo": True, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3
    {"materia": "Redesa",       "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmosa",  "bloques": 2, "computo": True, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectosa",   "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 2, "computo": True,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 3, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]

computo = [
        {"horarios": np.full((3,5), True)},
        {"horarios": np.full((3,5), True)}
]

sandwich = False

#Horario(materias, computo, sandwich)

calendarios = [
        {"semestre": "2", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "4", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "6", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "8", "calendario": np.full((3,5), "empty".ljust(30))}
    ]

semestre = 0
debbugear = True
col = 0
calendarios[semestre]["calendario"][0][col] = "materia"
calendarios[semestre]["calendario"][1][col] = "vacío"
calendarios[semestre]["calendario"][2][col] = "materia"

cont = 0
conte = 0
if(sandwich == False):
        for i in range(3):
            if calendarios[semestre]["calendario"][i][col] == "vacío":
                    cont += 1+i
            if calendarios[semestre]["calendario"][i][col] == "empty".ljust(30):
                    conte += 1+i
        #BUG AQUI, se cambio el conte != 0 por conte == 0, ya que esto provoca que descarte ramas que sean (materia)(vacio)(empty) cuando realmente no son sandwiches
        if cont == 2 and conte == 0: 
            #Se elimina el error puesto y se realiza el backtracking
            #DEBUG imprimir el calendario original AL LLENAR UN VACÍO
            imprimir_calendario_debug(calendarios, semestre, "DEBUG")
            #calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
            #DEBUG imprimir el calendario original AL LLENAR UN VACÍO
            #imprimir_calendario_debug(calendarios, semestre, "DEBUG")
            