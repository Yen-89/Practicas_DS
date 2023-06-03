#Método index (0,1,2,3,4,...-4,-3,-2,-1)
mi_texto = "Esta es una prueba"
resultado = mi_texto[-4] #qué caracter se encuentra en la posición -4
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n") #en qué indice se encuentra la letra 'n'
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a",5,12) #Queremos que nos busque desde el index 5 hasta el 12 la 'a'
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("a") #Queremos que nos busque al revez la letra 'a' de izq a der
print(resultado)

#Slicing
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]  #extracción de los caracteres desde el indice 2 al 5, recordar que no es inclusivo, por lo cual no traerá la F
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]  #desde el indice 2
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]  #antes del indice 5
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]  #desde el caracter 2 hasta el 10 tomando de a 2
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::2]  #desde el indice 0 hasta el último pero saltando de 3 en 3
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1]  #toda la cadena pero al reves
print(fragmento)

