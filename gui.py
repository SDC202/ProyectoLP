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

        # Crear Frame contenedor para el código, los números Y la barra de scroll
        code_frame = tk.Frame(root)
        code_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        # Barra de Scroll Vertical (¡Nueva!)
        scrollbar = tk.Scrollbar(code_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Área de texto para los números de línea (sin cambios)
        self.linenumbers = tk.Text(code_frame, width=4, padx=5, bd=0,
                                   bg="#f0f0f0", state='disabled',
                                   font=("Consolas", 10))
        self.linenumbers.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto con scroll (Input)
        self.input_text = tk.Text(code_frame, height=15, font=("Consolas", 10))
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Conexión de la barra de scroll a ambos widgets (llama a yview_sync)
        scrollbar.config(command=self.yview_sync)
        self.input_text.config(yscrollcommand=scrollbar.set)
        self.linenumbers.config(yscrollcommand=scrollbar.set)

        # Enlaces de eventos para la actualización de números (¡Windows OK!)
        self.input_text.bind('<KeyRelease>', self.update_line_numbers)
        self.input_text.bind('<MouseWheel>', self.update_line_numbers)

        # 5. Llamar a la actualización inicial
        self.update_line_numbers()

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
    def yview_sync(self, *args):
        """Método llamado por la barra de scroll para mover ambos widgets."""

        # La barra de scroll pasa argumentos válidos ('moveto', '0.0', etc.)
        self.input_text.yview(*args)
        self.linenumbers.yview(*args)

        # Llamar al generador de números después del scroll
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        # 1. Deshabilitar y Limpiar
        self.linenumbers.config(state='normal')
        self.linenumbers.delete("1.0", tk.END)

        # 2. Generar Números
        # Obtener el número total de líneas de código (usando 'end-1c' para evitar línea vacía final)
        total_lines = int(self.input_text.index('end-1c').split('.')[0])

        line_num_string = ""
        # Generar la cadena de números (padding opcional para alineación)
        for i in range(1, total_lines + 1):
            line_num_string += f"{i}\n"

        self.linenumbers.insert("1.0", line_num_string)

        # 3. SINCRONIZACIÓN VERTICAL (¡El paso clave!)
        # Obtener la fracción de desplazamiento actual del área de código.
        # yview() devuelve una tupla (fracción_superior, fracción_inferior), queremos el primer elemento.
        scroll_fraction = self.input_text.yview()[0]

        # Mover el widget de números a esa misma fracción de desplazamiento.
        self.linenumbers.yview_moveto(scroll_fraction)

        # 4. Volver a deshabilitar
        self.linenumbers.config(state='disabled')

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