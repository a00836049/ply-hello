# Hello World con PLY (Python Lex-Yacc)
# Reconoce frases como:  hello mundo
import ply.lex as lex
import ply.yacc as yacc

# ---------- 1. LEXER: parte el texto en tokens ----------

tokens = ("HELLO", "ID")

def t_HELLO(t):
    r"hello"
    return t

t_ID = r"[a-z]+"     # una palabra en minúsculas
t_ignore = " \t"     # ignora espacios y tabs

def t_error(t):
    print(f"  Caracter no válido: {t.value[0]!r}")
    t.lexer.skip(1)

# ---------- 2. PARSER: revisa que los tokens sigan la regla ----------

def p_saludo(p):
    "saludo : HELLO ID"
    print(f"  Regla aplicada: saludo -> HELLO ID   (HELLO={p[1]!r}, ID={p[2]!r})")
    p[0] = ("saludo", ("HELLO", p[1]), ("ID", p[2]))   # el árbol

def p_error(p):
    print(f"  Error de sintaxis en: {p.value!r}" if p else "  Error: faltan tokens")

# ---------- 3. PROBARLO ----------

lexer = lex.lex()
parser = yacc.yacc(debug=False, write_tables=False)

def analizar(texto):
    print(f"\nTexto: {texto!r}")

    print("\n[1] Análisis léxico (tokens):")
    lexer.input(texto)
    for tok in lexer:
        print(f"  {tok.type:<6} {tok.value!r:<10} posición {tok.lexpos}")

    print("\n[2] Análisis sintáctico:")
    arbol = parser.parse(texto, lexer=lexer)

    print("\n[3] Árbol:")
    if arbol:
        _, hello, nombre = arbol
        print("  saludo")
        print(f"  ├── {hello[0]}: {hello[1]}")
        print(f"  └── {nombre[0]}: {nombre[1]}")
        print(f"\nResultado: Hola, {nombre[1]}!")
    else:
        print("  (no se pudo construir)")

analizar("hello mundo")
analizar("hello")          # ejemplo con error
