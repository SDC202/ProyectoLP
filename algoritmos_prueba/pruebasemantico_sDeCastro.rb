# --- Algoritmo de Prueba para Analizador Semántico ---
# Este archivo contiene 5 errores semánticos intencionales
# para probar las 5 reglas del proyecto.

# --- Test Regla 3: Compatibilidad de Tipos ---
# Error: Intentar sumar INTEGER + STRING
resultado = 10 + "hola"

# --- Test Regla 4: Concordancia de Argumentos ---
def sumar_numeros(a, b)
  return a + b
end

# Error: Se llama con 1 argumento, pero esperaba 2
total = sumar_numeros(5) 

# --- Test Regla 5: 'break' fuera de bucle ---
# Error: 'break' no está dentro de un 'while' o 'for'
break

# --- Test Regla 2: Alcance (Scope) ---
def mi_funcion_scope
  variable_local = "solo vivo aqui"
end

# Error: 'variable_local' no existe en este ámbito (global)
puts variable_local

# --- Test Regla 1: Verificación de Declaración ---
mi_var_declarada = 1

# Error: 'otra_var_no_declarada' no ha sido definida
calculo = mi_var_declarada + otra_var_no_declarada 

puts "Análisis terminado"