import ply.yacc as yacc
import Analizador_LEXICO_V2

tokens = Analizador_LEXICO_V2.tokens
def p_inicio(p):
    '''inicio : principal'''
    print("Aceptado")

def p_principal(p):
    '''principal    : variable_declaracion principal
                    | variable_asignacion principal
                    | exp_aritmetica principal
                    | variable_declaracion
                    | variable_asignacion 
                    | exp_aritmetica '''

def p_variable_declaracion(p):
    '''variable_declaracion     : ENTERO ID DELIMITADOR
                                | FLOTANTE ID DELIMITADOR
                                | BULEANO ID DELIMITADOR'''
    if p[1] == "entero":
        print("Declaración de un numero entero. Identificador: ", p[2])
    elif p[1] == "flotante":
        print("Declaración de un numero flotante. Identificador: ", p[2])

def p_variable_asignacion(p):
    '''variable_asignacion  : ID ASIGNACION NUMERO DELIMITADOR
                            | ID ASIGNACION ID DELIMITADOR'''
    print("Hola desde asignacion: se asigno ", p[3], "a ", p[1])

def p_exp_aritmetica(p):
    '''exp_aritmetica   : expresion DELIMITADOR
                        '''
    print("Expresion aritmética")

def p_expresion(p):
        '''expresion    : expresion SUMA termino
                        | expresion MENOS termino
                        | termino'''


def p_termino(p):
    '''termino  : termino MULTIPLICACION factor
                | termino ENTRE factor
                | factor'''
    
def p_factor(p):
    '''factor   : NUMERO 
                | PARENTESIS_IZQ expresion PARENTESIS_DER'''
    
def p_error(p):
    print(f"Error de sintaxis en el token: {p}")

#Esta version tiene producciones solo para
    #DECLARACION DE VARIABLES 
    #ASIGNACION DE VARIABLES
    #EXPRESIONES ARITMETICAS

data='''entero .|.x ;
        .|.x <= 10;
        flotante .|.y;
        .|.y <= .|.x;
        10 + 10;
        (50 * 10 + 5);
        '''

yacc.yacc()
a = yacc.parse(data) #devuelve un AST


 

# while True:
#    try:
#        s = entrada("entero .|.x;")
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)