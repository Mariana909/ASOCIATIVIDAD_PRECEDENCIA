# Actividad: Asociatividad y Precedencia

## Descripción

Actividad de asociatividad y precedencia, realizando modificaciones a una gramática aritmética para implementar asociatividad por derecha, por izquierda, precedencia de operadores definida matemáticamente y su orden inverso.

Se implementan cuatro versiones de la gramática, cada una con su propio parser generado por ANTLR4, visitor y main. La gramática permite realizar operaciones de suma, resta, multiplicación y división entre números racionales, admitiendo enteros y números de punto flotante con signo.

---

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
pip install -r requisitos.txt
```

---

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
  requisitos.txt
  README.md
```

---

## Versiones de la gramática

| Carpeta | Asociatividad | Precedencia `* /` |
|---|---|---|
| `IZQ_NORMAL` | Izquierda | Mayor (matemática usual) |
| `IZQ_INVERSO` | Izquierda | Menor (invertida) |
| `DER_NORMAL` | Derecha | Mayor (matemática usual) |
| `DER_INVERSO` | Derecha | Menor (invertida) |

### Resumen de reglas de evaluación

| Versión | `*/÷` tiene mayor precedencia que `+/-` | Se evalúa de izquierda a derecha |
|---|---|---|
| `izqNormal` | Sí | Sí |
| `izqInverso` | No | Sí |
| `derNormal` | Sí | No |
| `derInverso` | No | No |

---

## Compilar una gramática con ANTLR

Desde dentro de la carpeta `GRAMATICA/` correspondiente:

```bash
cd IZQ_NORMAL/GRAMATICA
antlr4 -Dlanguage=Python3 -visitor -no-listener izqNormal.g4
```

Repetir para cada versión reemplazando el nombre del archivo `.g4`.

### Visualizar el árbol sintáctico con `grun`

`grun` requiere compilar la gramática para Java. Desde la misma carpeta `GRAMATICA/`:

```bash
# 1. Generar archivos Java
antlr4 izqNormal.g4

# 2. Compilar
javac -cp .:/ruta/antlr-4.13.2-complete.jar *.java

# 3. Ver árbol en texto
grun izqNormal programa -tree

# 4. Ver árbol visual (abre ventana gráfica)
grun izqNormal programa -gui
```

Escribe la expresión, presiona Enter y luego `Ctrl+D`. Esto permite ver visualmente cómo la misma expresión se agrupa de forma distinta según la versión, lo que es útil para entender el efecto de la asociatividad y la precedencia.

---

## Ejecutar

Desde la raíz del proyecto, pasando la ruta al archivo de entrada:

```bash
python3 IZQ_NORMAL/main.py entrada.txt
python3 IZQ_INVERSO/main.py entrada.txt
python3 DER_NORMAL/main.py entrada.txt
python3 DER_INVERSO/main.py entrada.txt
```

El archivo de entrada debe contener una expresión aritmética por línea. Las líneas vacías se ignoran.

### Ejemplo de `entrada.txt`

```
5+3
10-2*3
15-5-5
100/5/2
```

---

## Análisis de resultados

### Tabla comparativa completa

| Expresión | izqNormal | izqInverso | derNormal | derInverso |
|---|---|---|---|---|
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
| `7*3-2*4+10/5` | 15 | 19.6 | 11 | 19.599... |
| `2+3*4+5*6-10/2` | 39 | -90 | 39 | -90 |
| `100/5/2*3+4-1` | 33 | 60 | 123 | 240 |

---

### Efecto de la asociatividad

La asociatividad solo produce diferencias con operadores **no conmutativos** como `-` y `/`. Con `+` y `*` el resultado es el mismo independientemente del lado de agrupación.

| Expresión | Izquierda | Derecha | Agrupación izquierda | Agrupación derecha |
|---|---|---|---|---|
| `15-5-5` | 5 | 15 | `(15-5)-5 = 5` | `15-(5-5) = 15` |
| `100/5/2` | 10 | 40 | `(100/5)/2 = 10` | `100/(5/2) = 40` |
| `8-3-2-1` | 2 | 6 | `((8-3)-2)-1 = 2` | `8-(3-(2-1)) = 6` |

> **Nota:** expresiones como `2*3*4` o `-5+3` producen el mismo resultado en ambas asociatividades porque la multiplicación y la suma son conmutativas y asociativas en los reales.

---

### Efecto de la precedencia

