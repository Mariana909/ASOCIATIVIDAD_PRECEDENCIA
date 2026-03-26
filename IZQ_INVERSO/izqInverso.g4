grammar izqInverso;

programa: term EOF;

term
    : term MUL expresion
    | term DIV expresion
    | expresion
    ;

expresion
    : expresion SUM factor
    | expresion RES factor
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