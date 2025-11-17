import ply.yacc as yacc
from analizador_lexico import *

class SymbolTable:
    def __init__(self):
        self.scope_stack = []
        self.enter_scope()
        self.errors = []

    def enter_scope(self, is_loop=False):
        new_scope = {'__is_loop__': is_loop}
        self.scope_stack.append(new_scope)

    def exit_scope(self):
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
        else:
            self.report_error("Error: No se puede salir del ámbito global")

    def declare(self, name, symbol_type, data_type=None, param_count=None, lineno=0):
        scope = self.scope_stack[-1]
        
        if name in scope:
            self.report_error(f"Variable '{name}' ya declarada en este ámbito.", lineno)
            
        scope[name] = {
            'symbol_type': symbol_type,
            'data_type': data_type,
            'param_count': param_count
        }

    def lookup(self, name):
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None

symbol_table = SymbolTable()

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
    statements : statements NEWLINE statement
               | statements statement
               | statement
    '''

    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 3:
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

def p_expression_range(p):
    '''
    expression : expression RANGE_INCLUSIVE expression
               | expression RANGE_EXCLUSIVE expression
    '''
    pass

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
               | IDENTIFIER ASSIGN condition
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

def p_params(p):
    '''
    params : IDENTIFIER COMMA params
           | IDENTIFIER
    '''

    # Regla para definir los parametros

def p_return(p):
    '''
    return : RETURN expression
           | RETURN
           |
    '''

# Definición de Funciones
def p_function_definition(p):
    '''
    function_definition : DEF IDENTIFIER LPAREN params RPAREN statements return END
                        | DEF IDENTIFIER LPAREN RPAREN statements return END
                        | DEF IDENTIFIER statements return END
    '''

    # Regla para: def mi_func(a, b) ... end
    # Regla para: def mi_func() ... end
    # Regla para: def mi_func ... end (sin paréntesis)


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

# 1. Estructura de Control: if-elsif-else
def p_control_statement_if(p):
    '''
    control_statement : IF condition statements END
                      | IF condition statements ELSE statements END
                      | IF condition statements elsif_clauses END
                      | IF condition statements elsif_clauses ELSE statements END
    '''

def p_elsif_clauses(p):
    '''
    elsif_clauses : elsif_clauses ELSIF condition statements
                  | ELSIF condition statements
    '''
    
# 2. Estructura de Control: while
def p_control_statement_while(p):
    'control_statement : WHILE condition statements END'
    # Regla para: while x < 5 ... end

# 3. Condiciones Lógicas
def p_condition(p):
    '''
    condition : expression EQUAL expression
              | expression NOT_EQUAL expression
              | expression GREATER expression
              | expression LESS expression
              | expression GREATER_EQUAL expression
              | expression LESS_EQUAL expression
              | expression SPACESHIP expression
              | expression CASE_EQUAL expression
              | condition LOGICAL_AND condition
              | condition AND condition
              | condition LOGICAL_OR condition
              | condition OR condition
              | LOGICAL_NOT condition
              | NOT condition
              | expression
    '''
    # Permite: x == 5, x > 2, !(x > 2), x > 2 && y < 1, etc.

# 4. Estructura de Datos: Array
def p_expression_array(p):
    '''
    expression : LBRACKET array_elements RBRACKET
               | LBRACKET RBRACKET
    '''
    # Regla para: [1, "dos", 3]

def p_array_elements(p):
    '''
    array_elements : array_elements COMMA expression
                   | expression
    '''

# 5. Impresión
def p_io_statement_puts(p):
    '''
    io_statement : PUTS expression
                 | PUTS
    '''
    # Regla para: puts "Hola"
    # Regla para: puts (sin argumentos)

# 6. Tipo de Función: Llamada a Función
def p_expression_function_call(p):
    '''
    expression : IDENTIFIER LPAREN arguments RPAREN
               | IDENTIFIER LPAREN RPAREN
               | IDENTIFIER arguments
    '''
    # Regla para: mi_funcion(a, b)
    # Regla para: mi_funcion a, b (sin paréntesis)

def p_arguments(p):
    '''
    arguments : arguments COMMA expression
              | expression
    '''

# Terminan aportes Sebastian Manzanilla


parser = yacc.yacc()

parser.errors = []