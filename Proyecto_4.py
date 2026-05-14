#Leosugerencia1: creo que la creación de las matrices de computo se puede poner dentro de la funcion Horarios
#ya que esta realmente no se modifica y se crea de manera muy similar a las 4 matrices de horario de cada semestre

#Leosugerencia2: esto realmente es para que lo lea en el futuro, me gustaría encapsular en una funcion el print final del calendario
#y añadirle que diga profe y salon, pero realmente no importa

#Leosugerencia3: Estaría chingon que tmb pueda mostrar como el de octavio los calendarios de los salones de computo, la matriz 
#de horarios de cada profe en interfaz gráfica, etc, pero lo mismo esto es más algo opcional

##Leosugerencia4: Atenten contra su vida

import numpy as np

import subprocess
subprocess.run('cls', shell=True) #Para limpiar la pantalla al inicio de cada ejecución del código

#-------------------Settings--------------------

#Variable para cambiar el sandwich
#Para evitar que haya una clase seguida de una hora libre seguido de una clase
global_sandwich = True

#Se inicializa la variable de iteraciones 
#Sirve para ver la "rapidez" del código
iteraciones = 0

#Variable que permite a la función debug_imprimir() ver cada iteración de la búsqueda
debbugear = False

#hola andreuz
#matate gustavo
#hola leo

#-------------------Funciones y código--------------------

#Función utilizada para debbugear e imprimir el calendario
def imprimir_calendario_debug(calendarios, semestre, titulo="CALENDARIO"):

    global debbugear
    if not debbugear:
        return
    
    #Para borrar cada iteración
    subprocess.run('cls', shell=True) #Para limpiar la pantalla al inicio de cada ejecución del código

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

#Función que por medio de backtracking va armando el calendario segun las restricciones dadas

#Tiene 5 parámetros: Pos va de 0 a 60 posiciones, debido a que son 15 celdas por 4 semestres
#Igualmente pasa la lista de calendarios, la lista de materias, los salones de computo y la variable que prohibe o permite el sandwich

