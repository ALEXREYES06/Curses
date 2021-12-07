#definir una tupla
frutas = ('Naranjas', 'Platano', 'Guayaba') #Cuando trabajamos con tuplas, para que sea una tupla, cuando tenemos solo un valor debemos agregar una coma al final ejemplo: frutas = ('naranjas',)

#saber el largo de la tupla
print(len(frutas))

#accder a un elemento en  particular.
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#acceder a un rango de valores
print(frutas[0:2]) #sin incluir el ultimo indice

#recorrer elemento de la tupla
for fruta in frutas:
    print(fruta, end= ' ') #eL END me sirve para imprimir todo en un solo renglón

#cambiar valor tupla
#frutas[0] = 'Pera'
#No se puede cambiar el valor de un elemento de la tupla, pero puedes convertir la tupla a lista.
frutasLista = list(frutas)
frutasLista [0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas) #Como se pone un salto de línea

#eliminar la Tupla
del frutas
print(frutas)