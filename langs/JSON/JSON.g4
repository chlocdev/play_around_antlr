grammar JSON;

json
    : value
    ;

value
    : STRING
    | NUMBER
    | obj
    | array
    | 'true'
    | 'false'
    | 'null'
    ;


obj
    : '{' pair (',' pair)* '}'
    | '{' '}'
    ;

pair
    : STRING ':' value
    ;

array
    : '[' value (',' value)* ']'
    | '[' ']'
    ;

STRING
    : '"' (ESC | ~["\\])* '"'
    ;

fragment ESC
    : '\\' (["\\/bfnrt] | 'u' HEX HEX HEX HEX)
    ;

NUMBER
    : '-'? INT ('.' [0-9] +)? EXP?
    ;

fragment INT
    : '0'
    | [1-9] [0-9]*
    ;

fragment EXP
    : [eE] [+\-]? [0-9]+
    ;

WS
    : [ \t\n\r]+ -> skip
    ;

fragment HEX
    : [0-9a-fA-F]
    ;
