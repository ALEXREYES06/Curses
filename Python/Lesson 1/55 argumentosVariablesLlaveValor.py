#diccionario = {
   # 'IDE':'Integrated Development Enviroment',
  #  'OOP': 'Object oriente programming',
 #   'DBMS': 'Database Management System',
#}

def listarTerminos (**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos( IDE ='Integrated Development Enviroment', OOP = 'Object Oriented Programming')
