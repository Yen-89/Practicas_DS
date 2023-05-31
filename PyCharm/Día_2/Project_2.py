#Empresa dónde los vendedores reciben un 13% por venta total, calcular comisiones creando un programa que
#pregunte el nombre y cuánto han vendido en este mes
#el programa debe responder con una frase que lleve el nombre del vendedor y el monto correspondido por las comisiones

#Utilizar input para preguntar nombre y ventas con variables, convertir uno de esos ingresos en float
#Después calcular el 13% = valor * 13 / 100 y almacenar este resultado en una variable, no tenga más de 2 decimales
#print con formato

#Prefuntas y transformación de str a int

nombre = input("¿Cuál es tu nombre?: ")
ventas = int(input("¿Cuánto vendiste este mes?: "))

#Transformar el dato str en int
#ventas = int(ventas)

#Comisión y redondeo
comision = round(ventas * 13 / 100,2)

#Redondeo
#comision = round(comision,2)

#Frase
print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