La precedencia define qué operador "liga más fuerte" cuando se mezclan operadores distintos en una expresión. En la precedencia normal `*/÷` tiene mayor prioridad que `+/-`; en la invertida ocurre lo contrario.

| Expresión | Normal | Invertida | Agrupación normal | Agrupación invertida |
|---|---|---|---|---|
| `10-2*3` | 4 | 24 | `10-(2*3) = 4` | `(10-2)*3 = 24` |
| `4*5+6` | 26 | 44 | `(4*5)+6 = 26` | `4*(5+6) = 44` |
| `7+8*2-3` | 20 | -15 | `7+(8*2)-3 = 20` | `(7+8)*(2-3) = -15` |

---

### Árboles sintácticos — `100/2/5+3*2`

Esta expresión produce cuatro resultados distintos (16, 12.5, 256, 800), lo que la hace ideal para visualizar el efecto combinado de asociatividad y precedencia.

Para generar los árboles con `grun`, desde cada carpeta `GRAMATICA/`:

```bash
antlr4 <gramatica>.g4
javac -cp .:/ruta/antlr-4.13.2-complete.jar *.java
grun <gramatica> programa -gui
# Escribir: 100/2/5+3*2
# Presionar Ctrl+D
```

#### izqNormal — resultado: 16

`*/÷` tiene mayor precedencia y se agrupa por la izquierda:

```
((100/2)/5) + (3*2)
    50  / 5  +   6
       10    +   6  = 16
```

#### izqInverso — resultado: 12.5

`+/-` tiene mayor precedencia y se agrupa por la izquierda. El `+` entre `5` y `3` se resuelve primero:

```
(100/2) / (5+3) * 2
  50    /   8   * 2
       6.25    * 2   = 12.5
```

#### derNormal — resultado: 256

`*/÷` tiene mayor precedencia pero se agrupa por la derecha:

```
100 / (2/5) + (3*2)
100 /  0.4  +   6
    250     +   6   = 256
```

#### derInverso — resultado: 800

`+/-` tiene mayor precedencia y se agrupa por la derecha. El `+` entre `5` y `3` se resuelve primero, y la asociatividad derecha afecta toda la cadena de `*/÷`:

```
100 / (2 / (5+3) * 2)
100 / (2 /  8   * 2)
100 / (0.25     * 2)
100 /      0.125      = 800
```

> **Espacio para capturas:** una vez generados los árboles con `grun -gui`, agregar aquí las capturas de pantalla de cada versión para complementar el análisis textual.

-- izqNormal: <img width="376" height="414" alt="antlr4_parse_tree" src="https://github.com/user-attachments/assets/2c5100bf-9504-425d-b769-9bd0162b76ee" />
 --
-- izqInverso: <img width="387" height="399" alt="antlr4_parse_tree" src="https://github.com/user-attachments/assets/dad1f400-4d29-44fc-ae2e-56d4f929aac5" />
 --
-- derNormal:  <img width="442" height="481" alt="antlr4_parse_tree" src="https://github.com/user-attachments/assets/d114924c-e134-465d-96ca-5bc58ebd2c5b" />
 --
-- derInverso: <img width="508" height="548" alt="antlr4_parse_tree" src="https://github.com/user-attachments/assets/fc526b1c-616a-4da5-9ae9-54b0261b2734" />
 --

---

### Casos donde todas las versiones coinciden

Cuando una expresión contiene un solo operador o solo operadores del mismo nivel de precedencia entre números positivos, las cuatro versiones producen el mismo resultado:

| Expresión | Razón de la coincidencia |
|---|---|
| `5+3` | Un solo operador, sin ambigüedad |
| `20/4` | Un solo operador, sin ambigüedad |
| `-5+3` | Un solo operador (el `-` inicial es signo, no resta) |
| `-8*-2` | Un solo operador entre dos términos con signo |
| `2*3*4` | Solo `*`, que es conmutativo y asociativo |
| `3.5+2.1` | Solo `+`, conmutativo y asociativo |

---

### Casos límite

- **División por cero:** el visitor lanza `ZeroDivisionError` explícitamente antes de intentar la operación.
- **Números negativos consecutivos** (`6*-2`, `-8*-2`): el signo negativo es parte del `term` en la gramática (`RES NUM`), no un operador binario, por lo que se maneja correctamente en todas las versiones.
- **Punto flotante** (`9/2 = 4.5`): el visitor devuelve `int` cuando el resultado de una división es entero y `float` cuando no lo es, para evitar resultados como `4` donde se esperaría `4.5`.
