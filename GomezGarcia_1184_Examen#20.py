print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Veinteavo punto")
print(" ")

def myfuncion(y):
    if y > 0:
        result = y + myfuncion(y - 1)  # Suma y uso de if-else
        print(result)  # Imprime el resultado en cada paso de retorno
    else:
        result = 0
    return result
#Imprime mensaje
print("Resultados del ejemplo de recursividad:")
myfuncion(10)
