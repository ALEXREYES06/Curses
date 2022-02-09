#set es una coleccion de objetos sin orden ni indices
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#Conocer el largo de un set
print(len(planetas))

#revisar si un elemento está presente
print ('Marte' in planetas) #esta misma pregunta se puede hacer con listas y tuplas

#agregar elementos 
planetas.add('Tierra')
print(planetas)

#No soporta elemtos duplicados
planetas.add('Tierra') #Al imprimir solo se imprime una tierra.
print(planetas)

#eliminar elementos
#planetas.remove('Tierras')
# print(planetas)

#eliminar elemento posiblemente arrojando un error.
planetas.remove('Tierra')
print(planetas)

#Eliminar elemento, sin arrojar error en caso de que no exista el elemento
planetas.discard('Jupiter')
print(planetas)

#limpiar todo el set
planetas.clear()
print(planetas)

#eliminar set.
del(planetas)
print(planetas)