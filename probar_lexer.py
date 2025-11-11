# probar_lexer.py

# Este script fue hecho con ayuda de IAG para generar los logs de cada prueba.

# Comando
# python probar_lexer.py algoritmos_prueba/algoritmo.rb usuario

import sys
import datetime
from analizador_lexico import lexer  # Importa el lexer que definieron

def probar(archivo_rb, git_user):
    # Generar nombre del log (ej: lexico-usuario-10-10-2025-14h32.txt)
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"logs/lexico-{git_user}-{timestamp}.txt"

    try:
        # Leer el archivo de prueba
        with open(archivo_rb, 'r') as f:
            data = f.read()

        lexer.errors = []
        lexer.lineno = 1
        
        # Alimentar el lexer
        lexer.input(data)

        # Abrir archivo log para escribir
        with open(log_filename, 'w') as log_file:
            log_file.write(f"--- Log de Análisis Léxico ---\n")
            log_file.write(f"Usuario: {git_user}\n")
            log_file.write(f"Archivo: {archivo_rb}\n")
            log_file.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            log_file.write("-" * 30 + "\n\n")
            log_file.write("Tokens Reconocidos:\n")
            print("--- Tokens Reconocidos ---")

            # Tokenizar y escribir en el log
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No hay más tokens
                
                log_entry = f"Token: {tok.type}, Valor: '{tok.value}', Línea: {tok.lineno}\n"
                print(log_entry, end='') 
                log_file.write(log_entry)

            if lexer.errors:
                log_file.write("\n" + "-" * 30 + "\n")
                log_file.write("Errores Léxicos Encontrados:\n")
                print("\n" + "-" * 30 + "\nErrores Léxicos Encontrados:")
                
                for error in lexer.errors:
                    log_file.write(f"{error}\n")
                    print(error) # También mostrar errores en consola
            
            print(f"\n" + "-" * 30 + f"\nAnálisis completado. Log guardado en: {log_filename}")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_rb}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python probar_lexer.py <ruta_al_archivo.rb> <tu_usuario_git>")
    else:
        archivo_prueba = sys.argv[1]
        usuario_git = sys.argv[2]
        probar(archivo_prueba, usuario_git)