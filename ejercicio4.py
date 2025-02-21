def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

def comprobar_palindromo():
    palabra = input("Introduzca una palabra: ")
    return palindromo(palabra)

resultado = comprobar_palindromo()
print(resultado)
