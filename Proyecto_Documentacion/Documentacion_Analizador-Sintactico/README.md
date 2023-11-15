<div align="center">
<br>
<br>
<p align="center">
  <img src="img/CaratulaAS.jpg" alt="Bob" width="3000"/>
</p>
<br>
<br>
</div>

# Analizador-Sintactico

## 1. Introducción

Documentación de proyecto, una implementación de un analizador sintáctico en Python utilizando PLY (Python Lex-Yacc). Este proyecto tiene como objetivo principal proporcionar una herramienta educativa para el aprendizaje académico del funcionamiento interno de los analizadores sintácticos y cómo se pueden implementar en el contexto de compiladores

## Objetivos del Aprendizaje
- Proporcionar una implementación educativa de un analizador sintáctico utilizando PLY
- Facilitar la comprensión de los principios teóricos detrás de los analizadores sintácticos y la generación de código
- Ofrecer ejemplos prácticos que ilustren funcina un analizador sintáctico en un compilador

## Implementación en un Compilador
La capacidad de integrar un analizador sintáctico en un compilador es una competencia clave para aquellos que buscan desarrollar software que traduzca código fuente a código ejecutable. A lo largo de esta documentación, exploraremos cómo puede integrarse este analizador sintáctico en un contexto más amplio de compilación, proporcionando ejemplos y pautas para facilitar la comprensión práctica

## Breve Descripción de PLY y Propósito
PLY (Python Lex-Yacc) es una herramienta que combina la funcionalidad de Lex (analizador léxico) y Yacc (analizador sintáctico) en el entorno de programación Python. Su propósito es facilitar la creación de analizadores léxicos y sintácticos para procesar lenguajes formales. En este proyecto, utilizamos PLY para construir un analizador sintáctico que pueda ser educativo y aplicado en el desarrollo de compiladores

## 2. Instalación
Para comenzar a utilizar nuestro analizador sintáctico basado en PLY, sigue estos pasos de instalación:

