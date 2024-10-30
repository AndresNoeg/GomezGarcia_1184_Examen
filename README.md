# GomezGarcia_1184_Examen_2daUnidad

print(" ")

print(" Andres Noe Gomez Garcia 1184: Examen primer y segundo punto")

print(" ")

#Define una funcion

def my_function():

    #Imprime este mensaje al 
    
  print("Hello from a function")
  
#Invoca funcion

my_function()

![image](https://github.com/user-attachments/assets/b38baf7b-e389-4afc-8dde-851c5940d659)


print(" ")

print(" Andres Noe Gomez Garcia 1184: Examen Tercer punto")

print(" ")

#Define unafuncion

def impresion_funcion(x):

#Imprime una funcion y una variable

  print(x + " Pollo")

#Imprime la funcion con distintos finales

impresion_funcion("Hola")

impresion_funcion("Soy")

impresion_funcion("Noe")


![image](https://github.com/user-attachments/assets/92350862-48ad-4908-9062-81245d8e6dc9)


print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Cuarto punto")
print(" ")

#Define funcion con 2 variables
def dos_argumentos(x, y):
    #Imprime funcion con 2 variables
  print(x + " " + y)

#Invoca la funcion
dos_argumentos("Hola", "Amigo")

![image](https://github.com/user-attachments/assets/edc7686c-7f01-4254-a7a5-faf931660409)


print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Quinto punto")
print(" ")

#Define  una funcion con 2 variables
def un_argumento(x, y):
    #Imprime 
  print(x + " " + y)
#imprime solo una variable
un_argumento("Holiwis","")

![image](https://github.com/user-attachments/assets/23ad79e1-79fb-4a52-bfb3-e687fb9581ad)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Sexto punto")
print(" ")

#Define una funcion que crea una tupla de variables
def funcion_tupla(*amigos):
    #Imprime un mensaje con una variable
  print("El menor de mis amigos es: " + amigos[1])
  print("El mayor de mis amigos es: " + amigos[2])
#Invoca la funcion
funcion_tupla("Noe","Gaelito", "Sosa")

![image](https://github.com/user-attachments/assets/6878573a-c49d-4a97-b14e-404bfec145ec)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Septimo punto")
print(" ")

#Define la funcion
def desorden(c3, c2, c1):
    #imprime un espacio y una variable
  print("El menor de los numeros es: " + c3)
#Invoca la funcion
desorden(c1 = "10", c2 = "7", c3 = "9")

![image](https://github.com/user-attachments/assets/16e669b0-2b29-44ba-ba29-0a1d44c1ac8c)


print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Octavo punto")
print(" ")

#Define una funcion con un diccionario de variables
def diccionario_variables(**l):
    #Escribe un mensaje y la variable
  print("Mis apellidos son " + l["x"])
#invoca la funcion
diccionario_variables(y = "Garcia Sosa", x = "Gomez Garcia")

![image](https://github.com/user-attachments/assets/8d80f83d-0926-4320-90b5-ea641f9d5149)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Noveno punto")
print(" ")

#Define una funcion con una variable determinada
def funcion_pais(pais = "Mexico"):
    #Imprime mensaje y variable
  print("Yo soy de " + pais)

#Invoca la funcion
funcion_pais("Holanda")
funcion_pais("Pais de los juegos")
funcion_pais()
funcion_pais("Escocia")

![image](https://github.com/user-attachments/assets/24e8f0b8-0df7-4905-afb8-597858c347f6)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Decimo punto")
print(" ")

#Define funcion
def funcion_bucle(chatarra):
    #bucle for
  for x in chatarra:
    print(x)
#Declara lista
comida = ["Hamburguesa", "Hot Dogs", "Pizza"]
#Invoca funcion
my_function(comida)

![image](https://github.com/user-attachments/assets/96113e1c-8e9b-4892-9e68-20c8f2ffcdbd)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Onceavo punto")
print(" ")

#Define una funcion
def suma_al_argumento(x):
    #Regresa el resultado de la operacion
  return 86 + x

#Realiza la operacion segun elvalor de x dado entre los parentesis
print(suma_al_argumento(34))
print(suma_al_argumento(4))
print(suma_al_argumento(14))

![image](https://github.com/user-attachments/assets/bb30ad4c-4a7e-4d53-b711-2be6a8ae300c)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Doceavo punto")
print(" ")

#Funcion vacia
def funcion_vacia():
    #si la funcion esta vacia el pass evita el error 
  pass

![image](https://github.com/user-attachments/assets/e88be73d-6639-4cf0-978c-f940095f2dc9)
  
print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Treceavo punto")
print(" ")

#Define una funcion con una variable posicional
def valor_posicional(x, /):
    #Imprime la variable en cuestion
  print(x)
#invoca la funcion con el valor que se le dio
valor_posicional(10)
'''
No se declara con 
palabra clave 
ya que dara error
'''

![image](https://github.com/user-attachments/assets/4695c7dd-25e3-4459-b449-7acace6d7444)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Catorceavo punto")
print(" ")

#Define una funcion con una variable posicional aunque no se espere
def my_function(x):
    #Imprime la variable en cuestion
  print(x)
#invoca la funcion con el valor que se le dio
my_function(10)

![image](https://github.com/user-attachments/assets/fc0c9b41-df76-4793-86ce-5a34b2410d55)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Quinceavo punto")
print(" ")

#Define una funcion con una variable posicional aunque no se espere
def my_function(x, /):
    #Imprime la variable en cuestion
  print(x)
#invoca la funcion con el valor que se le dio
my_function(x=10)
#Dara error

![image](https://github.com/user-attachments/assets/f6918e3b-c4f0-4694-aa3c-447df1e41de3)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Dieciseisavo punto")
print(" ")

#Define funcion para definir variable con palabra clave
def palabras_clave(*, y):
  #Imprime la variable 
  print(y)
#Invoca la funcion
my_function(y = 15)

![image](https://github.com/user-attachments/assets/b2423190-88ac-4330-8a57-331770af3ded)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Diecisieteavo punto")
print(" ")

#Define funcionn con una variable
def palabras_clave(u):
    #Imprime variable
  print(u)
#Invoca la funcion aunque no se usen palabras clave
palabras_clave(25)

![image](https://github.com/user-attachments/assets/353228d0-5f6d-485a-b45f-567b2bac8742)

print(" ")
print(" Andres Noe Gomez Garcia 1184: Examen Dieciochoavo punto")
print(" ")

#Define funcion
def valorpositional(*, k):
  #Imprime variable en la funcion
  print(k)
#Invoca funcion
valorpositional(7)
#Se obtendra error

![image](https://github.com/user-attachments/assets/89477e67-6639-4d2b-b537-acf9d100a4d0)


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

![image](https://github.com/user-attachments/assets/17eba866-b1b0-48b0-b927-2d15d9adb737)

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
tri_recursion(10)

![image](https://github.com/user-attachments/assets/c404c28a-be82-4510-91d3-7180ec2353e6)





















