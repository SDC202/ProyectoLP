# --- Algoritmo de Prueba ---
# Este archivo contiene errores intencionales para probar
# el correcto funcionamiento del proyecto

# --- Setup: Declaraciones Válidas para Contexto ---
normal_var = 0
$global_var = 10
@instance_var = 20
@@class_var = 30
CONSTANTE = "Valor"

array = [1, 2, 3] # Tipo: ARRAY

class MiClase
    variable_de_instancia = "OK"
end

# Error: no se permite operaciones con identificadores de clase
error_1 = $global_var + MiClase

# Error: sintaxis incorrecta
error_2 2

# Error: Asignación de array a una variable que no es un array
error_3 = normal_var[0]

# Error: Operación con menos (-) no soportada para cadenas
error_4 = - "texto"

# Error: Variable no existente
error_5 = variable_no_existente + 1

# Error: Método no existente
error_6 = metodo_no_existente()

# Error: La operación range no soporta tipo array
error_7 = 1 ... array

puts "Prueba de analizador semántico terminada."