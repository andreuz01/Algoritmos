import numpy as np

#Archivo donde se guardan todas las listas de materias y profesores de prueba
#Igualmente se documentan sus soluciones como tiempos aproximados de ejecución
#Los tiempos aproximados son el más bajo de acuerdo al tiempo que tardo en encontrar una solución aceptando sandwiches
#Los tiempos máximos son los que tardó en encontrar una solución rechazando sándwiches

#Los resultados de las pruebas están guardados en archivos txt con su nombre de prueba y el tipo
#cS (con Sandwich) y sS (sin Sandwich)

#weaman3000

#--------------------Listas de pruebas--------------------

#----------Prueba original----------
#Tiempo aproximado (1 seg - 1 seg)
profesores = [
    {"profesor": "Peniche", "horarios": [
        [False, True, False, True, True],
        [True, True, False, True, True],
        [False, True, True, True, True]
    ]},

    {"profesor": "Aylin", "horarios": [
        [True, True, True, True, True],
        [True, False, True, False, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Franklin", "horarios": [
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, False, True, True]
    ]},

    {"profesor": "Edson", "horarios": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Kenia", "horarios": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Vega", "horarios": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Bolio", "horarios": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Martinez", "horarios": [
        [True, False, True, True, True],
        [True, True, True, True, False],
        [True, True, True, True, True]
    ]},

    {"profesor": "Lopez", "horarios": [
        [True, True, False, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True]
    ]},

    {"profesor": "Castro", "horarios": [
        [True, True, True, True, False],
        [True, False, True, True, True],
        [True, True, True, False, True]
    ]}
]

