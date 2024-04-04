import time
from random import randint

INTENTOS = 7

def main():
    """Subrutina principal del juego de ahorcado
    
    Entradas y restricciones:
    -Ninguna    
    Salidas:
    -El juego de ahorcado
    
    Recreado por Juan Pablo Jiménez, a partir de código de Mauricio A.
    """ 
    global INTENTOS    
    
    limpiarPantalla()
    imprimirEntrada()
    
    continuar = True
    while(continuar):
        
        textoOriginal = escojerFrase()
        limpiarPantalla()
        
        letrasUsadas = ""
        intentos = 0
        ronda = 1
        
        while(intentos <= INTENTOS and  
              not adivino(textoOriginal, letrasUsadas)):
            
            limpiarPantalla()
            imprimirStats(textoOriginal, letrasUsadas, intentos, ronda)
            letraIntento = leerIntento(letrasUsadas)
            
            if(aciertaIntento(textoOriginal, letraIntento)):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos += 1
            
            letrasUsadas += letraIntento
            ronda += 1
            time.sleep(1)
        
        if(adivino(textoOriginal, letrasUsadas)):
            limpiarPantalla()
            imprimirMensajeVictoria()
            imprimirStats(textoOriginal, letrasUsadas, intentos, ronda)
        else:
            imprimirMensajeDerrota(textoOriginal)
            
        continuar = leerJugarNuevamente()
        
    imprimirMensajeDespedida()
    
    
def limpiarPantalla():
    """Subrutina que imprime lineas en blanco para limpiar
    la pantalla 
    
    Entradas y Restricciones:
    -Ninguna
    Salidas:
    -40 lineas en blanco"""
    print("\n" * 40 )
    
    
def imprimirEntrada():
    """Subrutina que imprime un mensaje de bienvenida
    Entradas y Restricciones:
    -Ninguna
    Salidas:
    -Mensaje de bienvenida"""
    
    print("   ▄████████    ▄█    █▄     ▄██████▄     ▄████████")
    print("  ███    ███   ███    ███   ███    ███   ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄▄██▀")
    print("▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███████▀  ")
    print("  ███    ███   ███    ███   ███    ███ ▀███████████")
    print("  ███    ███   ███    ███   ███    ███   ███    ███")
    print("  ███    █▀    ███    █▀     ▀██████▀    ███    ███\n")    
    print("▄████████    ▄████████ ████████▄   ▄██████▄")
    print("███    ███   ███    ███ ███   ▀███ ███    ███")
    print("███    █▀    ███    ███ ███    ███ ███    ███")
    print("███          ███    ███ ███    ███ ███    ███")
    print("███        ▀███████████ ███    ███ ███    ███")
    print("███    █▄    ███    ███ ███    ███ ███    ███")
    print("███    ███   ███    ███ ███   ▄███ ███    ███")
    print("████████▀    ███    █▀  ████████▀   ▀██████▀")
    print("Elaborado por Juan Pablo Jiménez, en base a código de Mauricio A.")
    print()
    print()
    

def escojerFrase():
    """Función que escoje al azar una palabra entre las listas
    almacenadas, dependiendo de la dificultad escogida por
    el usuario

    Entradas y Reestricciones:
    -Ninguna
    Salidas:
    -Frase o palabra a adivinar al azar"""

    rondaFacil = ["tuanis", "pura vida", "zarpe", "chiva", "mae", "diay"]    
    rondaMedia = ["mejenga", "pepiado", "de tal palo tal astilla", "zaguate", "vieras que", "chepo"]
    rondaDificil = ["cria cuervos y te sacaran tus ojos", "al pan pan y al vino vino", "chamaco", "bombeta", "chinchorro", "despapayar"]

    dificultad = fraseAdivinar()
    palabra = randint(0, 5)

    if(dificultad == "1"):
        return rondaFacil[palabra]
    elif(dificultad == "2"):
        return rondaMedia[palabra]
    else:
        return rondaDificil[palabra]

    

def fraseAdivinar():
    """Función que pide al usuario escojer la dificultad de ronda
    que quiere jugar y devuelve esta opción
    
    Entradas y Restricciones:
    -Opción del usuario
    Salidas:
    -Nivel de dificultad de la ronda"""

    print("Escoja la dificultad de la frase")
    print("1 - Frase o palabra fácil")
    print("2 - Frase o palabra intermedia")
    print("3 - Frase o palabra difícil")
    print()
    op = input("Escoja la dificultad: ")
    
    while op not in ["1", "2", "3"]:
        print("\nEsta opción no existe, ingrese nuevamente una opción")
        op = input("Escoja la dificultad: ")
        
    return op


def adivino(texto, letrasUsadas):
    """Función booleana que dice si el usuario ya adivino el texto

    Entradas y Restricciones:
    -Texto: texto preparado (sin tildes, ni acentos), debe de ser un string sin acentos
    -letrasUsadas: letras que el usuario ha intentado, debe de ser un string sin acentos
    
    Salidas:
    -True si todas las letras del texto han sido intentadas,
    False sino"""

    if(type(texto) != str or type(letrasUsadas) != str):
        raise Exception("El texto y las letras intentadas deben ser string")

    for letra in texto:
        if(letra != " "):
            if(letra not in letrasUsadas):
                return False

    return True


