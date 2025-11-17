# Implementación de un Analizador Léxico, Sintáctico y Semántico para Ruby
## Proyecto de Lenguajes de Programación

Este repositorio contiene el desarrollo de un analizador completo para un subconjunto del lenguaje de programación **Ruby**, como parte del proyecto de la materia Lenguajes de Programación. El objetivo es aplicar los conceptos teóricos de la compilación para construir una herramienta capaz de procesar y validar código fuente en Ruby.

El analizador está construido en **Python 3** y utiliza la biblioteca **PLY (Python Lex-Yacc)**.

---

### 🧑‍💻 Integrantes (Grupo 11)

* **Sebastián Manzanilla** - `[ManzanillaSebastian]`
* **Sebastián De Castro** - `[SDC202]`

---

### 🎯 Objetivos del Proyecto

1.  **Analizador Léxico:** Identificar y clasificar correctamente los componentes (tokens) de Ruby, como palabras reservadas, identificadores, operadores y literales.
2.  **Analizador Sintáctico:** Validar la estructura gramatical del código (declaraciones, expresiones, estructuras de control) usando las reglas de PLY.
3.  **Analizador Semántico:** Verificar la coherencia lógica, como la declaración de variables, la compatibilidad de tipos y el alcance (scope).
4.  **GUI:** Proveer una interfaz gráfica de usuario para probar el analizador de forma interactiva.

---

### 🛠️ Herramientas y Tecnologías

* **Lenguaje Base:** Python 3.x
* **Analizador:** PLY (Python Lex-Yacc)
* **Interfaz Gráfica (GUI):** Tkinter / PyQt
* **Control de Versiones:** Git y GitHub

---

### 📂 Estructura del Repositorio

```
/ProyectoLP/
├── analizador_lexico.py    # Definición de tokens y reglas léxicas (Avance 1)
├── analizador_sintactico.py # Definición de la gramática (Avance 2) y reglas semánticas (Avance 3)
├── gui.py                  # Archivo principal para ejecutar la interfaz gráfica
├── probar_lexer.py         # Script para generar logs léxicos
├── probar_sintactico.py    # Script para probar el parser (Avance 2)
├── probar_semantico.py    # Script para probar el parser (Avance 3)
├── algoritmos_prueba/
│   ├── pruebalexer_sManzanilla.rb # Algoritmo de prueba para Sebastián M.
│   ├── pruebalexer_sDeCastro.rb   # Algoritmo de prueba para Sebastián D. C.
│   ├── pruebaparser_sManzanilla.rb # Algoritmo de prueba para Sebastián M.
│   ├── pruebaparser_sDeCastro.rb   # Algoritmo de prueba para Sebastián D. C.
│   ├── pruebasemantico_sManzanilla.rb # Algoritmo de prueba para Sebastián M.
│   └── pruebasemantico_sDeCastro.rb   # Algoritmo de prueba para Sebastián D. C.
├── logs/
│   └── (Aquí se guardan los logs generados en formato .txt)
└── README.md               # Documentación del repositorio
```

---

### 🚀 Cómo Ejecutar

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/SDC202/ProyectoLP.git
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

4.  **Probar los Avances (Terminal):**
    * **Avance 1 (Lexer):**
        ```bash
        python probar_lexer.py algoritmos_prueba/tu_archivo.rb tu_usuario_git
        ```
    * **Avance 2 (Parser):**
        ```bash
        python probar_sintactico.py algoritmos_prueba/tu_archivo.rb tu_usuario_git
        ```
    * **Avance 3 (Parser Semantico):**
        ```bash
        python probar_semantico.py algoritmos_prueba/tu_archivo.rb tu_usuario_git
        ```