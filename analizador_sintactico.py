import ply.yacc as yacc
from analizador_lexico import *

class SymbolTable:
    def __init__(self):
        self.scope_stack = []
        self.enter_scope()
        self.errors = []

    def enter_scope(self, is_loop=False, is_function=False):
        new_scope = {'__is_loop__': is_loop, '__is_function__': is_function}
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
    
    def check_loop(self):
        for scope in reversed(self.scope_stack):
            if scope.get('__is_loop__', False):
                return True
        return False

    def check_function(self):
        for scope in reversed(self.scope_stack):
            if scope.get('__is_function__', False):
                return True
        return False

    def report_error(self, message, lineno=0):
        error_msg = f"Error Semántico (Línea {lineno}): {message}"
        self.errors.append(error_msg)
        print(error_msg)

    def check_types(self, op, type1, type2, lineno=0):
        numeric_types = ['INTEGER', 'FLOAT']
        
        if op in ['+', '-', '*', '/', '%', '**']:
            if type1 in numeric_types and type2 in numeric_types:
                return 'FLOAT' if 'FLOAT' in (type1, type2) else 'INTEGER'
            
            if op == '+' and type1 == 'STRING' and type2 == 'STRING':
                return 'STRING'
            
            self.report_error(f"Operador '{op}' no soportado entre {type1} y {type2}.", lineno)
            return 'ERROR_TYPE'

        if op in ['>', '<', '==', '!=', '>=', '<=']:
            if (type1 == type2) or (type1 in numeric_types and type2 in numeric_types):
                return 'BOOLEAN'
            
            self.report_error(f"Comparación '{op}' no soportada entre {type1} y {type2}.", lineno)
            return 'ERROR_TYPE'
        
        if op in ['and', 'or', '&&', '||']:
            return 'BOOLEAN'

        return 'UNKNOWN'

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

start = 'program'

def p_empty(p):
    'empty :'
    pass

def p_enter_scope(p):
    'enter_scope : empty'
    symbol_table.enter_scope()

def p_enter_loop_scope(p):
    'enter_loop_scope : empty'
    symbol_table.enter_scope(is_loop=True)

def p_exit_scope(p):
    'exit_scope : empty'
    symbol_table.exit_scope()

def p_program(p):
    'program : statements'
    pass

def p_statements(p):
    '''
    statements : statements statement
               | empty
    '''
    pass

def p_statement(p):
    '''
    statement : assignment
              | special_assignment
              | io_statement
              | control_statement
              | function_definition
              | return_statement
              | class_definition
              | SEMICOLON
    '''
    pass

def p_expression_literals(p):
    '''
    expression : INTEGER
               | FLOAT
               | STRING
               | SYMBOL
               | REGEXP
               | range
    '''
    p[0] = p.slice[1].type

def p_expression_booleans(p):
    '''
    expression : TRUE
               | FALSE
               | NIL
               | condition
    '''
    p[0] = 'BOOLEAN'

