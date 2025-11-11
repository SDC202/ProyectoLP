# Prueba de Definición de Clases
class MiClase
  # Prueba de Asignación (Variables)
  @@contador = 0
  $global = "mundo"
  MI_CONSTANTE = 3.14
  
  # Prueba de Definición de Funciones
  def func_con_params(a, b)
    @instancia = a + b
  end

  def func_sin_params()
    # Prueba de Expresiones Aritméticas
    total = (5 + 3) * -10 # Prueba de binop, grouping y unary
    potencia = 2 ** 3
  end
  
  def func_sin_parens
     puts "sin parentesis"
  end
end

# Prueba de Herencia en Clases
class Hija < MiClase
  # Prueba de Estructura de Control: for
  def iterar
    mi_rango = (1..5)
    for i in mi_rango
      puts i
    end
  end
end

# Prueba de Estructura de Datos: Hash
hash_vacio = {}
hash_lleno = {
  :llave => "valor",
  "otra_llave" => 123
}

# Prueba de Ingreso de Datos
puts "Escribe tu nombre:"
nombre = gets.chomp
puts "Escribe tu edad:"
edad = gets

# Prueba de Asignación (Acceso a Array)
mi_array = [1, 2, 3]
mi_array[0] = 5 # Prueba de 'assignment_array'