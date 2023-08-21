'''Função Print'''

print(12,11,32,456, sep='-', end="##\n")
print(14,19, sep='-')
print(32,11,67,4356, sep='-')

''' sep = separador, usado para separar argumento nao nomeado

ex: print(12, 11 sep='-')
            =
    terminal: 12-11
            
'''
#\r\n -> CRLF(sistema windows)
#\n -> LF (sistema unix)

'''sem o \n no comando end="##\n" ele nao quebraria a linha do resultado no terminal '''