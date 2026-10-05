# Hello World con PLY (Python Lex-Yacc)

Ejemplo sencillo de un analizador léxico y sintáctico hecho con [PLY](https://www.dabeaz.com/ply/).
Reconoce frases como `hello mundo` y muestra cada etapa del análisis.

## Requisitos

- Python 3
- PLY:

```bash
pip install ply
```

## Cómo correrlo

```bash
python hello.py
```

## Cómo funciona

El programa tiene tres partes:

1. **Lexer** (`ply.lex`): parte el texto en tokens.
   - `HELLO` → la palabra `hello`
   - `ID` → cualquier palabra en minúsculas
2. **Parser** (`ply.yacc`): revisa que los tokens sigan la regla de la gramática:
   ```
   saludo : HELLO ID
   ```
3. **Árbol**: si la frase es válida, construye el árbol y muestra el resultado.

## Ejemplo de salida

```
Texto: 'hello mundo'

[1] Análisis léxico (tokens):
  HELLO  'hello'    posición 0
  ID     'mundo'    posición 6

[2] Análisis sintáctico:
  Regla aplicada: saludo -> HELLO ID   (HELLO='hello', ID='mundo')

[3] Árbol:
  saludo
  ├── HELLO: hello
  └── ID: mundo

Resultado: Hola, mundo!
```

Si la frase no sigue la regla (por ejemplo, solo `hello`), el parser marca un error de sintaxis
y no construye el árbol.

## Probar otras frases

Agrega líneas al final de `hello.py`:

```python
analizar("hello profe")
```
