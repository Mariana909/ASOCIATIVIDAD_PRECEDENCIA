ACTIVIDAD ASOCIATIVIDAD Y PRECEDENCIA

REQUISITOS

COMANDOS

ACTIVIDAD
 
 Asociatividad y precedencia, realizando modificaciones a una gramática aritmética para hacer asociatividad por derecha, por izquierda, tener la precedencia de operadores definida matemáticamente y el orden inverso, realizar dos pruebas y comparar los resultados obtenidos con la misma cadena en cada una de las versiones de la gramática
SOLUCIÓN
   En antlr se tendrán 4 gramáticas, cada una con la modificación necesaria para asociatividad por derecha, asociatividad por izquierda, precedencia usual de operaciones y precedencia inversa.
   La gramática permite realizar operaciones como suma, resta, multiplicación y división entre números racionales. Admitiendo tanto enteros como números de punto flotante con signo.

NOMBRES DE ARCHIVOS Y SU ASOCIATIVIDAD Y PRECEDENCIA

PARA EJECUTAR

# Comparativa de Asociatividad y Precedencia

| Expresión | izqNormal | izqInverso | derNormal | derInverso |
|---|---|---|---|---|
| **Asociatividad** | Izquierda | Izquierda | Derecha | Derecha |
| **Precedencia `*/÷`** | Mayor | Menor | Mayor | Menor |
| `5+3` | 8 | 8 | 8 | 8 |
| `10-2*3` | 4 | 24 | 4 | 24 |
| `4*5+6` | 26 | 44 | 26 | 44 |
| `20/4` | 5 | 5 | 5 | 5 |
| `7+8*2-3` | 20 | -15 | 20 | -15 |
| `15-5-5` | 5 | 5 | 15 | 15 |
| `2*3*4` | 24 | 24 | 24 | 24 |
| `100/5/2` | 10 | 10 | 40 | 40 |
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
| `8-3-2-1` | 2 | 2 | 6 | 6 |
| `5*2*3/6` | 5 | 5 | 5.0 | 5.0 |
| `4+3*2-1*5+6/2` | 8 | 38.5 | 2 | 38.5 |
| `20/4*2-3+1` | 8 | 0 | -1.5 | -2.5 |
| `7*3-2*4+10/5` | 15 | 19.6 | 11 | 19.599... |
| `2+3*4+5*6-10/2` | 39 | -90 | 39 | -90 |
| `100/5/2*3+4-1` | 33 | 60 | 123 | 240 |
