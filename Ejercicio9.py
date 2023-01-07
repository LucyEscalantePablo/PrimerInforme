
numero_1 = int(input('valor del numero "a": '))
numero_2 = int(input('valor del numero "b": '))

def sumaRecur (numero_2):
    if numero_2 == 1:
        return 1
    return  1 + sumaRecur( numero_2-1)
    

resultado = sumaRecur(numero_2)
print(resultado + numero_1)