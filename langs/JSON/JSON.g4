grammar JSON;

// Lexer rules
fragment DIGIT : '0'..'9';
fragment ESCAPE
    : '\\' ( ["\\/bfnrt] | UNICODE )
    ;
fragment UNICODE
    : 'u' HEX HEX HEX HEX
    ;
fragment HEX : [0-9a-fA-F];

STRING
    : '"' ( ESCAPE | ~ ["\\\r\n] )* '"'
    ;

NUMBER
    : '-'? INT ( '.' DIGIT+ )? EXP?
    ;
fragment INT
    : '0' | [1-9] DIGIT*
    ;
fragment EXP
    : [eE] [+\-]? DIGIT+
    ;

TRUE
    : 'true'
    ;

FALSE
    : 'false'
    ;

NULL
    : 'null'
    ;

// Parser rules
json
    : value
    ;

obj
    : '{' pair ( ',' pair )* '}'
    | '{' '}'
    ;

pair
    : STRING ':' value
    ;

array
    : '[' value ( ',' value )* ']'
    | '[' ']'
    ;

value
    : STRING
    | NUMBER
    | obj
    | array
    | TRUE
    | FALSE
    | NULL
    ;

// Ignore whitespace
WS
    : [ \t\r\n]+ -> skip
    ;
