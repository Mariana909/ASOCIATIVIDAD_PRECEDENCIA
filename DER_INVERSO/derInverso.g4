grammar derInverso;

programa: term EOF;

termino
    : expresion MUL term
    | expresion DIV term
    | expresion
    ;

expresion
    : factor SUM expresion
    | factor RES expresion
    | factor
    ;


factor
    : NUM
    | RES NUM
    ;

SUM: '+';
RES: '-';
MUL: '*';
DIV: '/';

NUM: DECIMAL | ENTERO;
DECIMAL: DIGITO+ '.' DIGITO+; 
ENTERO: DIGITO+;

fragment DIGITO: [0-9];

WS: [ \t]+ -> skip;