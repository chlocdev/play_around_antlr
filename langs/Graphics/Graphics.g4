grammar Graphics;

file : command+ ; // a file is a list of commands

command : 'line' 'from' point 'to' point ;

point : INT ',' INT ; // E.g., "0,10"

INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;