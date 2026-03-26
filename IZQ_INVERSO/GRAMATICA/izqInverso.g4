grammar izqInverso;

programa: expresion EOF;

expresion
    : expresion MUL factor
    | expresion DIV factor
    | factor
    ;

factor
    : factor SUM term
    | factor RES term
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