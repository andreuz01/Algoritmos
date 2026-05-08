import numpy as np

def Horario_impl(pos, calendarios, materias, computo, sandwich):
    #Variables
    n_materias = len(materias)

    semestre = pos //15
    localpos = pos %15

    col = localpos % 5
    row = localpos // 5

    #Detenerse al llegar a la ultima poscición
    if pos == 60:
        cont=0
        for i in range(n_materias):
            if materias[i]["bloques"]==0:
                cont+=1   
        if cont== n_materias:
            return True
        else:
            return False

    #Checa espacios libres suficientes
    #(Cuenta el numero de espacios validos para poner una materia y cuenta cuantas materias aun no se ponen)
    espacios_validos = 0
    modulos = 0
    for m in range(n_materias):
        if materias[m]["semestre"] == semestre:
            if materias[m]["bloques"] != 0:
                modulos += materias[m]["bloques"] 

    for x in range(3):
        for y in range(5):
            if calendarios[semestre]["calendario"][x][y] == "empty".ljust(30):
                espacios_validos += 1
                    
    if modulos > espacios_validos:
        return False

    
    #Función principal
    for num in range(n_materias):
        #Inicializar
        invalido = False
        indexcomp = None

        #Si la materia es de otro semestre o ya no le quedan clases que usar la salta
        if materias[num]["semestre"] != semestre or materias[num]["bloques"] == 0:
            continue
        
        #Si en esta hora el maestro esta ocupado en otro semestre se salta esta iteración
        if materias[num]["profesor"]["horarios"][row][col] == False:
                continue 

        #Checa si ya esta guardada esta materia en esta columna
        #Si ya se usa la materia en el dia se salta a la siguiente iteración
        for i in range(3):
            if materias[num]["materia"] == calendarios[semestre]["calendario"][i][col]:
                invalido = True
                break
        if invalido:
            continue
        
        #Si la materia que estamos probando usa el salon de computo checar si esta disponible en este horario
        if materias[num]["computo"] == True:
            #Revisa los dos salones y guarda cual de los dos es el disponible
            for z in range(2):
                if computo[z]["horarios"][row][col] == True:
                    indexcomp=z
                    break
            if indexcomp is None:
                continue


        #Rellenamos el horario con la materia disponible
        calendarios[semestre]["calendario"][row][col] = materias[num]["materia"]
        #Marcamos esta hora del profe como ocupada
        materias[num]["profesor"]["horarios"][row][col] = False
        #Restamos un módulo de los disponibles de la clase
        materias[num]["bloques"] -= 1

        #Marca como ocupado la hora en computo
        if indexcomp is not None:
            computo[indexcomp]["horarios"][row][col] = False

        if Horario_impl(pos+1, calendarios, materias, computo, sandwich):
                return True
                
        #Backtacking 
        materias[num]["bloques"] += 1
        calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
        materias[num]["profesor"]["horarios"][row][col] = True

        if indexcomp is not None:
            computo[indexcomp]["horarios"][row][col] = True

    #intentamos poner una hora vacía, si no se puede por el sandwich retorna falso
    calendarios[semestre]["calendario"][row][col] = "vacío"

    cont=0
    conte= 0
    #Cuenta cuantos vacios hay, cada uno con un peso dependiendo de su lugar dando los valores 1,2,3 por si solos y todas las combinaciones
    #Luego cuenta los empty, si hay mas de 0 entonces aun no es necesario regresar falso
    if(sandwich == False):
        for i in range(3):
            if calendarios[semestre]["calendario"][i][col] == "vacío":
                    cont += 1+i
            if calendarios[semestre]["calendario"][i][col] == "empty".ljust(30):
                    conte += 1+i
        if cont == 2 and conte != 0:
                return False

    #Seguir después de poner vacío
    if Horario_impl(pos+1, calendarios, materias, computo, sandwich):
                return True
    
    calendarios[semestre]["calendario"][row][col] == "empty".ljust(30)
    return False

def Horario(materias, computo):
    calendarios = [
        {"semestre": "2", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "4", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "6", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "8", "calendario": np.full((3,5), "empty".ljust(30))}
    ]

    pos = 0
    sandwich = True
    #Se realizan las verificaciones para que un mismo profesor no tenga
    #más de 2 asignaturas en el mismo semestre
    for z in range (0,6):
        for j in range (0,6):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el segundo semestre")
                 return False
    for z in range (7,12):
        for j in range (7,12):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el cuarto semestre")
                 return False
    for z in range (13,18):
        for j in range (13,18):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el sexto semestre")
                 return False
    for z in range (14,24):
        for j in range (14,24):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el octavo semestre")
                 return False
        
        
    if not Horario_impl(pos, calendarios, materias, computo, sandwich):
        print("="*30)
        print("\nNo es posible este calendario\n")
        print("="*30)
    else:
        # Si todo está correcto se imprime el calendario
        ancho = 15
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

        #Ancho total real de la tabla
        ancho_total = (ancho +3) * len(dias) + 1

        for z in range(4):

            print("=" * ancho_total)

            titulo = f" Semestre {z+z+2} "
            print(titulo.center(ancho_total, "="))

            #Días 
            for dia in dias:
                print(f"| {dia.ljust(ancho)}", end=" ")
            print("|")

            print("=" * ancho_total)

            #Materias
            for i in range(3):

                for k in range(5):

                    texto = calendarios[z]["calendario"][i][k]

                    print(f"| {texto.ljust(ancho)}", end=" ")

                print("|")

            print("=" * ancho_total)
            print()

        for z in range(2):

            print("=" * ancho_total)

            titulo = f" Computo {z+1} "
            print(titulo.center(ancho_total, "="))

            #Días
            for dia in dias:
                print(f"| {dia.ljust(ancho)}", end=" ")
            print("|")

            print("=" * ancho_total)

            for i in range(3):

                for k in range(5):

                    if(computo[z]["horarios"][i][k]):
                         
                        texto = "Vacío"
                    else:
                        texto = "Ocuapdo"

                    print(f"| {texto.ljust(ancho)}", end=" ")

                print("|")

            print("=" * ancho_total)
            print()

profesores = [
    {"profesor": "Peniche", "horarios": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]},

    {"profesor": "Aylin", "horarios": [
        [True, True, True, True, True],
        [True, True, True, False, True],
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


computo = [
        {"horarios": np.full((3,5), True)},
        {"horarios": np.full((3,5), True)}
    ]


Horario(materias,computo)