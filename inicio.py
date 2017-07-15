#prubas y basico python
#para importar cualquier libreria o modulo: import
#para alias: import __ as __

import random
a = random.randrange(20) #imprime un randomico de N-1
print(a)
b = random.randrange(3,7) #imprime un randomico del rango
print(b)
c = random.randrange(4,70,3)#imprime un randomico del rango contando el valor del 3er
print(c)

#funciones al definirlas deben tener : al final y luego ser invocadas
def suma(): #todas las definiciones deben ir con parentesis y : al final; siempre debe invocarse
    d = a + b
    e = a + c
    f = b + c
    return print("Los números son: ", a, ", ", b, " y ", c , "las sumas son:", d, " ", e, " ", f)
#para imprimir texto adicional con "" y separados por comas o + si son muchos
suma()#invocación de la funcion

def comp(d, e, f): #parametros seran locales
    suma1 = d
    suma2 = e
    suma3 = f
    #loops
    if suma1 < suma2 and suma2 < suma3: #las condicionales son literales y deben terminar on los ':'
        print("La suma menor es: ", suma1, " y la suma mayor es: ", suma3)
    elif suma1 > suma2 and suma1 < suma3: #equivalente al else if
        print("La suma menor es: ", suma2, " y la suma mayor es: ", suma3)
    #else
        #print("La suma menor es: ", suma3, " y la suma mayor es: ", suma2)
    print(" ")
print ("fin de programa") #final del if
    #if puede tener pass = nada que ejecutar

#introduccion de datos
num = int (input)
