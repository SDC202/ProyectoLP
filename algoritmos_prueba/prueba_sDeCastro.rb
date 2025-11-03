# --- Algoritmo de Prueba para Analizador Léxico de Ruby ---
# Este archivo contiene texto para probar todas las reglas de tokens definidas en el proyecto.

# 1. Constantes, Keywords (class, module, def, end)
module MiModulo
  class MiClase
    VERSION = 1.0 # CONSTANT, FLOAT
  end
end

holaaa ++++


# 2. Variables (Global, Class, Instance) y Literales (Integer)
$variable_global = 1
@@contador_clase = 0

class ObjetoPrueba
  def initialize(valor) # KEYWORD(def), IDENTIFIER, LPAREN, RPAREN
    @variable_instancia = valor # INSTANCE_VARIABLE, IDENTIFIER
  end
end

# 3. Delimitadores (., (), {}, []) y Keywords
objeto = ObjetoPrueba.new(10) # IDENTIFIER, DOT, IDENTIFIER, LPAREN, INTEGER, RPAREN
mi_array = [1, 2, 3]      # IDENTIFIER, LBRACKET, INTEGER, COMMA, RBRACKET

# 4. Literales (String, Symbol) y Operadores (=>, asumido)
mi_hash = {
  :simbolo_uno => "String con comillas dobles", # SYMBOL, STRING
  'llave_string' => "String con \"escapes\""     # STRING, STRING (con escape)
} # RBRACE

donde ño estoy

# 5. Literales (Regexp) y Semicolon
# (El punto y coma es opcional pero válido)
expresion = /[a-z_0-9]+/ ; # IDENTIFIER, REGEXP, SEMICOLON

# 6. Prueba de Keywords (if, else, end) y Operadores (asumidos)
if 5 > 3 # KEYWORD(if), INTEGER, (operador >), INTEGER
  puts "Prueba de identificador local" # IDENTIFIER, STRING
else
  # Esto es un comentario, debe ser ignorado
end

# 7. Prueba de error léxico
# El carácter ~ no está definido como un token válido.
error_lexico~