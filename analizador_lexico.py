import ply.lex as lex

keywords = {
    # Palabras clave de control de flujo
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'unless': 'UNLESS',
    'while': 'WHILE',
    'until': 'UNTIL',
    'for': 'FOR',
    'in': 'IN',
    'case': 'CASE',
    'when': 'WHEN',
    
    # Definiciones
    'def': 'DEF',
    'class': 'CLASS',
    'module': 'MODULE',
    'end': 'END',
    
    # Control de bucles y métodos
    'break': 'BREAK',
    'next': 'NEXT',
    'return': 'RETURN',
    'yield': 'YIELD',

    # Bloques y excepciones
    'do': 'DO',
    'begin': 'BEGIN',
    'rescue': 'RESCUE',
    'ensure': 'ENSURE',
    'retry': 'RETRY',
    
    # Literales especiales (tratados como keywords) 
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NIL',
    
    # Operadores lógicos de palabra
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    # Otros
    'alias': 'ALIAS',
    'self': 'SELF',
    'super': 'SUPER',
}

tokens_literales = (
    'NUMBER',        # Para Enteros y Flotantes (ej: 123, 3.14)
    'STRING',        # Para Cadenas (ej: "hola", 'mundo') 
    'SYMBOL',        # Para Símbolos (ej: :mi_simbolo)
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
    'MODULO',        # %
    'POWER',         # **

    # Asignación 
    'ASSIGN',        # =
    'PLUS_ASSIGN',   # +=
    'MINUS_ASSIGN',  # -=
    'TIMES_ASSIGN',  # *=
    'DIVIDE_ASSIGN', # /=
    'MOD_ASSIGN',    # %=
    'POWER_ASSIGN',  # **=
    
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
    'SCOPE',           # ::
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
)

tokens = tokens_literales + \
         tokens_identificadores + \
         tokens_operadores + \
         tokens_delimitadores + \
         tuple(keywords.values())