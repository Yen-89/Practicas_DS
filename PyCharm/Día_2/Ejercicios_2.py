nu1 = 7.5
nu2 = 2.5
suma = nu1 + nu2
print(type(suma))

#conversión implicita(Py automa lo convierte) y explicita(nosotros lo convertimos)
#implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2 #con esto, python convierte autom el num1 en float
print(sum)

print(type(num1))
print(type(num2))

#explicita
num3 = 5.8
print(num3)
print(type(num3))

#acá convertimos el num3 en un INTEGER
num4 = int(num3)
print(num4)
print(type(num4))

edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)

#Formatear cadenas con .format o sea f
x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y))  #manera tradicional
print("Mis numeros son {} y {}".format(x,y))  #manera con .format
print("La suma de {} y {} es igual a {}".format(x,y,y+x))  #manera con .format pero para suma

color = "rojo"
matricula = 34567

print(f"El auto es {color} y su matricula es {matricula}") #manera más corta y legible


#Operadores
a = 6
b = 2
c = 7
print(f"{a} + {b} es = a {a+b} ")
print(f"{a} mas {b} es igual a {a+b} ")

#División al piso, o sea que sólo pone el resultado pero en entero
print(f"{c} dividido al piso de {y} es igual a {c//b}")

#Modulo
print(f"{c} modulo de {b} es igual {c%b}")

#Redondeo (round)
print(90/7)
print(round(90/7))

resultado = round(90/7)
print(resultado)

#Quiero 2 decimales
valor = round(9.66666666666,3)
print(valor)

num1 = 13.87
print(round(num1))
print(int(num1))





