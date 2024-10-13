from datetime import datetime, timedelta


def run(hora_entrada, minutos):
    # Convertir la hora de entrada en un objeto datetime
    hora_obj = datetime.strptime(hora_entrada, '%H:%M')
    # Sumar los minutos utilizando timedelta
    nueva_hora = hora_obj + timedelta(minutes=minutos)
    # Convertir la nueva hora a formato de cadena HH:MM
    resultado = nueva_hora.strftime('%H:%M')
    # Imprimir el resultado
    print(resultado)


# llamar a la funcion
run('17:15', 240)