def imprimirStats(texto, letrasUsadas, intentos, ronda):
    """Esta función imprime los mensajes requeridos para cada
    ronda del juego.
    Imprime el número de ronda actual, un mensaje que indica las
    lettras que ya fuero utilizadas, cantidad de intentos fallidos
    y también escribe el texto enmascarado

    Entradas y Restricciones:
    -texto: texto preparado sin tildes ni acentos
    -letrasUsadas: letras que el usuario ha intentado
    -intentos: cantidad de intentos fallidos
    -ronda: número de ronda por la que va el juego

    Salidas:
    -Impresión en pantalla de la información de la ronda"""

    print(f"Ronda número: {ronda}")
    print(f"Letras que ya fueron usadas: {letrasUsadas}")
    print(f"Cantidad de intentos fallidos: {intentos} \n")
    print(f"{enmascarar(texto, letrasUsadas)} \n")
    

def enmascarar(texto, letrasUsadas):
    """Retorna un string con un guión bajo por cada letra que
    no hasido adivinada. Si una letra del texto aparece en las
    letras intentadas, entonces le agrega como tal en lugar del
    guión.
    Si el texto original tiene espacios, los sutituye con guiones
    normales.

    Entradas y Restricciones:
    -texto: texto a adivinar
    -letrasUsadas: letras que el usuario ha intentado

    Salidas:
    -String con el texto enmascarado"""

    listaPalabras = texto.split()
    resul = ""

    for palabra in listaPalabras:
        for letra in palabra:
            if letra in letrasUsadas:
                resul += letra + " "
            else:
                resul += "_ "
                
        resul += "- "

    return resul[:-2]


def leerIntento(letrasUsadas):
    """Función que pide al usuario que escriba una letra para
    adivinar. Si ya se encuentra en las intentadas o no es una letra,
    debe de imprimir un mensaje de error y volver a pedir la letra.

    Entradas y Restricciones:
    -letrasUsadas: letras que el usuario ha intentado

    Salidas:
    -String con la letra elegida por el usuario"""

    print()
    letra = input("Ingrese una letra: ")
    letra = letra.lower()

    while(len(letra) != 1 or letra not in "abcdefghijklmnñopqrstuvwxyz"
          or letra in letrasUsadas):
        
        print(f"Por favor ingrese una letra que no haya intentado. Letras usadas: {letrasUsadas}")
        letra = input("Ingrese una letra: ")
        letra = letra.lower()
    print()

    return letra


def aciertaIntento(texto, letraIntento):
    """Función booleana que dice si un intento es correcto o no.

    Entradas y Restricciones:
    -texto que se está adivinando
    -letra que intentó el usuario

    Salidas:
    -True si la letra se encuentra en el texto a adivinar,
    False sino"""

    return letraIntento in texto


def imprimirMensajeAcierto():
    """Procedimiento que imprime un mensaje de acierto en caso
    de haber adivinado una letra de la palabra secreta

    Entradas y Restricciones:
    -Ninguna

    Salidas:
    -Mensaje de acierto"""
    
    print("¡Ha adivinado la letra! :D")
    

def imprimirMensajeNoAcierto():
    """Procedimiento que imprime un mensaje de no acierto en caso
    de que la letra ingresada no pertenezaca a la palabra secreta

    Entradas y Restricciones:
    -Ninguna

    Salidas:
    -Mensaje de no acierto"""
    
    print("¡Letra no encontrada! :(")
    

def imprimirMensajeVictoria():
    """Procedimiento que imprime un mensaje de victoria al
    adivinar toda la palabra secreta

    Entradas y Restricciones:
    -Ninguna

    Salidas:
    -Mensaje de victoria"""
    
    print(f"¡Felicidades ha ganado el juego!")
    
    
def imprimirMensajeDerrota(textoOriginal):
    """Procedimiento que imprime un mensaje de derrota al
    no adivinar toda la palabra secreta en los intentos que se
    dieron

    Entradas y Restricciones:
    -textoOriginal: texto que se tenía que adivinar

    Salidas:
    -Mensaje de derrota"""

    print(f"¡Ha perdido el juego! \nLa palabra era {textoOriginal}")
    

def leerJugarNuevamente():
    """Función booleana que pregunta al usuario si quiere jugar
    de nuevo. Sólo acepta "S" ó "N" como respuesta.

    Entradas y Restricciones:
    -Ninguna

    Salidas:
    -True si el usuario escribe "S", False sino"""
    
    print()
    
    respuesta = input("¿Desea jugar de nuevo? (S/N) ")
    respuesta = respuesta.lower()

    while respuesta not in ["s","n"]:
        respuesta = input("¿Desea jugar de nuevo? (S/N) ")
        respuesta = respuesta.lower()

    return respuesta == "s"


def imprimirMensajeDespedida():
    """Procedimiento que imprime un mensaje de despedida
    al usuario 

    Entradas y Restricciones:
    -Ninguna

    Salidas:
    -Mensaje de despedida"""
    print("Gracias por jugar, hasta pronto.")
    

main()






















    









    


