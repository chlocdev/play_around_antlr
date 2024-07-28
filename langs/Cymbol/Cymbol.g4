grammar Cymbol;

// Parser rules
prog: (varDecl | functionDecl)*;

varDecl: type ID '=' expr ';';

functionDecl: type ID '(' params? ')' block;

params: param (',' param)*;
param: type ID;

block: '{' stmt* '}';
stmt: exprStmt
    | ifStmt
    | returnStmt
    | block;

exprStmt: expr ';';
ifStmt: 'if' expr 'then' stmt;
returnStmt: 'return' expr ';';

expr: expr ('*' | '/' | '+' | '-') expr
    | expr '==' expr
    | ID '(' args? ')'
    | ID
    | INT
    | '(' expr ')'
    ;

args: expr (',' expr)*;

// Lexer rules
type: 'int';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;

COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
