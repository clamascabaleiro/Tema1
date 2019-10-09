def comprobaOrde(tupla):
    anterior = tupla[0]
    ordeada = True
    for elemento in tupla:
        if elemento < anterior:
            print("A serie non esta ordeada menor a maior")
            ordeada = False
            break
        anterior = elemento
    if ordeada:
        print("A serie esta ordeada de menor a maior")

comprobaOrde ((1,2,5,45,67))

def Ejercicio9522(caracteres):
    diccionario = dict();
    for caracter in caracteres:
        if caracter in diccionario:
            diccionario [caracter] = diccionario [caracter] + 1
        else:
            diccionario [caracter] = 1
    return diccionario

print (Ejercicio9522("Qué lindo dia que hace hoy"));