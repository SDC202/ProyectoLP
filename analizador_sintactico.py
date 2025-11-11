import ply.yacc as yacc
from analizador_lexico import *

precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'LOGICAL_NOT'),
    ('nonassoc', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL', 'SPACESHIP', 'CASE_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULE_OP'),
    ('right', 'POWER'),
    ('right', 'UMINUS'),
)

def p_program(p):
    '''
    program : statements
    '''
    p[0] = p[1]

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''

    if len(p) == 3:
        p[0] = p[1] + [p[2]] 
        else:
        p[0] = [p[1]] 

def p_statement(p):
    '''
    statement : expression
              | assignment
              | io_statement
              | control_statement
              | function_definition
              | class_definition
    '''
    p[0] = p[1]

def p_expression_literals(p):
    '''
    expression : INTEGER
               | FLOAT
               | STRING
               | SYMBOL
               | TRUE
               | FALSE
               | NIL
               | REGEXP
    '''
    p[0] = p[1]

def p_expression_variables(p):
    '''
    expression : IDENTIFIER
               | INSTANCE_VARIABLE
               | CLASS_VARIABLE
               | GLOBAL_VARIABLE
               | CONSTANT
    '''
    p[0] = p[1]

def p_expression_array_access(p):
    'expression : IDENTIFIER LBRACKET expression RBRACKET'

def p_expression_dot_call(p):
    '''
    expression : expression DOT IDENTIFIER
               | expression DOT IDENTIFIER LPAREN arguments RPAREN
               | expression DOT IDENTIFIER LPAREN RPAREN
    '''


def p_error(p):
    if p:
        error_msg = f"Error de Sintaxis: Token inesperado '{p.value}' (Tipo: {p.type}) en la línea {p.lineno}"
    else:
        error_msg = "Error de Sintaxis: Final de archivo inesperado (EOF)"
    
    print(error_msg)
    parser.errors.append(error_msg)

# Empieza aporte Sebastián De Castro



# Termina aporte Sebastián De Castro

# Empieza aporte Sebastián Manzanilla



#Terminan aportes Sebastian Manzanilla


parser = yacc.yacc()

parser.errors = []