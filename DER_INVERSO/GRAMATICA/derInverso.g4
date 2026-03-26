grammar derInverso;

programa: expresion EOF;

expresion
    : factor MUL expresion
    | factor DIV expresion
    | factor
    ;

factor
    : term SUM factor
    | term RES factor
    | term
    ;

term
    : NUM
    | RES NUM
    ;

SUM: '+'; RES: '-'; MUL: '*'; DIV: '/';
NUM: DECIMAL | ENTERO;
DECIMAL: DIGITO+ '.' DIGITO+;
ENTERO: DIGITO+;
fragment DIGITO: [0-9];
WS: [ \t]+ -> skip;
