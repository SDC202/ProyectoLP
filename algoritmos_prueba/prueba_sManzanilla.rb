# --- Algoritmo de Prueba para Analizador Léxico de Ruby ---
# Este archivo contiene texto para probar todas las reglas de tokens definidas en el proyecto.

# Operadores Aritméticos y de Potencia
resultado_arit = 10 + 5 - 2 * 3 / 2 % 4 ** 2

# Asignación y Asignaciones Compuestas
a = 10 
b = 20
a += 5    # PLUS_ASSIGN
b -= 10   # MINUS_ASSIGN
b *= 2    # TIMES_ASSIGN
a /= 3    # DIVIDE_ASSIGN 
b %= 4    # MOD_ASSIGN
c **= 3   # POWER_ASSIGN

# Comparación
if (a == 5) && (b != 0)

    # Operadores de orden y spaceship
    if 5 > 3 && 4 < 6 && 5 >= 5 && 3 <= 3 && 5 <=> 3 == 1

        # Case Equality
        case "test"
        when String === "test" # CASE_EQUAL
            break
        end
    end
end

# Operadores Lógicos
variable_bool = true || false && !true

# Rangos
mi_rango_inc = 1..10    # RANGE_INCLUSIVE
mi_rango_exc = 1...10   # RANGE_EXCLUSIVE

# Hash Rocket y Scope
mi_hash = {
    clave => "valor" # HASH_ROCKET (Note: La flecha => es el operador)
}

MiClase::VARIABLE_CONSTANTE