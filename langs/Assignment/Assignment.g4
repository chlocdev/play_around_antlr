grammar Assignment;

// Lexer rules
WS : [ \t\r\n]+ -> skip; // skip whitespace

ID : [a-zA-Z]+ ; // match identifiers (letters only)

INT : [0-9]+ ; // match integers

// Parser rules
assignment : ID '=' INT NEWLINE? ;

NEWLINE : '\r'? '\n' ;

prog: assignment+ EOF ;
