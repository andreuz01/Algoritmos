# BUG1 el algoritmo no verifica que un profesor tenga disponibilidad suficiente para impartir sus materias
# Agregar en Horario(), ANTES de llamar a Horario_impl()
# Por ejemplo, si peniche tiene solo 1 modulo libre en su matriz de horarios, digamos solo tiene 1 True, y da 1 materia en cada año
# El algoritmo automáticametne debería decir "wey qpd peniche no puede dar 4 bloques si solo tiene 1 hora libre wtf bro"
# Entonces primero intentaría todo hasta darse cuetna despues de millones de intentos y decirse "wey creo que peniche nunca podía bro"

# BUG2 IGUAL hay que verificar que hayan bloques de cómputo suficientes para las materias que requieran computo
# Agregar en Horario(), ANTES de llamar a Horario_impl()
# Suponiendo que hay 11 materias y cada una de ellas necesita 3 modulos de computo, se necesitarian un total de 33 modulos de computo, cuando realmente solo hay
# dos salones de computo que pueden dar cada uno 15 modulos, o sea hay maximo para 30 modulos de computo
# es algo que falta verificarse 

# BUG3 Finalmente como son 6 materias que van de 1 a 3 bloques puede ser que en un semestre hayan 6 materias todas con 3 bloques que necesiten
# Agregar en Horario(), ANTES de llamar a Horario_impl()
# o sea que requieran 18 bloques cuando realmente solo hay espacio para 15 bloques en un semestre, revisar esto también con un chequeo.
#resuelto

# FALTA checar la parte de pruebas y terminar de hacer todos los casos de prueba que dicen (FALTA)

## Prueba 4a: IMPRIMIR qué profe dio clase en qué bloque
## Crear función ImprimirCalendarioProfesor(calendarios, materias)
## Mostrar para cada profesor en qué bloque y semestre aparece asignado

## Prueba 4c: Comparar disponibilidad inicial vs final del profesor
## Los horarios originales están guardados en profesoresOG (deepcopy al inicio)
## Crear función ImprimirDisponibilidadProfesor(profesoresOG, profesores)

## bug4 hay que mover las verificaciones a una funcion independiente antes de generar los horarios

import numpy as np
import copy #Permite deepcopy, sirve para copiar objetos complejos como diccionarios y listas
import subprocess

subprocess.run('cls', shell=True) #Para limpiar la pantalla al inicio de cada ejecución del código

#---------------Documentación de las listas---------------

#La lista de materias tiene a cada objeto con el nombre de la materia, la cantidad de bloques, el booleano del salon de computo, el semestre, el profesor y el salón
#El profesor dentro de este diccionario está dentro de otra lista de un diccionario que representa a los profesores
#La lista salones de computo son otra lista de diccionarios, con las dos matrices de horario de los dos salones

#-------------------Variables globales--------------------

#Variable para cambiar el sandwich (Materia - Vacío - Materia)
global_sandwich = True

#Permite contar las "iteraciones" del agendador de horarios
iteraciones = 0

#Permite llamar a la función debug_imprimir(...)
debbugear = False

#Estas listas se mantienen como globales para su uso en la función MainMenu(), así no se pierden localmente

#Se crea la lista de computo con las matrices de disponibilidad de cada salón lleno de valores True
computo = [
        {"horarios": np.full((3,5), True)},
        {"horarios": np.full((3,5), True)}
]

#Se crea la lista de "calendarios", teniendo semestre, matriz llena de vacíos
# y con espacios menores a 30 caracteres por celda para definir el dtype del array de numpy
calendarios = [
    {"semestre": "2", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "4", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "6", "calendario": np.full((3,5), "empty".ljust(30))},
    {"semestre": "8", "calendario": np.full((3,5), "empty".ljust(30))}
]

##########################################################
# V     Insertar listas de profesores y materias aquí    V
##########################################################

