""" 
    Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario
    dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
    por pantalla la duración total en horas, minutos y segundos.
"""

def segundos_dado_intervalo(horas,minutos,segundos):
    # Calcula la duración en seg dado un intervalo(hora,minuto,segundo)
    resultado= horas*3600 + minutos*60 + segundos

    return resultado


def intervalo_dado_segundos(segundos):
    # Calcula la duración (hora,minuto,segundo) dado un intervalo de segundos
    hora= segundos//3600
    minutos= (segundos - hora*3600) // 60
    segundo= (segundos - hora*3600) % 60

    return hora,minutos,segundo


def ingreso_intervalos(intervalo):
    # Ingreso de intervalo
    print(f"INTERVALO {intervalo}")
    hora=int(input("Ingrese la hora:"))
    minuto=int(input("Ingrese los minutos:"))
    segundo=int(input("Ingrese los segundos:"))
    print("")
    return hora,minuto,segundo
    

def main():

    hora_1,minuto_1,segundo_1= ingreso_intervalos(1)
    hora_2,minuto_2,segundo_2= ingreso_intervalos(2)
    suma_intervalos = segundos_dado_intervalo(hora_1,minuto_1,segundo_1) + segundos_dado_intervalo(hora_2,minuto_2,segundo_2)
    horas,minutos,segundos = intervalo_dado_segundos(suma_intervalos)

    print(f"La suma de los dos intervalos es {horas}h, {minutos}m, {segundos}s.")


main()