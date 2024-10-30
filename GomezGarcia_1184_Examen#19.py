print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Diecinueveavo punto")
print(" ")

def suma(a, b, /, *, c, d):
    return a + b + c + d


print(suma(5, 5, c=8, d=8))  #El resultado sera : 26

'''
(5, 6, 7, 8) Al declararse esto dará un error 
porque c y d deben usarse como palabras clave
ya que son variables posicionales declarados en la funcion
'''