def num_pares(numeros):
    suma = 0
    for i in numeros:
        if i % 2 == 0:
            suma += i
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_pares(numeros))
