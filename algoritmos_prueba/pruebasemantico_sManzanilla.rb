# --- Algoritmo de Prueba para Analizador Semántico ---
# Este archivo contiene 5 errores semánticos intencionales
# para probar las 5 reglas del proyecto.

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

# Error: Acceso a un array en una variable que no es un array 
error_2 = normal_var[0]

# Error: Asignación de array a una variable que no es un array
normal_var[0] = "error 3"

# Error: Operación con menos (-) no soportada para cadenas
error_4 = - "texto"

# Error: Variable no existente
error_5 = variable_no_existente + 1

# Error: Método no existente
metodo_no_existente()

# Error: Método no existente
error_7 = @@class_var.metodo_no_existente()

# Error: La operación range no soporta tipo array
1 ... array

puts "Prueba de analizador semántico terminada."