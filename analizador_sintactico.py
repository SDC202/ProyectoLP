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

# Asignación de Variables
def p_assignment(p):
    '''
    assignment : IDENTIFIER ASSIGN expression
               | INSTANCE_VARIABLE ASSIGN expression
               | CLASS_VARIABLE ASSIGN expression
               | GLOBAL_VARIABLE ASSIGN expression
               | CONSTANT ASSIGN expression
               | assignment_array ASSIGN expression
    '''

    # Regla para: x = 5, @x = 5, @@x = 5, $x = 5, X = 5, mi_array[0] = 5

def p_assignment_array(p):
    'assignment_array : IDENTIFIER LBRACKET expression RBRACKET'

# Expresiones Aritméticas
def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MODULE_OP expression
               | expression POWER expression
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_unary(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = ('unary_minus', p[2])

# Definición de Clases
def p_class_definition(p):
    '''
    class_definition : CLASS CONSTANT statements END
                     | CLASS CONSTANT LESS CONSTANT statements END
    '''

    # Regla para: class MiClase ... end
    # Regla para: class Hija < Padre ... end

# Definición de Funciones
def p_function_definition(p):
    '''
    function_definition : DEF IDENTIFIER LPAREN params RPAREN statements END
                        | DEF IDENTIFIER LPAREN RPAREN statements END
                        | DEF IDENTIFIER statements END
    '''

    # Regla para: def mi_func(a, b) ... end
    # Regla para: def mi_func() ... end
    # Regla para: def mi_func ... end (sin paréntesis)

def p_params(p):
    '''
    params : params COMMA IDENTIFIER
           | IDENTIFIER
    '''

    # Regla para definir los parametros

# Estructura de Datos: Hash
def p_expression_hash(p):
    '''
    expression : LBRACE hash_pairs RBRACE
               | LBRACE RBRACE
    '''
    # Regla para: { llave => valor, :otra => 1 }

def p_hash_pairs(p):
    '''
    hash_pairs : hash_pairs COMMA hash_pair
               | hash_pair
    '''

def p_hash_pair(p):
    '''
    hash_pair : expression HASH_ROCKET expression
              | SYMBOL HASH_ROCKET expression
              | STRING HASH_ROCKET expression
    '''

# Ingreso de Datos
def p_io_statement_gets(p):
    '''
    io_statement : IDENTIFIER ASSIGN GETS DOT IDENTIFIER
                 | IDENTIFIER ASSIGN GETS
    '''
    # Regla para: nombre = gets.chomp
    # Regla para: nombre = gets

# Estructura de Control: for
def p_control_statement_for(p):
    '''
    control_statement : FOR IDENTIFIER IN expression statements END
    '''
    # Regla para: for i in (1..5) ... end

# Termina aporte Sebastián De Castro

# Empieza aporte Sebastián Manzanilla



# Terminan aportes Sebastian Manzanilla


parser = yacc.yacc()

parser.errors = []