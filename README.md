# Actividad: Asociatividad y Precedencia

## Descripción

Actividad de asociatividad y precedencia, realizando modificaciones a una gramática aritmética para implementar asociatividad por derecha, por izquierda, precedencia de operadores definida matemáticamente y su orden inverso.

Se implementan cuatro versiones de la gramática, cada una con su propio parser generado por ANTLR4, visitor y main. La gramática permite realizar operaciones de suma, resta, multiplicación y división entre números racionales, admitiendo enteros y números de punto flotante con signo.

## Requisitos previos

- Python 3.8 o superior
- Java Runtime (requerido por ANTLR)
- antlr4-tools
- antlr4-python3-runtime

### Instalación de dependencias

```bash
# Java
sudo apt install default-jre

# antlr4
pip3 install --user antlr4-tools
pip3 install antlr4-python3-runtime
```

Si `antlr4` no queda disponible en el PATH:
```bash
pipx install antlr4-tools
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Entorno virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime
```

## Estructura del proyecto

```
ASOCIATIVIDAD_PRECEDENCIA/
  IZQ_NORMAL/
    GRAMATICA/
      izqNormal.g4
      izqNormalLexer.py       # Generado por ANTLR — no editar
      izqNormalParser.py      # Generado por ANTLR — no editar
      izqNormalVisitor.py     # Generado por ANTLR — no editar
    main.py
    visitorIN.py
  IZQ_INVERSO/
    GRAMATICA/
      izqInverso.g4
      izqInversoLexer.py
      izqInversoParser.py
      izqInversoVisitor.py
    main.py
    visitorII.py
  DER_NORMAL/
    GRAMATICA/
      derNormal.g4
      derNormalLexer.py
      derNormalParser.py
      derNormalVisitor.py
    main.py
    visitorDN.py
  DER_INVERSO/
    GRAMATICA/
      derInverso.g4
      derInversoLexer.py
      derInversoParser.py
      derInversoVisitor.py
    main.py
    visitorDI.py
  entrada.txt
```

## Versiones de la gramática

| Carpeta | Asociatividad | Precedencia `* /` |
|---|---|---|
| `IZQ_NORMAL` | Izquierda | Mayor (matemática usual) |
| `IZQ_INVERSO` | Izquierda | Menor (invertida) |
| `DER_NORMAL` | Derecha | Mayor (matemática usual) |
| `DER_INVERSO` | Derecha | Menor (invertida) |

## Compilar una gramática con ANTLR

Desde dentro de la carpeta `GRAMATICA/` correspondiente:

```bash
cd IZQ_NORMAL/GRAMATICA
antlr4 -Dlanguage=Python3 -visitor -no-listener izqNormal.g4
```

Repetir para cada versión reemplazando el nombre del archivo `.g4`.

## Ejecutar

Desde dentro de la carpeta de cada versión, pasando la ruta al archivo de entrada:

```bash
cd IZQ_NORMAL
python3 main.py "/ruta/a/entrada.txt"
```

El archivo de entrada debe contener una expresión aritmética por línea. Las líneas vacías se ignoran.

### Ejemplo de `entrada.txt`

```
5+3
10-2*3
15-5-5
100/5/2
```

## Comparativa de resultados

La misma expresión evaluada en las cuatro versiones produce resultados distintos según la asociatividad y la precedencia aplicadas.

| Expresión | izqNormal | izqInverso | derNormal | derInverso |
|---|---|---|---|---|
| **Asociatividad** | Izquierda | Izquierda | Derecha | Derecha |
| **Precedencia `*/÷`** | Mayor | Menor | Mayor | Menor |
| `5+3` | 8 | 8 | 8 | 8 |
| `10-2*3` | 4 | 24 | 4 | 24 |
| `4*5+6` | 26 | 44 | 26 | 44 |
| `20/4` | 5 | 5 | 5 | 5 |
| `7+8*2-3` | 20 | -15 | 20 | -15 |
| `15-5-5` | 5 | 5 | **15** | **15** |
| `2*3*4` | 24 | 24 | 24 | 24 |
| `100/5/2` | 10 | 10 | **40** | **40** |
| `-5+3` | -2 | -2 | -2 | -2 |
| `6*-2` | -12 | -12 | -12 | -12 |
| `-8*-2` | 16 | 16 | 16 | 16 |
| `3.5+2.1` | 5.6 | 5.6 | 5.6 | 5.6 |
| `10.0-3*2` | 4.0 | 14.0 | 4.0 | 14.0 |
| `5*2.5` | 12.5 | 12.5 | 12.5 | 12.5 |
| `9/2` | 4.5 | 4.5 | 4.5 | 4.5 |
| `2+3*4-5/5` | 13 | -1 | 13 | -1.0 |
| `10-2*3+4/2` | 6 | 28 | 2 | 28.0 |
| `3*4+2*5-10/2` | 17 | -45 | 17 | -45.0 |
| `1+2+3*4*5` | 63 | 120 | 63 | 120 |
| `100/2/5+3*2` | 16 | 12.5 | 256 | 800 |
| `-3*4+2*-5` | -22 | 90 | -22 | 90 |
| `2.5*4+3.5*2` | 17.0 | 37.5 | 17.0 | 37.5 |
| `10/2/5+1` | 2 | 0.833... | 26 | 30 |
| `8-3-2-1` | 2 | 2 | **6** | **6** |
| `5*2*3/6` | 5 | 5 | 5.0 | 5.0 |
| `4+3*2-1*5+6/2` | 8 | 38.5 | 2 | 38.5 |
| `20/4*2-3+1` | 8 | 0 | -1.5 | -2.5 |
| `7*3-2*4+10/5` | 15 | 19.6 | 11 | 19.6 |
| `2+3*4+5*6-10/2` | 39 | -90 | 39 | -90 |
| `100/5/2*3+4-1` | 33 | 60 | 123 | 240 |

### Casos más representativos

**Asociatividad** — visible con operadores no conmutativos como `-` y `/`:

| Expresión | Izquierda | Derecha | Agrupación izq | Agrupación der |
|---|---|---|---|---|
| `15-5-5` | 5 | 15 | `(15-5)-5` | `15-(5-5)` |
| `100/5/2` | 10 | 40 | `(100/5)/2` | `100/(5/2)` |
| `8-3-2-1` | 2 | 6 | `((8-3)-2)-1` | `8-(3-(2-1))` |

**Precedencia** — visible cuando se mezclan `+/-` con `*/÷`:

| Expresión | Normal | Inversa | Interpretación normal | Interpretación inversa |
|---|---|---|---|---|
| `10-2*3` | 4 | 24 | `10-(2*3)` | `(10-2)*3` |
| `4*5+6` | 26 | 44 | `(4*5)+6` | `4*(5+6)` |
| `7+8*2-3` | 20 | -15 | `7+(8*2)-3` | `(7+8)*(2-3)` |