def p_expression_variables(p):
    '''
    expression : IDENTIFIER
               | INSTANCE_VARIABLE
               | CLASS_VARIABLE
               | GLOBAL_VARIABLE
               | CONSTANT
               | array_access
    '''
    name = p[1]
    symbol = symbol_table.lookup(name)
    
    if symbol is None:
        if p.lineno(1) != 0:
            symbol_table.report_error(f"Variable o identificador '{name}' no definido.", p.lineno(1))
            p[0] = 'ERROR_TYPE'
    elif symbol['symbol_type'] != 'VARIABLE':
        symbol_table.report_error(f"'{name}' no es una variable.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    else:
        p[0] = symbol['data_type']

def p_range(p):
    '''
    range : expression RANGE_EXCLUSIVE expression
               | expression RANGE_INCLUSIVE expression
    '''
    lineno = p.lineno(2)

    required_types = ['INTEGER', 'FLOAT']

    print(p[1])
    
    if p[1] not in required_types or p[3] not in required_types:

        symbol_table.report_error(
            f"El rango permite operaciones entre {required_types}, pero se encontró {p[1]} y {p[3]}.",
            lineno
        )
        p[0] = 'ERROR_TYPE'
        return
        
    p[0] = 'RANGE'

def p_expression_dot_call(p):
    '''
    expression : IDENTIFIER DOT IDENTIFIER
               | IDENTIFIER DOT function_call
    '''
    identifier_name = p[3]
    symbol = symbol_table.lookup(identifier_name)
    if symbol is None:
        symbol_table.report_error(f"Propiedad '{identifier_name}' no definida.", p.lineno(3))
        p[0] = 'ERROR_TYPE'
    else:
        p[0] = 'UNKNOWN'

def p_expression_array(p):
    '''
    expression : LBRACKET array_elements RBRACKET
               | LBRACKET RBRACKET
    '''
    p[0] = 'ARRAY'

def p_array_elements(p):
    '''
    array_elements : array_elements COMMA expression
                   | expression
    '''
    pass

def p_special_assignment(p):
    '''
    special_assignment : IDENTIFIER PLUS_ASSIGN expression
                       | IDENTIFIER MINUS_ASSIGN expression
                       | IDENTIFIER TIMES_ASSIGN expression
                       | IDENTIFIER DIVIDE_ASSIGN expression
                       | IDENTIFIER MOD_ASSIGN expression
                       | IDENTIFIER POWER_ASSIGN expression
    '''

    var_name = p[1]
    symbol = symbol_table.lookup(var_name)

    if symbol is None:
        symbol_table.report_error(f"Identificador '{var_name}' no definido.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
        return

    var_type = symbol['data_type']
    op = p[2]
    expr_type = p[3]
    numeric_types = ['INTEGER', 'FLOAT']

    if var_type not in numeric_types:
        symbol_table.report_error(f"La asignación especial '{op}' solo es permitida para variables INTEGER o FLOAT. '{var_name}' es {var_type}.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    elif expr_type not in numeric_types:
        symbol_table.report_error(f"La expresión asignada a '{op}' debe ser INTEGER o FLOAT, pero se encontró {expr_type}.", p.lineno(3))
        p[0] = 'ERROR_TYPE'
    else:
        if expr_type == 'FLOAT' and var_type == 'INTEGER':
            symbol['data_type'] = 'FLOAT'
            p[0] = 'FLOAT'
        else:
            p[0] = var_type

def p_assignment(p):
    '''
    assignment : IDENTIFIER ASSIGN expression
               | INSTANCE_VARIABLE ASSIGN expression
               | CLASS_VARIABLE ASSIGN expression
               | GLOBAL_VARIABLE ASSIGN expression
               | CONSTANT ASSIGN expression
               | array_access ASSIGN expression
    '''
    var_name = p[1]
    expr_type = p[3]
    
    if isinstance(var_name, str):
        symbol_table.declare(var_name, 'VARIABLE', data_type=expr_type, lineno=p.lineno(1))

def p_array_access(p):
    'array_access : IDENTIFIER LBRACKET expression RBRACKET'
    
    array_name = p[1]
    symbol = symbol_table.lookup(array_name)
    if symbol is None:
        symbol_table.report_error(f"Identificador '{array_name}' no definido.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    elif symbol['data_type'] != 'ARRAY':
        symbol_table.report_error(f"'{array_name}' no es un array.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    else:
        p[0] = 'UNKNOWN'

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MODULE_OP expression
               | expression POWER expression
    '''
    type1 = p[1]
    op = p[2]
    type2 = p[3]
    
    result_type = symbol_table.check_types(op, type1, type2, p.lineno(2))
    p[0] = result_type

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_function_call(p):
    'expression : function_call'

def p_function_call(p):
    '''
    function_call : IDENTIFIER LPAREN arguments RPAREN
                  | IDENTIFIER LPAREN RPAREN
                  | IDENTIFIER arguments
    '''
    func_name = p[1]
    arg_list = []

    if len(p) == 5:
        arg_list = p[3]
    elif len(p) == 3:
        arg_list = p[2]

    num_args = len(arg_list)
    symbol = symbol_table.lookup(func_name)

    if symbol is None:
        symbol_table.report_error(f"Función '{func_name}' no definida.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    elif symbol['symbol_type'] != 'FUNCTION':
        symbol_table.report_error(f"'{func_name}' no es una función, es {symbol['symbol_type']}.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    elif symbol['param_count'] != num_args:
        symbol_table.report_error(
            f"Función '{func_name}' esperaba {symbol['param_count']} argumentos, pero recibió {num_args}.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    else:
        p[0] = 'UNKNOWN'

def p_arguments(p):
    '''
    arguments : arguments COMMA expression
              | expression
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_expression_unary(p):
    "expression : MINUS expression %prec UMINUS"
    if p[2] not in ['INTEGER', 'FLOAT']:
        symbol_table.report_error(f"Operador '-' no soportado para {p[2]}.", p.lineno(1))
        p[0] = 'ERROR_TYPE'
    else:
        p[0] = p[2]

def p_class_definition(p):
    '''
    class_definition : CLASS CONSTANT enter_scope statements exit_scope END
                     | CLASS CONSTANT LESS CONSTANT enter_scope statements exit_scope END
    '''
    class_name = p[2]
    symbol_table.declare(class_name, 'CLASS', lineno=p.lineno(1))

def p_param_list(p):
    '''
    param_list : IDENTIFIER COMMA param_list
           | IDENTIFIER
    '''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

# Definición de Funciones
def p_function_definition(p):
    '''
    function_definition : DEF func_name_hook func_header statements exit_scope END
    '''
    pass

def p_func_name_hook(p):
    'func_name_hook : IDENTIFIER'
    p[0] = p[1]

def p_func_header(p):
    '''
    func_header : LPAREN param_list RPAREN 
                | LPAREN RPAREN
                | empty
    '''
    func_name = p[-1]
    print(func_name)
    param_list = []
    
    if len(p) == 4:
        param_list = p[2]
    
    symbol_table.declare(func_name, 'FUNCTION', param_count=len(param_list), lineno=p.lineno(0))
    
    symbol_table.enter_scope(is_function=True)
    
    for param in param_list:
        symbol_table.declare(param, 'VARIABLE', data_type='UNKNOWN', lineno=p.lineno(0))
    
    p[0] = param_list

def p_return_statement(p):
    '''
    return_statement : RETURN expression
                     | RETURN
    '''

    if not symbol_table.check_function():
        symbol_table.report_error("'return' no puede usarse fuera de una definición de función.", p.lineno(1))

    pass

def p_expression_hash(p):
    '''
    expression : LBRACE hash_pairs RBRACE
               | LBRACE RBRACE
    '''
    p[0] = 'HASH'

def p_hash_pairs(p):
    '''
    hash_pairs : hash_pairs COMMA hash_pair
               | hash_pair
    '''
    pass

def p_hash_pair(p):
    '''
    hash_pair : expression HASH_ROCKET expression
              | SYMBOL HASH_ROCKET expression
              | STRING HASH_ROCKET expression
    '''
    pass

def p_io_statement_puts(p):
    '''
    io_statement : PUTS expression
                 | PUTS
    '''
    p[0] = "PUTS"

def p_io_statement_gets(p):
    '''
    io_statement : IDENTIFIER ASSIGN GETS DOT IDENTIFIER
                 | IDENTIFIER ASSIGN GETS
    '''
    var_name = p[1]
    symbol_table.declare(var_name, 'VARIABLE', data_type='STRING', lineno=p.lineno(1))

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
    if len(p) == 4:
        p[0] = symbol_table.check_types(p[2], p[1], p[3], p.lineno(2))
    elif len(p) == 3:
        p[0] = 'BOOLEAN'
    else:
        p[0] = p[1]

def p_control_statement_for(p):
    '''
    control_statement : FOR for_setup statements exit_scope END
    '''
    pass

def p_for_setup(p):
    '''
    for_setup : IDENTIFIER IN expression enter_loop_scope
    '''
    iterator_var = p[1]

    symbol_table.declare(iterator_var, 'VARIABLE', data_type='UNKNOWN', lineno=p.lineno(1))
    
    pass

def p_control_statement_if(p):
    '''
    control_statement : IF condition enter_scope statements exit_scope END
                      | IF condition enter_scope statements exit_scope ELSE enter_scope statements exit_scope END
                      | IF condition enter_scope statements elsif_clauses exit_scope END
                      | IF condition enter_scope statements elsif_clauses ELSE enter_scope statements exit_scope END
    '''
    pass

def p_elsif_clauses(p):
    '''
    elsif_clauses : ELSIF condition statements elsif_clauses
                  | ELSIF condition statements
    '''
    
def p_control_statement_while(p):
    'control_statement : WHILE condition enter_loop_scope statements exit_scope END'

def p_statement_break(p):
    'statement : BREAK'
    if not symbol_table.check_loop():
        symbol_table.report_error("'break' no puede usarse fuera de un bucle.", p.lineno(1))

def p_statement_next(p):
    'statement : NEXT'
    if not symbol_table.check_loop():
        symbol_table.report_error("'next' no puede usarse fuera de un bucle.", p.lineno(1))

def p_error(p):
    if p:
        error_msg = f"Error de Sintaxis: Token inesperado '{p.value}' (Tipo: {p.type}) en la línea {p.lineno}"
    else:
        error_msg = "Error de Sintaxis: Final de archivo inesperado (EOF). Es posible que haya un entorno indebidamente delimitado"
    
    print(error_msg)
    parser.errors.append(error_msg)


parser = yacc.yacc()

parser.errors = []