1. **Instala Python:**
   Asegúrate de tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde [el sitio oficial de Python](https://www.python.org/downloads/).

2. **Instala PLY:**
   Puedes instalar PLY utilizando el administrador de paquetes de Python, pip. Abre una terminal o línea de comandos y ejecuta el siguiente comando:
   ```bash
   pip install ply

## 3. Uso básico
Ejemplos sencillos de cómo usar tu analizador sintáctico. Puedes incluir fragmentos de código y explicaciones paso a paso.

## 4. Estructura del código
### 4.1 Definición de Precedencia
Esta sección establece cómo se deben interpretar y evaluar las expresiones en términos de la precedencia de los operadores, lo cual es crucial para garantizar que las expresiones se analicen correctamente y sigan la lógica esperada
  ```python
# Definición de precedencia y reglas de producción
precedence = (
    # Definir precedencia de operadores
    ('left', 'SUMA', 'MENOS'),
    ('left', 'MULTIPLICACION', 'ENTRE'),
    ('right', 'UMINUS'),
    ('left', 'MENOR_QUE', 'MAYOR_QUE', 'MENOR_O_IGUAL_QUE', 'MAYOR_O_IGUAL_QUE', 'DIFERENTE_DE', 'IGUAL_A'),
)
```
* La sección define la precedencia de los operadores en tu lenguaje. Esto es crucial para resolver ambigüedades en la gramática y determinar el orden de evaluación de los operadores. La notación ('left', ...) indica asociatividad de izquierda para los operadores listados, mientras que ('right', ...) indica asociatividad de derecha
* se ha definido la precedencia para operadores aritméticos (SUMA, MENOS, MULTIPLICACION, ENTRE), el operador unario negativo (UMINUS), y operadores de comparación (MENOR_QUE, MAYOR_QUE, MENOR_O_IGUAL_QUE, MAYOR_O_IGUAL_QUE, DIFERENTE_DE, IGUAL_A).

### 4.2 Reglas de producción
El bloque de código que comienza con def p_programa(p): y continúa con varias funciones que comienzan con p_ se refiere a las reglas de producción de tu analizador sintáctico utilizando PLY

```python
def p_programa(p):
    'programa : declaraciones'
```
* Esta regla establece que un programa (programa) está compuesto por una secuencia de declaraciones (declaraciones). La parte entre comillas simples ('programa : declaraciones') es la definición de la regla en términos de la gramática del lenguaje
```python
# Reglas de producción
def p_programa(p):
    'programa : declaraciones'
def p_declaraciones(p):
    'declaraciones : declaracion SALTO_DE_LINEA'
def p_declaracion(p):
    '''declaracion : declaracion_variable
                   | declaracion_funcion'''
def p_declaracion_variable(p):
    'declaracion_variable : tipo VARIABLE DELIMITADOR'
def p_tipo(p):
    '''tipo : ENTERO
            | BULEANO
            | FLOTANTE'''
# Resto de las reglas de producción...
```

## 5. Gramática
La gramática utilizada en el analizador sintáctico PLY de este proyecto se presenta a continuación. Estas reglas de producción describen la estructura sintáctica del lenguaje que el analizador es capaz de reconocer

1. Un programa está compuesto por declaraciones
  - **programa** -> declaraciones
2. Las declaraciones pueden ser una declaración seguida de un salto de línea
  -  **declaraciones** -> declaracion SALTO_DE_LINEA
3. Una declaración puede ser una declaración de variable o una declaración de función
  -  **declaracion** -> declaracion_variable | declaracion_funcion
4. Una declaración de variable comienza con un tipo seguido de un nombre de variable y termina con un delimitador
  -  **declaracion_variable** -> tipo VARIABLE DELIMITADOR
5. El tipo de variable puede ser ENTERO, BULEANO o FLOTANTE
  -  **tipo** -> ENTERO | BULEANO | FLOTANTE
6. Una declaración de función comienza con la palabra clave FUNCION, seguida de paréntesis que contienen parámetros, un bloque de función y termina con un delimitador
  -  **declaracion_funcion** -> FUNCION PARENTESIS_IZQ parametros PARENTESIS_DER bloque_funcion DELIMITADOR
7. Los parámetros de una función pueden ser nulos (ε) o una lista de variables separadas por comas
  -  **parametros** -> ε | parametros VARIABLE | parametros VARIABLE parametros
8. Un bloque de función está contenido entre paréntesis y contiene expresiones
  -  **bloque_funcion** -> PARENTESIS_IZQ expresiones PARENTESIS_DER
9. Las expresiones pueden ser una sola expresión o una secuencia de expresiones
  -  **expresiones** -> expresion | expresiones expresion
10. Aquí se detallan las reglas para diversas operaciones y elementos que pueden formar una expresión, incluyendo operadores aritméticos, comparativos, variables, números, cadenas y construcciones como condicionales y bucles
  - **expresion** -> expresion SUMA expresion | expresion MULTIPLICACION expresion | expresion MENOS expresion | expresion ENTRE expresion | expresion MENOR_QUE expresion | expresion MAYOR_QUE expresion | expresion MENOR_O_IGUAL_QUE expresion | expresion MAYOR_O_IGUAL_QUE expresion | expresion DIFERENTE_DE expresion | expresion IGUAL_A expresion | VARIABLE | NUMERO | CADENA | condicional | bucle_mientras | bucle_para | expresion_unaria | expresion_parentesis
11. Los argumentos de una función pueden ser nulos (ε) o una lista de expresiones separadas por comas
  -  **argumentos** -> ε | argumentos expresion | argumentos expresion argumentos
12. Una construcción condicional tiene la forma "SI expresion ENTONCES bloque_funcion"
  -  **condicional** -> SI expresion ENTONCES bloque_funcion
13. Un bucle mientras tiene la forma "MIENTRAS expresion ENTONCES bloque_funcion"
  -  **bucle_mientras** -> MIENTRAS expresion ENTONCES bloque_funcion
14. Un bucle para tiene la forma "PARA expresion ENTONCES bloque_funcion"
  -  **bucle_para** -> PARA expresion ENTONCES bloque_funcion
15. Una expresión unaria tiene la forma "MENOS expresion" y tiene mayor precedencia (%prec UMINUS)
  -  **expresion_unaria** -> MENOS expresion %prec UMINUS
16. Una expresión entre paréntesis tiene la forma "PARENTESIS_IZQ expresion PARENTESIS_DER"
  -  **expresion_parentesis** -> PARENTESIS_IZQ expresion PARENTESIS_DER

## 6. Detalles técnicos
### 6.1 Yacc (Yet Another Compiler Compiler)
Yacc es una herramienta de generación de analizadores sintácticos (parsers) que se utiliza comúnmente en la construcción de compiladores y analizadores para lenguajes de programación. Fue desarrollado como parte del sistema Unix y es parte del conjunto de herramientas conocido como "Lex and Yacc" (o "Flex and Bison" en sus versiones más modernas).

* Definición de la Gramática: En el contexto de Yacc, la gramática se define mediante reglas de producción. Estas reglas describen la estructura sintáctica del lenguaje que se está analizando.

* Especificación de Acciones Semánticas: Junto con las reglas de producción, se especifican acciones semánticas en forma de código en algún lenguaje de programación (como C o Python). Estas acciones se ejecutan cuando se encuentra una coincidencia con una regla de producción específica.

* Generación del Analizador Sintáctico: Yacc utiliza la gramática y las acciones semánticas para generar un analizador sintáctico en el lenguaje de programación elegido. Este analizador es capaz de analizar secuencias de tokens y construir una estructura de árbol sintáctico que representa la estructura del programa fuente.

* Integración con el Analizador Léxico (Lex): Comúnmente, Yacc se utiliza junto con Lex (o herramientas similares) para construir un analizador léxico que proporciona los tokens al analizador sintáctico.

## 7. Ejemplos avanzados
Proporciona ejemplos más complejos de uso. Muestra cómo manejar casos especiales o construcciones sintácticas más avanzadas.

## 8. Errores y manejo de excepciones
El bloque de código que comienza con def p_error(p): se refiere a la gestión de errores en tu analizador sintáctico. Esta función se llama automáticamente por PLY cuando ocurre un error sintáctico durante el análisis del código fuente

```python
# Manejo de errores
def p_error(p):
    print(f"Error de sintaxis en el token: {p}")
```
* **def p_error(p)**: Esta línea define la función *p_error* que se activa cuando se encuentra un error sintáctico.
* **print(f"Error de sintaxis en el token: {p}")**: Cuando se llama a esta función, imprime un mensaje de error indicando que se encontró un error de sintaxis y muestra información sobre el token *(p)* que causó el error. Esta información puede incluir detalles como el tipo de token y su valor

## 10. Referencias
[1](https://www.dabeaz.com/ply/ply.html)D. Beazley, "PLY (Python Lex-Yacc)," [En línea]. Disponible en: https://www.dabeaz.com/ply/ply.html
