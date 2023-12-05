import ply.yacc as yacc
import Analizador_LEXICO_V2

tokens = Analizador_LEXICO_V2.tokens

class Node:
    def __init__(self, node_type, **kwargs):
        self.node_type = node_type
        self.attributes = kwargs

    def imprimir(self, ident):
        print(f"{ident}Nodo: {self.node_type}")
        for key, value in self.attributes.items():
            print(f"{ident}{key}: {value}")

def imprimir_arbol(node, ident=""):
    node.imprimir(ident)
    if hasattr(node, "children") and node.children:
        for child in node.children:
            imprimir_arbol(child, ident + "  ")    



def p_inicio(p):
    '''inicio : principal'''
    print("Aceptado")
    p[0] = Node("program", child=p[1])

def p_principal(p):
    '''principal    : variable_declaracion principal
                    | variable_asignacion principal
                    | exp_aritmetica principal
                    | variable_declaracion
                    | variable_asignacion 
                    | exp_aritmetica '''
    if len(p) == 2:
        p[0] = Node("block", child=p[1])
    else:
        p[0] = Node("block", children=[p[1], p[2]])

def p_variable_declaracion(p):
    '''variable_declaracion     : ENTERO ID DELIMITADOR
                                | FLOTANTE ID DELIMITADOR
                                | BULEANO ID DELIMITADOR'''
    node_type = "declaration"
    identifier = p[2]
    p[0] = Node(node_type, identifier=identifier)

    print(f"{node_type.capitalize()} de un numero {p[1]}. Identificador: {identifier}")

def p_variable_asignacion(p):
    '''variable_asignacion  : ID ASIGNACION NUMERO DELIMITADOR
                            | ID ASIGNACION ID DELIMITADOR
                            | ID ASIGNACION exp_aritmetica DELIMITADOR'''
    node_type = "assignment"
    identifier = p[1]
    value = p[3]
    p[0] = Node(node_type, identifier=identifier, value=value)

    print(f"Se asigno {value} a {identifier} \n")

def p_exp_aritmetica(p):
    '''exp_aritmetica   : expression DELIMITADOR'''
    print("Expresion aritmética")

def p_expression(p):
    '''
    expression : expression SUMA expression
               | expression MENOS expression
               | expression ENTRE expression
               | expression MULTIPLICACION expression
               | NUMERO
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        print(p[0])

def p_error(p):
    print(f"Error de sintaxis en el token: {p}")

# se cambio el nombre de imprimeEsta 'imprimeEsta'   : 'IMPRIME'
def p_imprime_esta(p):
    '''imprimeEsta : IMPRIME PARENTESIS_IZQ NUMERO PARENTESIS_DER DELIMITADOR'''
    if len(p) == 2:
        p[0] = Node("number", value=p[1])
    else:
        p[0] = p[2]


data = '''
entero .|.x ;
.|.x <= 10;
flotante .|.y;
.|.y <= 11;
10 + 10;
20 + 15;
5 * 6;
'''


yacc.yacc()
a = yacc.parse(data)  # devuelve un AST
a.imprimir("")
imprimir_arbol(a)
print(a.node_type)
print(a.attributes['child'])