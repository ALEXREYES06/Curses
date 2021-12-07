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

# Imprimir por rango sin incluir el indice 2
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

#preguntar el largo de una lista
print(len(nombres))

#agreagr un nuevo elemento a la lista
nombres.append('Lorenzo')
print(nombres)

#insertar un elmento en un indice én especifico
nombres.insert(1, 'Octavio')
#Se inserta el nombre de octavio en el uindice 1 y todos los demas valores se mueven a la derecha
print(nombres)

#remover un elemento
nombres.remove('Octavio')
print(nombres)

#remover el ultimo valor agregado a la lista
nombres.pop()
print(nombres)

#aliminar un elemenro en un indice indicado
del nombres[0]
print(nombres)

#limpiar elementos de la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)