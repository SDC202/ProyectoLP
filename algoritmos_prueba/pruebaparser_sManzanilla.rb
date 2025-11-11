# 1. Prueba de Estructura de Control: if-elsif-else
if a > b
  puts "cadena"
elsif a == b
  puts "cadena"
else
  puts "cadena"
end

# 2. Prueba de Estructura de Control: while
contador = 0
while contador < 3
  puts contador
end

# 3. Prueba de Condiciones Lógicas
if a < b && c
  puts "cadena"
end

if a > b or d
  puts "cadena"
end

if not d
  puts "cadena"
end

if a <= 10 and b >= 20
  puts "cadena"
end

# Uso del spaceship
resultado_comparacion = a <=> b

# Uso del operador case-equal (Regla: expression CASE_EQUAL expression)
if 1..10 === 5
  puts "cadena"
end

# 4. Prueba de Estructura de Datos: Array
# Array vacío
array_vacio = []

# Prueba array_elements
mi_lista = [10, "hola", true, nil]

# Prueba acceso a array
puts mi_lista[1]

# 5. Prueba de Impresión (puts)
puts "cadena"

# puts con una expresión
puts 5 * 5 

# puts sin argumentos
puts

# 6. Prueba de uso de funciones
# Llamada a función con argumentos (paréntesis
calcular_suma(a, 5)

# Llamada a función con argumentos sin paréntesis (Ruby-style)
calcular_suma a, 1

# Llamada a función sin argumentos (con paréntesis)
calcular_suma