#----------Prueba1----------
#Tiempo aproximado (2 mins - 5 mins)
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
    {"materia": "Algebra",      "bloques": 5, "computo": False, "semestre": 0, "profesor": profesores[0], "salon": "151"},
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
    {"materia": "Algebra II",     "bloques": 1, "computo": False, "semestre": 2, "profesor": profesores[3], "salon": "200"},
    {"materia": "Calculo II",     "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[4], "salon": "200"},
    {"materia": "Arquitectura", "bloques": 2, "computo": True,  "semestre": 2, "profesor": profesores[5], "salon": "200"},
    {"materia": "Electronica",  "bloques": 1, "computo": True, "semestre": 2, "profesor": profesores[6], "salon": "200"},
    {"materia": "Estadistica",  "bloques": 3, "computo": False, "semestre": 2, "profesor": profesores[7], "salon": "200"},

    # Semestre 3, requieren 12 bloques, o sea 3 vacíos
    {"materia": "Redes II",       "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[8], "salon": "210"},
    {"materia": "Algoritmos II",  "bloques": 2, "computo": True, "semestre": 3, "profesor": profesores[9], "salon": "210"},
    {"materia": "Proyectos II",   "bloques": 3, "computo": False, "semestre": 3, "profesor": profesores[0], "salon": "210"},
    {"materia": "IA",           "bloques": 2, "computo": True,  "semestre": 3, "profesor": profesores[1], "salon": "210"},
    {"materia": "Seguridad",    "bloques": 1, "computo": True, "semestre": 3, "profesor": profesores[2], "salon": "210"},
    {"materia": "Compiladores", "bloques": 3, "computo": True,  "semestre": 3, "profesor": profesores[3], "salon": "210"}
]

##########################################################
# ^     Insertar listas de profesores y materias aquí    ^
##########################################################

#Variables utilizadas dentro de MainMenu() para Reestablecer los valores del calendario
calendarioOG = copy.deepcopy(calendarios) 
computoOG = copy.deepcopy(computo)
materiasOG = copy.deepcopy(materias)
profesoresOG = copy.deepcopy(profesores)

#-------------------Funciones y código--------------------

#Función utilizada para debbugear e imprimir el calendario por medio de breakpoints
#Toma la lista de calendarios, el semestre actual y el título, puesto a default como calendario pero se cambia a debug en la ejecución del código
def imprimir_calendario_debug(calendarios, semestre, titulo="CALENDARIO"):

    #Permite configurar si se va a imprimir o no
    global debbugear
    if not debbugear:
        return
    
    #Para borrar cada iteración
    subprocess.run('cls', shell=True)

    #Se crea a lista de días
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    #toma el calendario del semestre a imprimir
    calendario = calendarios[semestre]["calendario"]

    #Establece el ancho
    ancho = 18
    ancho_total = (ancho + 3) * len(dias) + 1

    #Imprime la linea inicial
    print("\n" + "=" * ancho_total)

    #Asigna el titulo y el semestre a una variable string
    texto_titulo = f" {titulo} | Semestre {calendarios[semestre]['semestre']} "
    #Imprime el texto centrando este string tomando los parametros del ancho de donde se va a centrar y con que elemento lo va a centrar
    print(texto_titulo.center(ancho_total, "="))

    #Imprime la siguiente línea debajo del título
    print("=" * ancho_total)

    # Encabezados (imprime los días)
    for dia in dias:
        print(f"| {dia.center(ancho)}", end=" ")
    print("|")

    #Imprime la linea debajo de los encabezados
    print("=" * ancho_total)

    for fila in range(calendario.shape[0]):

        for col in range(calendario.shape[1]):

            #El texto a mostrar es el string del calendario fila, quitando espacios vacios adicionales u otros
            texto = str(calendario[fila][col]).strip()

            #En caso de ser vacío lo convierte en los guiones
            # Mejor visualización de vacíos
            if texto == "empty":
                texto = "-----"

            #Finalmente imprime el texto con el espaciado correcto
            print(f"| {texto.center(ancho)}", end=" ")

        #imprime la ultima barra de la fila y luego de esto continua a la siguiente fila
        print("|")

    #Pone una barra al final y un espacio 
    print("=" * ancho_total)
    print()

# Horario_impl(...) por medio de backtracking va armando el calendario según las restricciones dadas
# Tiene 5 parámetros: 

# -pos: Va de 0 - 60, debido a que son 15 celdas por 4 semestres 
# -calendarios: la lista de calendarios actuales en la iteracion
# -materias: lista de materias con sus datos
# -computo: lista de salones de cómputo con sus datos
# -sandwich: Variable que prohibe o permite el (materia - vacío - materia)

def Horario_impl(pos, calendarios, materias, computo, sandwich):

    def print_progress_bar(iteraciones):
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

    #----------Variables----------

    #Contador de iteraciones/llamadas
    global iteraciones
    iteraciones += 1

    print_progress_bar(iteraciones)

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
        
        ##Checa por cada materia si cumplen las condiciones para ser colocadas, si no, son saltadas
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
        ##Si pasa pruebas es insertada en el calendario, en la columna y fila

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
        ##Cuantas HAS colocado y son vacias
        cont=0

        #Cuenta las celdas llenas de "empty.ljust(30)"
        ##Cuales NO has colocado
        conte= 0

        #Es un chequeo que se realiza en cada iteración
        #Cuenta cuantos vacios hay, cada uno con un peso dependiendo de su lugar dando los valores 1,2,3 por si solos y todas las combinaciones
        if((sandwich == False) and (row == 2)): ##si NO puede haer sandwich y ES la ultima fila del calendario
            for i in range(3):
                if calendarios[semestre]["calendario"][i][col] == "vacío":
                        cont += 1+i
                if calendarios[semestre]["calendario"][i][col] == "empty".ljust(30):
                        conte += 1+i
            if cont == 2 and conte == 0:                 
                #-----break evitando el sandwich-----
                #Si no encontró una solución válida y retorno, rompe el ciclo de probar las materias
                #Como se descarta la rama por el false, se tienen que devolver los valores del maestro, bloques faltantes y salon de cómputo
                #Para hacer que retroceda a su estado anterior

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
                
                break ###FIX IMPORTANTÍSIMO, ANTES DESCARTABA LA RAMA ANTES DE PROBAR MATERIA-VACIO-VACIO, AHORA AHORRA MUCHAS ITERACIONES

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

    ##hardcodeado luego intenta vacio
    #Intentamos poner una hora vacía
    calendarios[semestre]["calendario"][row][col] = "vacío"

    #DEBUG imprimir el calendario original AL LLENAR UN VACÍO
    imprimir_calendario_debug(calendarios, semestre, "DEBUG")

    #Seguir después de poner vacío
    if Horario_impl(pos+1, calendarios, materias, computo, sandwich):
        return True
    
    ##si no funciona vacio se sale
    #Hacer el backtracking luego de haber probado vacío y marcar la rama como inválida
    calendarios[semestre]["calendario"][row][col] = "empty".ljust(30)
    
    #DEBUG imprimir el calendario original DESPUÉS DE PROBAR VACÍO
    imprimir_calendario_debug(calendarios, semestre, "DEBUG")

    #Se descarta la rama y se regresa al no tener más opciones
    return False

# Horario(...) inicializa las primeras revisiones antes de llamar a Horario_impl(...)
# Tiene 4 parámetros:

# -calendarios: lista de calendarios globales
# -materias: lista de materias a agendar con sus datos
# -computo: lista de salones de cómputo con sus datos
# -sandwich: Variable que prohibe o permite el (materia - vacío - materia)

def Horario(calendarios, materias, computo, sandwich = True):
    
    #Se inicializa en la posición 0
    pos = 0

    bloquesS0 = 0
    bloquesS1 = 0
    bloquesS2 = 0
    bloquesS3 = 0
    for i in range(len(materias)):
        if materias[i]["semestre"] == 0:
            bloquesS0 += materias[i]["bloques"]
        if materias[i]["semestre"] == 1:
            bloquesS1 += materias[i]["bloques"]
        if materias[i]["semestre"] == 2:
            bloquesS2 += materias[i]["bloques"]
        if materias[i]["semestre"] == 3:
            bloquesS3 += materias[i]["bloques"]    


    if bloquesS0 > 15:
        print("el segundo semestre semestretiene mas bloques que los permitidos")
        return False
    if bloquesS1 > 15:
        print("el cuarto semestre semestretiene mas bloques que los permitidos")
        return False
    if bloquesS2 > 15:
        print("el sexto semestre semestretiene mas bloques que los permitidos")
        return False
    if bloquesS3 > 15:
        print("el octavo semestre semestretiene mas bloques que los permitidos")
        return False

    ##Chequeo de materias por semestre para los for, checa cuantas materias hay en cada semestre
    semestre0 = 0
    semestre1 = 0
    semestre2 = 0
    semestre3 = 0
    for z in range(len(materias)):
        if materias[z]["semestre"] == 0: semestre0 += 1
        if materias[z]["semestre"] == 1: semestre1 += 1
        if materias[z]["semestre"] == 2: semestre2 += 1
        if materias[z]["semestre"] == 3: semestre3 += 1
    ##Los vuelve sus puntos finales 
    semestre1 = semestre1 + semestre0
    semestre2 = semestre1 + semestre2
    semestre3 = semestre2 + semestre3
    #Se realizan las verificaciones para que un mismo profesor no tenga
    #más de 2 asignaturas en el mismo semestre

    #Cada ciclo for revisa un semestre distinto, por los rangos de índices establecidos en las materias de cada semestre
    #Va verificando que el mismo profesor no se repita más de 1 vez en cada semestre
    
    for z in range (0,semestre0):
        for j in range (0,semestre0):
            #Si ambas son la misma materia a ser comparada se continua a la siguiente iteracion
            if z==j:
                 continue
            #Si el profesor de la materia z es igual al de la materia j dentro del semestre, retorna falso 
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el segundo semestre")
                 return False
    for z in range (semestre0,semestre1):
        for j in range (semestre0,semestre1):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el cuarto semestre")
                 return False
    for z in range (semestre1,semestre2):
        for j in range (semestre1,semestre2):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el sexto semestre")
                 return False
    for z in range (semestre2,semestre3):
        for j in range (semestre2, semestre3):
            if z==j:
                 continue
            if materias[z]["profesor"]== materias[j]["profesor"]:
                 print("El profesor tiene dos materias en el octavo semestre")
                 return False
        
    #Se realiza la llamada a la implementación de la función dentro del if
        
    print(f'No existen profesores repetidos\n\nSe ha inicializado correctamente el agendador de horarios\n')

    # Se llama a Horario_impl(...) para generar por medio de bactracking el horario
    # Si retornó falso no encontró una posible solución, si retorna verdadero entonces generó de manera correcta el horario
    if not Horario_impl(pos, calendarios, materias, computo, sandwich):
        subprocess.run('cls', shell=True) #limpias pantalla
        print("No es posible este calendario\n")
    else:
        subprocess.run('cls', shell=True) #limpias pantalla
        print("Calendario generado exitosamente\n")
    print(f'El número de iteraciones realizadas fueron: {iteraciones}\n')

    input_ignore = input("Presiona Enter para continuar...") ##Esperas el usuario ingrese una tecla
    subprocess.run('cls', shell=True) #limpias pantalla

def ImprimirCalendario(calendario, materias, computo):
        ancho = 15
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

        #Ancho total real de la tabla
        ancho_total = (ancho +3) * len(dias) + 1 ##108 =

        for z in range(4):

            print("=" * ancho_total)

            titulo = f" Semestre {z+z+2} "
            print(titulo.center(ancho_total, "="))

            #Días 
            for dia in dias:
                print(f"| {dia.ljust(ancho)}", end=" ")
            print("|")

            print("=" * ancho_total)

            for i in range(3):

                # Consigue la materia hazlo el primero
                for k in range(5):
                    texto = calendarios[z]["calendario"][i][k]
                        # Limpiar el texto para mostrarlo bonito si no hay nada
                    if texto == "empty".ljust(30) or texto == "empty":
                        texto = "Vacío"
                    elif texto == "vacío":
                        texto = "Vacío"
                    else:
                        texto = texto.strip()
                    print(f"| {texto.ljust(ancho)}", end=" ")
                print("|")


                # Consigue el profesor
                for k in range(5):
                 nombre = calendarios[z]["calendario"][i][k]
                 profe = ""
                
                    # Solo buscar el profesor si no es una celda vacía
                 if nombre not in ["empty".ljust(30), "empty", "vacío"]:
                    for m in materias:
                        if m["materia"] == nombre.strip():
                            profe = m["profesor"]["profesor"]
                            break
                
                 if profe == "":
                    profe = "-----"
                    
                 print(f"| {profe.ljust(ancho)}", end=" ")
                print("|")


                # Salon de computo
                for k in range(5):

                     nombre = calendarios[z]["calendario"][i][k]
                     salon = ""
                
                    # Solo buscar el salón si no es una celda vacía
                     if nombre not in ["empty".ljust(30), "empty", "vacío"]:
                        for m in materias:
                            if m["materia"] == nombre.strip():
                                salon = "Salón Computo" if m["computo"] else f"Salón {m['salon']}"
                                break
                
                     if salon == "":
                        salon = "-----"
                    
                     print(f"| {salon.ljust(ancho)}", end=" ")
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

        input_ignore = input("\nPresiona Enter para continuar...")
        subprocess.run('cls', shell=True)

def MateriasBloquesProfesores(materias):
    print("========================================================================")
    print("*******************************Semestre 1*******************************")
    print("========================================================================")
    for m in materias:
        if m["semestre"] == 0:
            print(f'semestre:{m["semestre"] + 1}, materia: {m["materia"]}, profesor: {m["profesor"]["profesor"]}, bloques restantes:{m["bloques"]}')
        else:
            continue
    print("\n")
    print("========================================================================")
    print("*******************************Semestre 2*******************************")
    print("========================================================================")

    for m in materias:
        if m["semestre"] == 1:
            print(f'semestre:{m["semestre"] + 1}, materia: {m["materia"]}, profesor: {m["profesor"]["profesor"]}, bloques restantes:{m["bloques"]}')
        else:
            continue
    print("\n")
    print("========================================================================")
    print("*******************************Semestre 3*******************************")
    print("========================================================================")

    for m in materias:
        if m["semestre"] == 2:
            print(f'semestre:{m["semestre"] + 1}, materia: {m["materia"]}, profesor: {m["profesor"]["profesor"]}, bloques restantes:{m["bloques"]}')
        else:
            continue
    print("\n")
    print("========================================================================")
    print("*******************************Semestre 4*******************************")
    print("========================================================================")

    for m in materias:
        if m["semestre"] == 3:
            print(f'semestre:{m["semestre"] + 1}, materia: {m["materia"]}, profesor: {m["profesor"]["profesor"]}, bloques restantes:{m["bloques"]}')
        else:
            continue    
    print("\n")
    input_ignore = input("Presiona Enter para continuar...")
    subprocess.run('cls', shell=True)

def ReiniciarCalendario():
    global calendarios, computo, profesores, materias, iteraciones
    calendarios = copy.deepcopy(calendarioOG)
    computo = copy.deepcopy(computoOG)
    profesores = copy.deepcopy(profesoresOG)
    materias = copy.deepcopy(materiasOG)
    iteraciones = 0

## MainMenu() es una interfáz gráfica que sirve para para probar el calendario en todos sus aspectos para el video

#Todos los puntos que falta si los cumple el algoritmo, sin embargo es más dificil demostrar que lo cumplen si no se realizan las demostraciones

## Prueba 1: Un semestre no puede tener más de una asignatura en el mismo bloque 
## Demostracion: Mostrar el calendario (LISTO)

## Prueba 2: Cada asignatura debe cubrir exactamente su número requerido de bloques
## Demostración: Generar lista de materias (LISTO) 

## Prueba 3: Una asignatura no puede ser asignada mas de una vez el mismo dia
## Demostración: generar calendario y mostra y ya (LISTO)

## Prueba 4 (FALTA): Un profesor...
##      a. no puede estar asignado a más de una clase en el mismo bloque
##      b. no puede exceder 1 asignatura por semestre
##      c. debe respetar su disponibilidad
## Demostración: 
##      a. IMPRIMIR calendario de cada profe para saber que profe dio clase en que bloque (FALTA)
##      b. Mostrar que asignatura dio en el semestre y cual fue (LISTO)
##      c. Imprimir su calendario inicial de profesores y compararlo con el finalizado (FALTA)

## Prueba 5: Uso de laboratorios...
##      a. Máximo 2 asignaturas simultáneas que requieran cómputo
##      b. Solo asignaturas que lo requieran pueden ocuparlos
## Demostración: 
##      a. IMPRIMIR calendario de cómputo con el nombre de las materias que los usan en cada celda (FALTA)
##      b. IMRPIMIR lista de asignaturas que requieren del salon de cómputo y verificar si lo requieren (FALTA) 

## Prueba 6: Huecos en el horario (Sandwich)
##      a. Poder activarlo o desactivarlo (LISTO)

##FALTA: demostrar varios de los puntos que pide el profesor para las pruebas
def MainMenu():
    
    def generar_calendario():
        subprocess.run('cls', shell=True)
        ReiniciarCalendario()
        if global_sandwich:
            print(f"Inicializando generador de horario CON huecos en el horario\n")
        else:
            print(f"\nInicializando generador de horario SIN huecos en el horario\n")
        Horario(calendarios, materias, computo, global_sandwich)
    
    def ver_calendario():
        subprocess.run('cls', shell=True)
        print("\nMostrando horario...\n")
        ImprimirCalendario(calendarios, materias, computo)

    def mostrar_materias_bloques_y_profesores():
        subprocess.run('cls', shell=True)
        print("Cada horario tiene ciertas necesidades que deben cumplirse cada semestre")
        print(" -Un profesor no puede exceder 1 asignatura por semestre")
        print(" -Cada asignatura debe cubrir exactamente su número requerido de bloques\n")
        print("Esta lista muestra un conteo de estas necesidades\n")
        input("Presiona Enter para continuar...")
        subprocess.run('cls', shell=True)
        MateriasBloquesProfesores(materias)
    
    def configuracion_del_sandwich():
        global global_sandwich
        config_sandwich = True
        while config_sandwich:
            subprocess.run('cls', shell=True)
            print("La configuración de huecos en el horario permite o desactiva los bloques vacíos disponibles entre clases, desea...\n")
            print("1. Permitir huecos en el horario\n")
            print("2. Desactivar huecos en el horario\n")
            print("3. Volver\n")

            eleccion_sandwich = input("Ingrese el número de la opción que desea probar: ")

            match eleccion_sandwich:
                case "1":
                    global_sandwich = True
                    subprocess.run('cls', shell=True)
                    print("Huecos permitidos\n")
                    print("Regenere el horario para reflejar los cambios\n")
                    input("Presiona Enter para continuar...")
                    config_sandwich = False
                    subprocess.run('cls', shell=True)
                case "2":
                    global_sandwich = False
                    subprocess.run('cls', shell=True)
                    print("Huecos desactivados\n")
                    print("Regenere el horario para reflejar los cambios\n")
                    input("Presiona Enter para continuar...")
                    config_sandwich = False
                    subprocess.run('cls', shell=True)
                case "3":
                    config_sandwich = False
                    subprocess.run('cls', shell=True)
                case _:
                    opcion_invalida()    

    def opcion_invalida():
        subprocess.run('cls', shell=True)
        print("\nOpción inválida, por favor ingrese un número válido\n")
        input_ignore = input("Presiona Enter para continuar...")

    def work_zone():
        subprocess.run('cls', shell=True)
        print(":P")
        input_ignore = input("\nZona en construcción, presiona Enter para continuar...")

    iniciado = True

    while iniciado:
        subprocess.run('cls', shell=True)
        print("===========================================================================================")
        print("****************************Bienvenido al generador de horarios****************************")
        print("===========================================================================================")

        print("\nDentro del generador de horarios tiene un listado de opciones a elegir...\n")
        print("1. Generar horario\n")
        print("2. Ver horario\n")
        print("3. Configurar huecos en el horario\n")
        print("4. Materias, bloques y profesores\n")
        print("5. ---\n")
        print("6. ---\n")        
        print("7. Salir\n")

        eleccion = (input("Ingrese el número de la opción que desea probar: "))

        match eleccion:

            case "1":
                vericar()
                generar_calendario()

            case "2":
                ver_calendario()

            case "3":
                configuracion_del_sandwich()
            
            case "4":
                mostrar_materias_bloques_y_profesores()

            case "5":
                work_zone()

            case "6":
                work_zone()

            case "7":
                subprocess.run('cls', shell=True)
                print("Ha salido del programa...\n")
                iniciado = False

            case _:
                opcion_invalida()

#Se inicializa la ejecución del código
MainMenu()