# ProyectoLP
Proyecto de la materia de Lenguajes de Programación por Sebastian² en la carrera de Computación de la ESPOL.


# Implementación de un Analizador Léxico, Sintáctico y Semántico para Ruby
## Proyecto de Lenguajes de Programación

[cite_start]Este repositorio contiene el desarrollo de un analizador completo para un subconjunto del lenguaje de programación **Ruby**, como parte del proyecto de la materia Lenguajes de Programación[cite: 90, 94]. [cite_start]El objetivo es aplicar los conceptos teóricos de la compilación para construir una herramienta capaz de procesar y validar código fuente en Ruby[cite: 101].

[cite_start]El analizador está construido en **Python 3** y utiliza la biblioteca **PLY (Python Lex-Yacc)**[cite: 98, 203].

---

### [cite_start]🧑‍💻 Integrantes (Grupo 11) [cite: 91]

* [cite_start]**Sebastián Manzanilla** - `[ManzanillaSebastian]` [cite: 92]
* [cite_start]**Sebastián De Castro** - `[SDC202]` [cite: 92]

---

### 🎯 Objetivos del Proyecto

1.  [cite_start]**Analizador Léxico:** Identificar y clasificar correctamente los componentes (tokens) de Ruby, como palabras reservadas, identificadores, operadores y literales[cite: 109].
2.  [cite_start]**Analizador Sintáctico:** Validar la estructura gramatical del código (declaraciones, expresiones, estructuras de control) usando las reglas de PLY[cite: 110].
3.  [cite_start]**Analizador Semántico:** Verificar la coherencia lógica, como la declaración de variables, la compatibilidad de tipos y el alcance (scope)[cite: 111].
4.  [cite_start]**GUI:** Proveer una interfaz gráfica de usuario para probar el analizador de forma interactiva[cite: 105, 207].

---

### 🛠️ Herramientas y Tecnologías

* [cite_start]**Lenguaje Base:** Python 3.x [cite: 203]
* [cite_start]**Analizador:** PLY (Python Lex-Yacc) [cite: 203]
* [cite_start]**Interfaz Gráfica (GUI):** Tkinter / PyQt [cite: 203]
* [cite_start]**Control de Versiones:** Git y GitHub [cite: 203]

---

### 📂 Estructura del Repositorio

/ProyectoLP/ │ ├── analizador_lexico.py # Definición de tokens y reglas léxicas (Avance 1) ├── analizador_sintactico.py # Definición de la gramática (Avance 2) ├── analizador_semantico.py # Reglas semánticas (Avance 3) │ ├── gui.py # Archivo principal para ejecutar la interfaz gráfica ├── probar_lexer.py # Script para generar logs léxicos │ ├── /algoritmos_prueba/ │ ├── prueba_sManzanilla.rb # Algoritmo de prueba para Sebastián M. │ └── prueba_sDeCastro.rb # Algoritmo de prueba para Sebastián D. │ ├── /logs/ │ └── (Aquí se guardan los logs generados en formato .txt) │ └── README.md # Documentación del repositorio


---

### 🚀 Cómo Ejecutar

1.  **Clonar el repositorio:**
    ```bash
    git clone [URL-DE-TU-REPOSITORIO]
    cd ProyectoLP
    ```

2.  **Instalar dependencias:**
    El proyecto requiere la biblioteca `PLY`.
    ```bash
    pip install ply
    ```
    *(Si se usa PyQt, también se necesitará `pip install PyQt5`)*

3.  **Ejecutar el Analizador:**
    Para lanzar la interfaz gráfica principal:
    ```bash
    python gui.py
    ```

4.  **Probar el Lexer (Avance 1):**
    Para generar un log de prueba desde la terminal:
    ```bash
    python probar_lexer.py algoritmos_prueba/tu_archivo.rb tu_usuario_git
    ```