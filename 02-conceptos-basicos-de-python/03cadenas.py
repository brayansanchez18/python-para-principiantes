print('Hola \nmundo')
print("Hola \tmundo")
print("Hola mundo")
print("Hola 'mundo'")
print('Hola "mundo"')

a = '''Esto es
una cadena
multilinea'''
print(a)

x = "Hola Mundo!"
print(x[1])

# Obtenga los caracteres de la posición 1 a la posición 4:
x = "Hola Mundo"
print(x[0:4])

# Obtenga los caracteres desde el principio hasta la posición 3:
x = "Hola Mundo"
print(x[:3])

# El método upper() devuelve la cadena en mayúsculas:
x = "Hola Mundo"
print(x.upper())

# El método lower() devuelve la cadena en minúsculas:
x = "Hola Mundo"
print(x.lower())

# El método strip() elimina cualquier espacio en blanco del principio o del final:
x = "   Hola Mundo"
print(x.strip())

# El método replace() reemplaza una cadena por otra cadena:
x = "Hola Mundo"
print(x.replace("M", "X"))

# Para concatenar, o combinar, dos cadenas se puede utilizar el operador +.
x = "Hola Mundo"
y= ",como estan?"
z=x+y
print(z)

# Las cadenas en Python se pueden formatear con el uso del
# método format(), que es una herramienta muy versátil y
# poderosa para formatear cadenas. El método format()
# en String contiene llaves {} como marcadores de posición
# que pueden contener argumentos según la posición o la
# palabra clave para especificar el orden
peso = 55
x = "Me llamo Javier peso {} kilos"
print(x.format(peso))

peso = 55
edad = 33
altura = 175
x = "Me llamo Javier peso {} kilos, tengo {} años y mido {} cm  "
print(x.format(peso,edad,altura))