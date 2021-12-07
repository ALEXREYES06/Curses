#Crear un diccionario, llave + valor (key+value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP': 'Object oriente programming',
    'DBMS': 'Database Management System',
}
print(diccionario,'\n')

#imprimir largo de diccionario
print(len(diccionario))

#acceder a un elemento en especificoEs necesario proporciona el key
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#modificar un elemento
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
