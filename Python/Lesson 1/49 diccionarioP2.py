#Crear un diccionario, llave + valor (key+value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP': 'Object oriente programming',
    'DBMS': 'Database Management System',
}
print(diccionario,'\n')

#recorrer los elementos de un diccionario.
for termino, valor in diccionario.items():
    print(termino, valor)

#recuperar solo los terminos
for termino in diccionario.keys():
    print(termino)

#recuperar solo los valores
for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun elemento
print('IDE' in diccionario)

#agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#remover elemento
diccionario.pop('DBMS')
print(diccionario)

#limpiar diccionario
diccionario.clear()
print(diccionario)

del diccionario
print(diccionario)
