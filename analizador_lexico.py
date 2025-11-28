import ply.lex as lex

keywords = {
    # Palabras clave de control de flujo
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'unless': 'UNLESS', #no incluido en el analizador sintactico
    'while': 'WHILE',
    'until': 'UNTIL', #no incluido en el analizador sintactico
    'for': 'FOR',
    'in': 'IN',
    'case': 'CASE', #no incluido en el analizador sintactico
    'when': 'WHEN', #no incluido en el analizador sintactico
    
    # Definiciones
    'def': 'DEF',
    'class': 'CLASS',
    'module': 'MODULE', #no incluido en el analizador sintactico
    'end': 'END',
    
    # Control de bucles y métodos
    'return': 'RETURN',
    'break': 'BREAK',
    'next': 'NEXT',
    'yield': 'YIELD', #no incluido en el analizador sintactico
    'then': 'THEN', #no incluido en el analizador sintactico

    # Bloques y excepciones
    'do': 'DO', #no incluido en el analizador sintactico
    'begin': 'BEGIN', #no incluido en el analizador sintactico
    'rescue': 'RESCUE', #no incluido en el analizador sintactico
    'ensure': 'ENSURE', #no incluido en el analizador sintactico
    'retry': 'RETRY', #no incluido en el analizador sintactico
    
    # Literales especiales (tratados como keywords) 
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NIL',
    
    # Operadores lógicos de palabra
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    # Otros
    'alias': 'ALIAS', #no incluido en el analizador sintactico
    'self': 'SELF', #no incluido en el analizador sintactico
    'super': 'SUPER', #no incluido en el analizador sintactico
    'puts': 'PUTS',
    'gets': 'GETS',
}

tokens_literales = (
    'INTEGER',
    'FLOAT',
    'STRING',
    'SYMBOL',
    'REGEXP',
)

tokens_identificadores = (
    'IDENTIFIER',        # Variables locales y nombres de métodos (ej: mi_variable)
    'INSTANCE_VARIABLE', # Variable de instancia (ej: @nombre)
    'CLASS_VARIABLE',    # Variable de clase (ej: @@contador)
    'GLOBAL_VARIABLE',   # Variable global (ej: $VERSION)
    'CONSTANT',          # Constantes y nombres de Clases/Módulos (ej: MiClase, PI)
)

tokens_operadores = (
    # Aritméticos 
    'PLUS',          # +
    'MINUS',         # -
    'TIMES',         # *
    'DIVIDE',        # /
    'MODULE_OP',        # %
    'POWER',         # **

    # Asignación 
    'ASSIGN',        # =
    'PLUS_ASSIGN',   # += #no incluido en el analizador sintactico
    'MINUS_ASSIGN',  # -= #no incluido en el analizador sintactico
    'TIMES_ASSIGN',  # *= #no incluido en el analizador sintactico
    'DIVIDE_ASSIGN', # /= #no incluido en el analizador sintactico
    'MOD_ASSIGN',    # %= #no incluido en el analizador sintactico
    'POWER_ASSIGN',  # **= #no incluido en el analizador sintactico
    
    # Comparación 
    'EQUAL',         # ==
    'NOT_EQUAL',     # !=
    'GREATER',       # >
    'LESS',          # <
    'GREATER_EQUAL', # >=
    'LESS_EQUAL',    # <=
    'SPACESHIP',     # <=>
    'CASE_EQUAL',    # ===
    
    # Lógicos 
    'LOGICAL_AND',   # &&
    'LOGICAL_OR',    # ||
    'LOGICAL_NOT',   # !
    
    # Otros operadores de Ruby
    'RANGE_INCLUSIVE', # ..
    'RANGE_EXCLUSIVE', # ...
    'HASH_ROCKET',     # => (para Hashes )
    'SCOPE',           # :: #no incluido en el analizador sintactico
)

tokens_delimitadores = (
    'LPAREN',        # (
    'RPAREN',        # )
    'LBRACKET',      # [ 
    'RBRACKET',      # ]
    'LBRACE',        # { 
    'RBRACE',        # }
    'COMMA',         # ,
    'DOT',           # .
    'SEMICOLON',     # ;
    'NEWLINE',       # \n
)

tokens = tokens_literales + \
         tokens_identificadores + \
         tokens_operadores + \
         tokens_delimitadores + \
         tuple(keywords.values())

# Empieza aporte Sebastián De Castro (tokens literales, identificadores y delimitadores)

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)

    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)

    return t

def t_STRING(t):
    r' ( " (\\.|[^"\\])* " ) | ( \' (\\.|[^\'\\])* \' ) '
    t.value = t.value[1:-1]
    
    return t

def t_SYMBOL(t):
    r':[a-zA-Z_]\w*'
    t.value = t.value[1:] 
    
    return t

def t_REGEXP(t):
    r'/(\\.|[^/\\\n])*/'
    
    return t

def t_IDENTIFIER(t):
    r'[a-z_]\w*'
    t.type = keywords.get(t.value, 'IDENTIFIER')

    return t

def t_INSTANCE_VARIABLE(t):
    r'@[a-zA-Z_]\w*'

    return t

def t_CLASS_VARIABLE(t):
    r'@@[a-zA-Z_]\w*'

    return t

def t_GLOBAL_VARIABLE(t):
    r'\$[a-zA-Z_]\w*'

    return t

def t_CONSTANT(t):
    r'[A-Z]\w*'

    return t

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_SEMICOLON = r';'

# Termina aporte Sebastián De Castro

# Empieza aporte Sebastián Manzanilla (tokens operadores)

# Tokens de 3 caracteres
t_POWER_ASSIGN = r'\*\*='
t_RANGE_EXCLUSIVE = r'\.\.\.'
t_CASE_EQUAL = r'==='
t_SPACESHIP = r'<=>'

# Tokens de 2 caracteres
t_POWER = r'\*\*'
t_RANGE_INCLUSIVE = r'\.\.'
t_SCOPE = r'::'
t_HASH_ROCKET = r'=>'

t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='

t_GREATER_EQUAL   = r'>='
t_LESS_EQUAL      = r'<='
t_EQUAL           = r'=='
t_NOT_EQUAL       = r'!='

t_LOGICAL_AND     = r'&&'
t_LOGICAL_OR      = r'\|\|'

# Tokens de 1 caracter
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE_OP = r'%'
t_GREATER = r'>'
t_LESS = r'<'
t_LOGICAL_NOT = r'!'

#Definiciones movidas por prioridad
t_DOT = r'\.'

# Termina aporte Sebastián Manzanilla

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # return t


def t_error(t):
    error_msg = f"Error Léxico: Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}"
    lexer.errors.append(error_msg)
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()

lexer.errors = []