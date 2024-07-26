grammar BadExpr;

prog: stat+ stat* ; // unnecessary repetition

stat: expr NEWLINE
    | ID '=' expr NEWLINE
    | NEWLINE
    | ID '=' INT NEWLINE // unnecessary duplication of rules
    ;

expr: expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | term
    | INT
    | ID
    | '(' expr ')'
    ;

term: factor // unnecessary intermediate rule
    ;

factor: INT
    | ID
    | '(' expr ')'
    ;

ID: [a-zA-Z]+ ; // match identifiers

INT: [0-9]+ ; // match integers

NEWLINE: '\r'? '\n' ; // return newlines to parser (is end-statement signal)

WS: [ \t]+ -> skip ; //toss out whitespace
