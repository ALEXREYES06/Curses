#definir lista
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

#imprimir lista de nombres
print(nombres)

#acceder de manera individual
print(nombres[0])
print(nombres[1])

#acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir por rango sin incluir el indice 2
print(nombres[0:2])

#ir del uiniocio de la lista al indice sin incluirlo
print(nombres[:3])

#ir del indice indicado hastya el final
print(nombres[1:])

#cambiar valor de la lista
nombres[3]= 'Ivone'
print(nombres)

#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No esxisten más nomnres en la lista')