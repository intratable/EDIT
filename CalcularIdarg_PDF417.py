import unicodedata
from datetime import datetime

dni = "12345678"
apellido = "González"
nombres = "María Isabel"
fecha_nacimiento = "1990/05/15"
sexo = "F"
fecha_vencimiento = "2024/07/31"

def convertir_fecha(input_fecha):
    try:
        fecha_obj = datetime.strptime(input_fecha, "%Y/%m/%d")
        fecha_formateada = fecha_obj.strftime("%y%m%d")
        return str(fecha_formateada)
    except ValueError:
        return "Error: Formato de fecha incorrecto"

def check_digit(s):
    m = [7, 3, 1]
    n = 0

    for i, char in enumerate(s):
        if char.isdigit():
            n += int(char) * m[i % 3]
        else:
            return -1

    return n % 10

def quitar_acentos(cadena):
    cadena_normalizada = ''.join(c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn')
    cadena_limpia = ''.join(c if c.isalnum() or c.isspace() or c == '<' else ' ' for c in cadena_normalizada)
    return cadena_limpia.upper()

def generar_idarg(dni, apellido, nombres, fecha_nacimiento, sexo, fecha_vencimiento):
    fecha_nacimiento = convertir_fecha(fecha_nacimiento)
    fecha_vencimiento = convertir_fecha(fecha_vencimiento)

    DigitoVerificador1 = check_digit(str(dni))
    DigitoVerificador2 = check_digit(fecha_nacimiento)
    DigitoVerificador3 = check_digit(fecha_vencimiento)
    DigitoVerificador4 = check_digit(f"{dni}0{DigitoVerificador1}{fecha_nacimiento}{DigitoVerificador2}{fecha_vencimiento}{DigitoVerificador3}")

    linea1 = f"IDARG{dni}<{DigitoVerificador1}"
    linea2 = f"{fecha_nacimiento}{DigitoVerificador2}{sexo.upper()}{fecha_vencimiento}{DigitoVerificador3}ARG<<<<<<<<<<<{DigitoVerificador4}"
    linea3 = f"{quitar_acentos(apellido)}<<{quitar_acentos(nombres.replace(' ', '<'))}"

    linea1 = linea1.ljust(30, '<')
    linea2 = linea2.ljust(30, '<')
    linea3 = linea3.ljust(30, '<')

    msg = f"""
        {linea1}
        {linea2}
        {linea3}
    """
    print("IDARG :", msg.strip())  # Imprime el mensaje sin los espacios en blanco adicionales al principio y final
    return msg.strip()

print(generar_idarg(dni, apellido, nombres, fecha_nacimiento, sexo, fecha_vencimiento))