def Horario_impl(pos, calendarios, materias, computo, sandwich):
     
    #----------Variables----------

    #Contador de iteraciones/llamadas
    global iteraciones
    iteraciones += 1

    n_materias = len(materias)

    #Se encuentra el semestre diviendo exactamente la posición, va de 0 - 3
    semestre = pos //15

    #Posición en la que estamos dentro del semestre, va de 0 a 14
    localpos = pos %15

    #Convierte localpos a la columna y la fila de la posición local del semestre ubicado
    col = localpos % 5
    row = localpos // 5

    #----------Chequeos iniciales----------

    #1. Checa si es que llegó a la última posición
    
    if pos == 60:
        cont=0
        #Va verificando que todas las materias no tengan bloques pendientes
        #Y va sumando un contador segun el número de materias ya completamente asignadas
        for i in range(n_materias):
            if materias[i]["bloques"]==0:
                cont+=1   
        #Si todas las materias están completas el horario es válido y detiene la búsqueda
        if cont== n_materias:
            return True
        #Si no, entonces se retorna falso y retrocede a la llamada anterior
        else:
            return False

    #2. Checa espacios libres suficientes
    
    #(Cuenta el número de espacios validos para poner una materia y cuenta cuantas materias aún no se ponen)
    
    #Se inicializan las variables
    espacios_validos = 0
    modulos = 0

    #Va contando los módulos faltantes del semestre actual dentro de todas las materias
    #El primer if es para verificar que la materia pertenezca al semestre
    #El siguiente es para sumar los bloques faltantes si estos no son iguales a 0
    for m in range(n_materias):
        if materias[m]["semestre"] == semestre:
            if materias[m]["bloques"] != 0:
                modulos += materias[m]["bloques"] 

    #Va contando las celdas vacías disponibles en el semestre
    #Recorre todo el calendario y va sumando la cantidad de espacios válidos
    for x in range(3):
        for y in range(5):
            if calendarios[semestre]["calendario"][x][y] == "empty".ljust(30):
                espacios_validos += 1

    #Si la cantidad de módulos faltantes es mayor a los espacios vacíos retorna falso y detiene la búsqueda                    
    if modulos > espacios_validos:
        return False

    #----------Función principal----------

    #Un ciclo for que se va ejecutando para cada materia dentro de la lista de materias
    for num in range(n_materias):
        
        #-----Inicializar variables-----
        
        #Variable para realizar el chequeo de que la materia no se repita el mismo día
        invalido = False
        
        #Variable para realizar el chequeo si la materia requiere de salón de cómputo
        indexcomp = None

        #-----Revisiones-----

        #1. Revisar disponiblidad de la materia
        #Si la materia es de otro semestre o ya no le quedan clases que usar la salta
        if materias[num]["semestre"] != semestre or materias[num]["bloques"] == 0:
            continue
        
        #2. Revisar disponibilidad del profesor
        #Si en esta hora el maestro esta ocupado en otro semestre se salta esta iteración
        if materias[num]["profesor"]["horarios"][row][col] == False:
                continue 

        #3. Revisar repetición que la materia no se repita
        #Checa si ya esta guardada esta materia en esta columna
        for i in range(3):
            if materias[num]["materia"] == calendarios[semestre]["calendario"][i][col]:
                invalido = True
                break
        #Si ya se usa la materia en el dia se salta a la siguiente iteración
        if invalido:
            continue
        
        #4. Revisar salones de cómputo 
        #Si la materia que estamos probando usa el salon de computo checar si esta disponible en este horario
        if materias[num]["computo"] == True:
            #Revisa los dos salones y guarda cual de los dos es el disponible
            for z in range(2):
                if computo[z]["horarios"][row][col] == True:
                    indexcomp=z
                    break
            #Si ninguno está disponible continua a la siguiente iteración
            if indexcomp is None:
                continue

        #----------Rellenar el calendario (matriz)----------

        #Rellenamos el horario con la materia disponible
        calendarios[semestre]["calendario"][row][col] = materias[num]["materia"]
        #Marcamos esta hora del profe como ocupada
        materias[num]["profesor"]["horarios"][row][col] = False
        #Restamos un módulo de los disponibles de la clase
        materias[num]["bloques"] -= 1

        #DEBUG imprimir el calendario AL LLENAR UN PROFE
        imprimir_calendario_debug(calendarios, semestre, "DEBUG")

        #Si la materia requiere el salón de cómputo, marca como ocupado la hora en computo
        if indexcomp is not None:
            computo[indexcomp]["horarios"][row][col] = False

        #Nueva verificación de sandwich. se quiere checar el sandwich una vez se puso una materia en la última celda de cada columna, solamente ahi se puede saber si hay sandwich o no
        #Igualmente tomamos en cuenta si se van a permitir los sándwiches o no. Teniendo esto en mente la posición correcta donde debe de ir la verificación del sandwich es justo después 
        #Poner una materia.
        
        #-----Variables para evitar el sandwich-----
        
        #Cuenta las celdas con el string "vacío"
        cont=0

        #Cuenta las celdas llenas de "empty.ljust(30)"
        conte= 0

        #Es un chequeo que se realiza en cada iteración
        #Cuenta cuantos vacios hay, cada uno con un peso dependiendo de su lugar dando los valores 1,2,3 por si solos y todas las combinaciones
        if((sandwich == False) and (row == 2)):
            for i in range(3):
                if calendarios[semestre]["calendario"][i][col] == "vacío":
                        cont += 1+i
                if calendarios[semestre]["calendario"][i][col] == "empty".ljust(30):
                        conte += 1+i
            if cont == 2 and conte == 0:                 
                #-----Backtacking evitando el sandwich-----
                #Si no encontró una solución válida y retorno, hace el backtracking
                #Como se descarta la rama por el false, se tienen que devolver los valores del maestro, bloques faltantes y salon de cómputo
                #Para hacer que haga backtrack y retroceda a su estado anterior

                #Le suma un bloque faltante a la materia
                materias[num]["bloques"] += 1
                #Se asigna la celda actual como una empty para poder volver a probar
                calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
                #Se establece el horario del profesor como disponible
                materias[num]["profesor"]["horarios"][row][col] = True

                #Regresa la disponibilidad del salón de cómputo solo si este estaba marcado como ocupado por la materia
                if indexcomp is not None:
                    computo[indexcomp]["horarios"][row][col] = True

                #DEBUG imprimir el después de evitar el sandwich
                imprimir_calendario_debug(calendarios, semestre, "DEBUG")
                
                return False

        #Pasa a la siguiente llamada con la siguiente posición a rellenar, con los mismos calendarios, materias computo y variable del sandwich
        if Horario_impl(pos+1, calendarios, materias, computo, sandwich):
            #Si llegó a la solución retorna true para salir de todas las llamadas
            return True
                
        #----------Backtacking----------

        #Si no encontró una solución válida y retorno, hace el backtracking

        #Le suma un bloque faltante a la materia
        materias[num]["bloques"] += 1
        #Convierte el espacio anterior como vacío
        calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
        #Se establece el horario del profesor como disponible
        materias[num]["profesor"]["horarios"][row][col] = True

        #DEBUG imprimir el calendario al hacer backtracking
        imprimir_calendario_debug(calendarios, semestre, "DEBUG")

        #Regresa la disponibilidad del salón de cómputo solo si este estaba marcado como ocupado por la materia
        if indexcomp is not None:
            computo[indexcomp]["horarios"][row][col] = True

    #En este punto el for ya intentó poner todas las materias, entonces intentará ingresar un espacio "vacío"

    #Intentamos poner una hora vacía
    calendarios[semestre]["calendario"][row][col] = "vacío"

    #DEBUG imprimir el calendario original AL LLENAR UN VACÍO
    imprimir_calendario_debug(calendarios, semestre, "DEBUG")

    #Seguir después de poner vacío
    if Horario_impl(pos+1, calendarios, materias, computo, sandwich):
        return True
    
    #Hacer el backtracking luego de haber probado vacío y marcar la rama como inválida
    calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
    
    #DEBUG imprimir el calendario original DESPUÉS DE PROBAR VACÍO
    imprimir_calendario_debug(calendarios, semestre, "DEBUG")

    #Se descarta la rama y se regresa al no tener más opciones
    return False

