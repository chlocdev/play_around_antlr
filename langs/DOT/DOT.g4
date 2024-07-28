grammar DOT;

// Parser rules
graph
    : 'digraph' ID '{' stmt_list '}'
    ;

stmt_list
    : (stmt ';')* (stmt)?
    ;

stmt
    : node_stmt
    | edge_stmt
    | attr_stmt
    | ID '=' ID
    ;

node_stmt
    : node_id (attr_list)?
    ;

edge_stmt
    : (node_id | subgraph) edgeRHS (attr_list)?
    ;

attr_stmt
    : ('graph' | 'node' | 'edge') attr_list
    ;

attr_list
    : '[' a_list? ']'
    ;

a_list
    : (ID '=' ID) (',' ID '=' ID)* (',')?
    ;

edgeRHS
    : ('->' | '--') (node_id | subgraph) (('->' | '--') (node_id | subgraph))*
    ;

node_id
    : ID (port)?
    ;

port
    : ':' ID (':' ID)?
    ;

subgraph
    : 'subgraph' (ID)? '{' stmt_list '}'
    ;

// Lexer rules
ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;

LINE_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
