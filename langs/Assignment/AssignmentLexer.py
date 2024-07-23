# Generated from langs/Assignment/Assignment.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,4,1,15,8,1,11,1,12,1,16,1,1,1,1,1,2,4,2,22,8,2,11,2,12,2,23,1,
        3,4,3,27,8,3,11,3,12,3,28,1,4,3,4,32,8,4,1,4,1,4,0,0,5,1,1,3,2,5,
        3,7,4,9,5,1,0,3,3,0,9,10,13,13,32,32,2,0,65,90,97,122,1,0,48,57,
        38,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,
        11,1,0,0,0,3,14,1,0,0,0,5,21,1,0,0,0,7,26,1,0,0,0,9,31,1,0,0,0,11,
        12,5,61,0,0,12,2,1,0,0,0,13,15,7,0,0,0,14,13,1,0,0,0,15,16,1,0,0,
        0,16,14,1,0,0,0,16,17,1,0,0,0,17,18,1,0,0,0,18,19,6,1,0,0,19,4,1,
        0,0,0,20,22,7,1,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,
        24,1,0,0,0,24,6,1,0,0,0,25,27,7,2,0,0,26,25,1,0,0,0,27,28,1,0,0,
        0,28,26,1,0,0,0,28,29,1,0,0,0,29,8,1,0,0,0,30,32,5,13,0,0,31,30,
        1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,10,0,0,34,10,1,0,0,0,
        5,0,16,23,28,31,1,6,0,0
    ]

class AssignmentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    ID = 3
    INT = 4
    NEWLINE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "INT", "NEWLINE" ]

    ruleNames = [ "T__0", "WS", "ID", "INT", "NEWLINE" ]

    grammarFileName = "Assignment.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