#Tiene el parámetro de la lista de materias, la lista de salones de cómputo y el sandwich, puesto como predefinido que si acepte sandwich en caso de no pasarselo
def Horario(materias, computo, sandwich = True):
    
    #Se crea una lista de "calendarios", siendo estos diccionarios
    #Cuentan con el semestre, su matriz llena de vacíos, con espacios menores a 30 caracteres por celda para definir el dtype del array de numpy
    calendarios = [
        {"semestre": "2", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "4", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "6", "calendario": np.full((3,5), "empty".ljust(30))},
        {"semestre": "8", "calendario": np.full((3,5), "empty".ljust(30))}
    ]

    #Se inicializa en la posición 0
    pos = 0

    #Se realizan las verificaciones para que un mismo profesor no tenga
    #más de 2 asignaturas en el mismo semestre

    #Cada ciclo for revisa un semestre distinto, por los rangos de índices establecidos en las materias de cada semestre
    #Va verificando que el mismo profesor no se repita más de 1 vez en cada semestre
    
    for z in range (0,6):
        for j in range (0,6):
            #Si ambas son la misma materia a ser comparada se continua a la siguiente iteracion
            if z==j:
                 continue
            #Si el profesor de la materia z es igual al de la materia j dentro del semestre, retorna falso 
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el segundo semestre")
                 return False
    for z in range (6,12):
        for j in range (6,12):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el cuarto semestre")
                 return False
    for z in range (12,18):
        for j in range (12,18):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el sexto semestre")
                 return False
    for z in range (18,24):
        for j in range (18,24):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el octavo semestre")
                 return False
        
    #Se realiza la llamada a la implementación de la función dentro del if
        
    print(f'Se ha inicializado correctamente el agendador de horarios')

    #Si retorna falso, se imprime que no es posible la configuración actual del calendario
    if not Horario_impl(pos, calendarios, materias, computo, sandwich):
        print("="*30)
        print("\nNo es posible este calendario\n")
        print("="*30)
    # Si todo está correcto se imprime el calendario
    else:
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
                        texto = "Ocupado"

                    print(f"| {texto.ljust(ancho)}", end=" ")

                print("|")

            print("=" * ancho_total)
            print()
    
    print(f'\nEl número de iteraciones fueron: {iteraciones}')

#----------Documentación de las listas----------

#La lista de materias tiene a cada objeto con el nombre de la materia, la cantidad de bloques, el booleano del salon de computo, el semestre, el profesor y el salón
#El profesor dentro de este diccionario está dentro de otra lista de un diccionario que representa a los profesores
#La lista salones de computo son otra lista de diccionarios, con las dos matrices de horario de los dos salones

###################################################
# v Insertar listas de profesores y materias aqui v

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

# ^ Insertar listas de profesores y materias aqui ^
###################################################

#Se crean los objetos de computo, con sus horarios 5x3 llenos de Trues
computo = [
        {"horarios": np.full((3,5), True)},
        {"horarios": np.full((3,5), True)}
]

#Llama a la función Horario, pasando la lista de materias como la lista de salones de cómputo, como la variable de sandwich
Horario(materias,computo, global_sandwich)