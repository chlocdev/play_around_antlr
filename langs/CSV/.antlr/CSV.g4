grammar CSV;

file: header row* EOF;

header: row;

row: field (',' field)* '\r'? '\n';

field
    : TEXT
    | QUOTED_TEXT
    ;

TEXT
    : ~[,\r\n"]+ // Match any character except ',', '\r', '\n', and '"'
    ;

QUOTED_TEXT
    : '"' ('""' | ~'"')* '"' // Match text enclosed in double quotes, allowing for escaped quotes
    ;

WS
    : [ \t]+ -> skip // Ignore whitespace
    ;
