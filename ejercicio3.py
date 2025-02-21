def num_romanos():
    numero=int(input("Introduzca un número para convertirlo en romano: "))
    valores={1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_romano = ""
    for valor, simbolo in valores.items():
        while numero>=valor:
            num_romano+=simbolo
            numero-=valor
    return num_romano


print(num_romanos())  
