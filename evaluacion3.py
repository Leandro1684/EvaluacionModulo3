#Nombres dados para crear lista
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
#Se crean 3 listas vacías para alojar los nombres
magos = []
cientificos = []
otros = []

#Para separar los nombres utilizaremos un bucle for 
for name in nombres:
        if name == 'Harry Houdini' or name == 'David Blaine' or name == 'Teller': 
            magos.append(name)
        elif name == 'Newton' or name == 'Hawking' or name == 'Einstein': 
            cientificos.append(name)
        elif name == 'Messi' or name == 'Pele' or name == 'Juanes': 
            otros.append(name)


#Definir la Funcion hacer_grandioso()
def hacer_grandioso():
     for name in range(len(magos)):
          magos[name] = f"El gran {magos[name]}" 

#Función para imprimir nombre de cualquier lista
def imprimir_nombres(lista):
     print("Los que componen la lista son: ")
     for name in lista:
          print(name)


print("\n--------------Lista de nombres antes de ser modificados--------------")
imprimir_nombres(nombres)

print("\n---------------------Lista de magos grandiosos-----------------------")
hacer_grandioso()
imprimir_nombres(magos)

print("\n---------------------Lista de los cientificos------------------------")
imprimir_nombres(cientificos)

print("\n----------------------Lista de los restantes-------------------------")
imprimir_nombres(otros)