materias = [
    # Semestre 0
    {"materia": "Calculo",      "bloques": 3, "computo": False,  "semestre": 0, "profesor": profesores[1], "salon": "151"},
    {"materia": "Algebra",      "bloques": 3, "computo": False, "semestre": 0, "profesor": profesores[0], "salon": "151"},
    {"materia": "Redes",        "bloques": 2, "computo": False,  "semestre": 0, "profesor": profesores[2], "salon": "151"},
    {"materia": "Programacion", "bloques": 3, "computo": True,  "semestre": 0, "profesor": profesores[3], "salon": "151"},
    {"materia": "Ingles",       "bloques": 2, "computo": False, "semestre": 0, "profesor": profesores[4], "salon": "151"},
    {"materia": "Etica",        "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[5], "salon": "151"},

    # Semestre 1
    {"materia": "Algoritmos",   "bloques": 3, "computo": False, "semestre": 1, "profesor": profesores[6], "salon": "160"},
    {"materia": "Proyectos",    "bloques": 3, "computo": False, "semestre": 1, "profesor": profesores[7], "salon": "160"},
    {"materia": "Fisica",       "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[8], "salon": "160"},
    {"materia": "BasesDatos",   "bloques": 3, "computo": True,  "semestre": 1, "profesor": profesores[9], "salon": "160"},
    {"materia": "Circuitos",    "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[0], "salon": "160"},
    {"materia": "Probabilidad", "bloques": 1, "computo": False, "semestre": 1, "profesor": profesores[1], "salon": "160"},

    # Semestre 2
    {"materia": "Sistemas",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[2], "salon": "200"},
    {"materia": "Algebraa",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculoa",     "bloques": 2, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 3, "computo": True,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 2, "computo": False, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3
    {"materia": "Redesa",       "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmosa",  "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectosa",   "bloques": 2, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 3, "computo": False,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 2, "computo": False, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 1, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]

#----------Prueba1----------
#Tiempo aproximado (2 mins - 30 mins)
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
    # Semestre 0, requieren 12 bloques, o sea 3 vacíos
    {"materia": "Algebra",      "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[0], "salon": "151"},
    {"materia": "Calculo",      "bloques": 3, "computo": False,  "semestre": 0, "profesor": profesores[1], "salon": "151"},
    {"materia": "Redes",        "bloques": 2, "computo": True,  "semestre": 0, "profesor": profesores[2], "salon": "151"},
    {"materia": "Programacion", "bloques": 3, "computo": True,  "semestre": 0, "profesor": profesores[3], "salon": "151"},
    {"materia": "Ingles",       "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[4], "salon": "151"},
    {"materia": "Etica",        "bloques": 2, "computo": False, "semestre": 0, "profesor": profesores[5], "salon": "151"},

    # Semestre 1, requieren 12 bloques, o sea 3 vacíos
    {"materia": "Algoritmos",   "bloques": 1, "computo": True, "semestre": 1, "profesor": profesores[6], "salon": "160"},
    {"materia": "Proyectos",    "bloques": 3, "computo": False, "semestre": 1, "profesor": profesores[7], "salon": "160"},
    {"materia": "Fisica",       "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[8], "salon": "160"},
    {"materia": "BasesDatos",   "bloques": 1, "computo": True,  "semestre": 1, "profesor": profesores[9], "salon": "160"},
    {"materia": "Circuitos",    "bloques": 3, "computo": True, "semestre": 1, "profesor": profesores[0], "salon": "160"},
    {"materia": "Probabilidad", "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[1], "salon": "160"},

    # Semestre 2, requieren 12 bloques, o sea 3 vacíos
    {"materia": "Sistemas",     "bloques": 2, "computo": True, "semestre": 2, "profesor": profesores[2], "salon": "200"},
    {"materia": "Algebraa",     "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculoa",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 2, "computo": True,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 1, "computo": True, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3, requieren 12 bloques, o sea 3 vacíos
    {"materia": "Redesa",       "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmosa",  "bloques": 2, "computo": True, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectosa",   "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 2, "computo": True,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 3, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]

#----------Prueba 2----------
#Tiempo aproximado (30 segs - 2 mins)
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
    # Semestre 0, lleva 10 modulos
    {"materia": "Algebra",      "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[0], "salon": "151"},
    {"materia": "Calculo",      "bloques": 2, "computo": False,  "semestre": 0, "profesor": profesores[1], "salon": "151"},
    {"materia": "Redes",        "bloques": 3, "computo": True,  "semestre": 0, "profesor": profesores[2], "salon": "151"},
    {"materia": "Programacion", "bloques": 2, "computo": True,  "semestre": 0, "profesor": profesores[3], "salon": "151"},
    {"materia": "Ingles",       "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[4], "salon": "151"},
    {"materia": "Etica",        "bloques": 1, "computo": False, "semestre": 0, "profesor": profesores[5], "salon": "151"},

    # Semestre 1, requiere 10 modulos
    {"materia": "Algoritmos",   "bloques": 1, "computo": True, "semestre": 1, "profesor": profesores[6], "salon": "160"},
    {"materia": "Proyectos",    "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[7], "salon": "160"},
    {"materia": "Fisica",       "bloques": 1, "computo": False, "semestre": 1, "profesor": profesores[8], "salon": "160"},
    {"materia": "BasesDatos",   "bloques": 3, "computo": True,  "semestre": 1, "profesor": profesores[9], "salon": "160"},
    {"materia": "Circuitos",    "bloques": 2, "computo": True, "semestre": 1, "profesor": profesores[0], "salon": "160"},
    {"materia": "Probabilidad", "bloques": 1, "computo": False, "semestre": 1, "profesor": profesores[1], "salon": "160"},

    # Semestre 2, requieren 10 modulos
    {"materia": "Sistemas",     "bloques": 1, "computo": True, "semestre": 2, "profesor": profesores[2], "salon": "200"},
    {"materia": "Algebraa",     "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculoa",     "bloques": 2, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 1, "computo": True,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 3, "computo": True, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 2, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3, requieren 10 bloques
    {"materia": "Redesa",       "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmosa",  "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectosa",   "bloques": 2, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 1, "computo": True,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 3, "computo": True, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 2, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]