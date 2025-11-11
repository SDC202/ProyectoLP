# probar_sintactico.py

# Este script fue hecho con ayuda de IAG para generar los logs de cada prueba.

# Comando
# python probar_sintactico.py algoritmos_prueba/algoritmo.rb usuario

import sys
import datetime
from analizador_sintactico import parser
from analizador_lexico import lexer

def probar_sintactico(archivo_rb, git_user):
    # Generar nombre del log
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"logs/sintactico-{git_user}-{timestamp}.txt" # Nombre de log de sintaxis

    try:
        with open(archivo_rb, 'r') as f:
            data = f.read()

        # Limpiar listas de errores (importante para múltiples pruebas)
        parser.errors = []
        lexer.errors = [] # Asumiendo que modificaste tu lexer como te indiqué
        
        # Asignar el log_file al lexer (si usas ese método)
        # Opcional, pero recomendado
        if hasattr(lexer, 'log_file'):
             lexer.log_file = None # Para que no escriba doble
        
        # --- Ejecutar el PARSER ---
        parser.parse(data, lexer=lexer)
        
        # Abrir log para escribir
        with open(log_filename, 'w') as log_file:
            log_file.write(f"--- Log de Análisis Sintáctico ---\n")
            log_file.write(f"Usuario: {git_user}\n")
            log_file.write(f"Archivo: {archivo_rb}\n")
            log_file.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            log_file.write("-" * 30 + "\n\n")

            # Escribir Errores Sintácticos
            if parser.errors:
                log_file.write("Errores Sintácticos Encontrados:\n")
                print("--- Errores Sintácticos Encontrados ---")
                for error in parser.errors:
                    log_file.write(f"{error}\n")
                    print(error)
            else:
                log_file.write("Análisis Sintáctico Exitoso: No se encontraron errores.\n")
                print("Análisis Sintáctico Exitoso: No se encontraron errores.")
            
            # Escribir Errores Léxicos
            if lexer.errors:
                log_file.write("\n" + "-" * 30 + "\n")
                log_file.write("Errores Léxicos Encontrados (detectados durante sintaxis):\n")
                print("--- Errores Léxicos Encontrados ---")
                for error in lexer.errors:
                    log_file.write(f"{error}\n")
                    print(error)

        print(f"\nAnálisis completado. Log guardado en: {log_filename}")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_rb}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python probar_sintactico.py <ruta_al_archivo.rb> <tu_usuario_git>")
    else:
        archivo_prueba = sys.argv[1]
        usuario_git = sys.argv[2]
        probar_sintactico(archivo_prueba, usuario_git)