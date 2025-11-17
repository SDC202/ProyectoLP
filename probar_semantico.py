# probar_semantico.py
import sys
import datetime

# Importa el parser, lexer y la TABLA DE SÍMBOLOS
from analizador_sintactico import parser, lexer, symbol_table

def probar_semantico(archivo_rb, git_user):
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"logs/semantico-{git_user}-{timestamp}.txt" # <-- Nombre de log semántico

    try:
        with open(archivo_rb, 'r') as f:
            data = f.read()

        # --- Reiniciar TODOS los analizadores ---
        lexer.errors = []
        parser.errors = []
        symbol_table.errors = [] # <-- ¡Importante!
        
        # Reinicia la tabla de símbolos (borra el ámbito global anterior)
        symbol_table.__init__() 

        # --- Ejecutar el PARSER (que ahora es semántico) ---
        parser.parse(data, lexer=lexer)
        
        # Abrir log para escribir
        with open(log_filename, 'w') as log_file:
            log_file.write(f"--- Log de Análisis Semántico ---\n")
            log_file.write(f"Usuario: {git_user}\n")
            log_file.write(f"Archivo: {archivo_rb}\n")
            log_file.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            log_file.write("-" * 30 + "\n\n")

            # Tarea 4: Escribir los errores semánticos
            if symbol_table.errors:
                log_file.write("Errores Semánticos Encontrados:\n")
                print("--- Errores Semánticos Encontrados ---")
                for error in symbol_table.errors:
                    log_file.write(f"{error}\n")
                    print(error)
            else:
                log_file.write("Análisis Semántico Exitoso: No se encontraron errores semánticos.\n")
                print("Análisis Semántico Exitoso: No se encontraron errores semánticos.")
            
            # También es útil registrar los otros errores
            if parser.errors:
                log_file.write("\n" + "-" * 30 + "\n")
                log_file.write("Errores Sintácticos Encontrados:\n")
                print("--- Errores Sintácticos Encontrados ---")
                for error in parser.errors:
                    log_file.write(f"{error}\n")
                    print(error)

            if lexer.errors:
                log_file.write("\n" + "-" * 30 + "\n")
                log_file.write("Errores Léxicos Encontrados:\n")
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
        print("Uso: python probar_semantico.py <ruta_al_archivo.rb> <tu_usuario_git>")
    else:
        archivo_prueba = sys.argv[1]
        usuario_git = sys.argv[2]
        probar_semantico(archivo_prueba, usuario_git)