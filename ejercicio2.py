import random
def cargar_contraseña():
    longitud=int(input("Introduzca la longitud de su contraseña: "))
    pas=" "
    letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?"
    for i in range (longitud):
        pas+=random.choice(letras)
    return pas

resultado=cargar_contraseña()
print(resultado)