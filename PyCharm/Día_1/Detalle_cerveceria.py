#Mejor amigo tiene una fabrica de cerveza, le falta ponerle nombre a su cerveza.
#Hacer un programa con dos preguntas y nos ayude a llegar al nombre de la cerveza

##Código dos preguntas con respuestas
#Primera opción
print(input("Ingresa el nombre de tu mascota: "))
print(input("Ingresa la especie de tu mascota: "))

#Segunda opción
print(input("Ingresa el nombre de tu ciudad favorita: "))
print(input("Ingresa el tipo de cerveza que venderás: "))


##Combinar estas dos preguntas en una línea para que me una las dos respuestas y así crear una marca
#Primera opción
print("El nombre de tu cerveza es: " + input("Ingresa el nombre de tu mascota: ")[:5] + input("Ingresa la especie de tu mascota: "))
#Segunda opción
print("El nombre de tu cerveza es: " + (input("Ingresa el nombre de tu ciudad favorita: "))[:4] + (input("Ingresa el tipo de cerveza que venderás: ")))

##El nombre de la cerveza se imprima en comillas
print("El nombre de tu cerveza es ' " + input("Ingresa el nombre de tu ciudad favorita: ")[:4] + " " + input("Ingresa el tipo de cerveza que venderás: ") + " ' ")
print("El nombre de tu cerveza es ' " + input("Ingresa el nombre de tu ciudad favorita: ")[:4] + input("Ingresa el tipo de cerveza que venderás: ") + " ' ")