# probar_lexer.py

# Este script fue hecho con ayuda de IAG para generar los logs de cada prueba.

# Comando
# python probar_lexer.py algoritmos_prueba/algoritmo.rb usuario

import sys
import datetime
from analizador_lexico import lexer  # Importa el lexer que definieron

def probar(archivo_rb, git_user):
    # ... (generación de log_filename) ...
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"logs/lexico-{git_user}-{timestamp}.txt"

    try:
        with open(archivo_rb, 'r') as f:
            data = f.read()

        # Abrir archivo log para escribir
        with open(log_filename, 'w') as log_file:
            # ... (escribe la cabecera del log) ...
            log_file.write(f"--- Log de Análisis Léxico ---\n")
            log_file.write(f"Usuario: {git_user}\n")
            log_file.write(f"Archivo: {archivo_rb}\n")
            log_file.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            log_file.write("-" * 30 + "\n\n")
            log_file.write("Eventos de Análisis (Tokens y Errores):\n")
            print("--- Eventos de Análisis (Tokens y Errores) ---")

            # --- CAMBIO 1: Pasa el log_file al lexer ---
            lexer.log_file = log_file
            lexer.lineno = 1
            
            # Alimentar el lexer
            lexer.input(data)

            # Tokenizar
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No hay más tokens
                
                # Escribe solo los tokens VÁLIDOS (t_error se maneja solo)
                log_entry = f"Token: {tok.type}, Valor: '{tok.value}', Línea: {tok.lineno}\n"
                print(log_entry, end='') 
                log_file.write(log_entry)
            
            # --- CAMBIO 2: Ya no se necesita la sección de errores ---
            # Los errores se escribieron en tiempo real.
            
            print(f"\n" + "-" * 30 + f"\nAnálisis completado. Log guardado en: {log_filename}")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_rb}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    # ... (el resto del script es igual) ...
    if len(sys.argv) != 3:
        print("Uso: python probar_lexer.py <ruta_al_archivo.rb> <tu_usuario_git>")
    else:
        archivo_prueba = sys.argv[1]
        usuario_git = sys.argv[2]
        probar(archivo_prueba, usuario_git)