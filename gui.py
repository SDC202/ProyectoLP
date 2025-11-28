# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from analizador_lexico import lexer
from analizador_sintactico import parser, symbol_table

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Ruby - Grupo 11")
        self.root.geometry("900x700")

        # Menú de Opciones
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir Archivo", command=self.cargar_archivo)
        file_menu.add_command(label="Guardar Como", command=self.guardar_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        root.config(menu=menu_bar)

        # Área de texto principal (Input)
        # Label
        tk.Label(root, text="Código Fuente Ruby:", font=("Arial", 12, "bold")).pack(pady=5, anchor="w", padx=10)

        # Área de texto con scroll
        self.input_text = scrolledtext.ScrolledText(root, height=15, font=("Consolas", 10))
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=10)

        # Botón de "Analizar"
        self.analyze_button = tk.Button(root, text="ANALIZAR CÓDIGO",
                                        command=self.analizar_codigo,
                                        bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                                        height=2)
        self.analyze_button.pack(pady=10, fill=tk.X, padx=10)

        # Área de resultados/salida
        # Label
        tk.Label(root, text="Resultados del Análisis (Tokens y Errores):",
                 font=("Arial", 12, "bold")
                 ).pack(pady=5, anchor="w", padx=10)

        # Salida (solo lectura)
        self.output_text = scrolledtext.ScrolledText(root, height=15, state='disabled', bg="#f0f0f0",
                                                     font=("Consolas", 10))
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Métodos

    # Lógica de Archivos
    def cargar_archivo(self):
        filepath = filedialog.askopenfilename(filetypes=[("Archivos Ruby", "*.rb"), ("Todos los archivos", "*.*")])
        if filepath:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: \n {e}")

    def guardar_archivo(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".rb", filetypes=[("Archivos Ruby", "*.rb")])
        if filepath:
            try:
                content = self.input_text.get("1.0", tk.END)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    # Análisis de la Entrada
    def analizar_codigo(self):
        # Obtener el código del área de texto
        codigo = self.input_text.get("1.0", tk.END)

        # Habilitar escritura en el área de salida para mostrar resultados
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)  # Limpiar salida anterior

        # Reiniciar Analizadores
        lexer.lineno = 1
        lexer.errors = []

        parser.errors = []
        symbol_table.__init__()

        results = ""

        # Análisis Léxico
        results += "--- ANÁLISIS LÉXICO (LISTA DE TOKENS) ---\n"

        # Identificar Tokens
        lexer.input(codigo)
        while True:
            tok = lexer.token()
            if not tok:
                break
            results += f"Línea {tok.lineno}: {tok.type} -> {tok.value}\n"

        # Agregar Errores
        if lexer.errors:
            results += "\n--- ERRORES LÉXICOS ENCONTRADOS ---\n"
            for err in lexer.errors:
                results += f"[ERROR] {err}\n"
        else:
            results += "\n>> Análisis Léxico finalizado sin errores.\n"

        # Separador
        results += "\n" + "=" * 50 + "\n\n"

        # Análisis Sintáctico y Semántico

        # Reiniciar el lexer otra vez
        lexer.lineno = 1
        lexer.input(codigo)

        results += "--- ANÁLISIS SINTÁCTICO Y SEMÁNTICO ---\n"

        # Ejecutar el parser
        parser.parse(codigo, lexer=lexer)

        # Reportar Errores Sintácticos
        if parser.errors:
            results += "\n[ERRORES SINTÁCTICOS]:\n"
            for err in parser.errors:
                results += f"{err}\n"
        else:
            results += ">> Sintaxis Correcta.\n"

        # Reportar Errores Semánticos
        if symbol_table.errors:
            results += "\n[ERRORES SEMÁNTICOS]:\n"
            for err in symbol_table.errors:
                results += f"{err}\n"
        else:
            results += ">> Semántica Correcta (Lógica y Tipos).\n"

        # En caso de no encontrar errores...
        if not parser.errors and not symbol_table.errors:
            results += "\nEL CÓDIGO ES VÁLIDO."

        # Mostrar la salida y bloquear edición
        self.output_text.insert(tk.END, results)
        self.output_text.config(state='disabled')


# main
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()