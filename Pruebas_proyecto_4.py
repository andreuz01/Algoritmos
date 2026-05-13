import numpy as np

#Aqui se guardan todas las matrices de prueba

#Listas de pruebas
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
    {"materia": "Circuitos",    "bloques": 3, "computo": False, "semestre": 1, "profesor": profesores[0], "salon": "160"},
    {"materia": "Probabilidad", "bloques": 2, "computo": False, "semestre": 1, "profesor": profesores[1], "salon": "160"},

    # Semestre 2
    {"materia": "Sistemas",     "bloques": 2, "computo": True, "semestre": 2, "profesor": profesores[2], "salon": "200"},
    {"materia": "Algebraa",     "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculoa",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 2, "computo": False,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3
    {"materia": "Redesa",       "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmosa",  "bloques": 2, "computo": True, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectosa",   "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 2, "computo": True,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 1, "computo": False, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 3, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]