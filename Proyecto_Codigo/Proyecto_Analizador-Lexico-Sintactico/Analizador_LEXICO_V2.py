import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = {
    'entero'    : 'ENTERO',
    'buleano'   : 'BULEANO',
    'flotante'  : 'FLOTANTE',
    'SI'        : 'SI',
    'EntonCes'  : 'ENTONCES',
    'Para'      : 'PARA',
    'MiEntras'  : 'MIENTRAS',
    ':~*'       : 'FUNCION',
    'imprimeEsta'   : 'IMPRIME'  # Nueva palabra reservada
}

tokens = [
    #Operadores aritméticos 4
    'SUMA',
    'MULTIPLICACION',
    'MENOS',
    'ENTRE',
    #Op. Relacionales 6
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_O_IGUAL_QUE',
    'MAYOR_O_IGUAL_QUE',
    'DIFERENTE_DE',
    'IGUAL_A',
    
    #NO se como nombrar a estos 3
    'NUMERO',
    'ID',
    'CADENA',
    'RESERVED',


    #Delimitadores 3
    'DELIMITADOR',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    
    #OTROS 3
    'ASIGNACION',
    'COMENTARIO',
    'SALTO_LINEA',
    #19
] + list(reservadas.values())


#ER para los tokens

t_SUMA = r'\+'
t_MULTIPLICACION = r'\*'
t_MENOS = r'\-'
t_ENTRE = r'/'

t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_O_IGUAL_QUE = r'<=3'
t_MAYOR_O_IGUAL_QUE = r'=>\*'

t_DIFERENTE_DE = r'{\|}'
t_ASIGNACION = r'<='
t_IGUAL_A = r'='
t_DELIMITADOR = r";"

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_ignore = ' \t '
#t_SALTO_LINEA =r'\n'


def t_NUMERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t 

t_ID =  r'.\|.[a-zA-Z0-9]+'

def t_RESERVED(t):
    r'[a-zA-Z]+'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    return t
#t_CADENA = ''

t_COMENTARIO = r'"[^"]*"'

def t_SALTO_LINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Carácter ilegal: A", t.value[0])
    t.lexer.skip(1)

def t_imprimeEsta(t):
    r'imprimeEsta'
    return t

# Construir el lexer
data = 'entero .|.x;'
lexer = lex.lex()

# Prueba del lexer

# data = '''
# +
# *
# -
# /
# <
# >
# (
# )
# <=3
# =>*
# {|}
# .|.VARIABLE1    <=  4656 ;
# entero ;
# SI .|.x <= 10 ;
# '''

#lexer.input(data)


# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     #print(tok)
#     print(f'Tipo: {tok.type}, Valor: {tok.value}')
