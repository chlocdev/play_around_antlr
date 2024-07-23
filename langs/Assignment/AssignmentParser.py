# Generated from langs/Assignment/Assignment.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,18,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,3,0,9,8,0,1,1,4,1,12,8,
        1,11,1,12,1,13,1,1,1,1,1,1,0,0,2,0,2,0,0,17,0,4,1,0,0,0,2,11,1,0,
        0,0,4,5,5,3,0,0,5,6,5,1,0,0,6,8,5,4,0,0,7,9,5,5,0,0,8,7,1,0,0,0,
        8,9,1,0,0,0,9,1,1,0,0,0,10,12,3,0,0,0,11,10,1,0,0,0,12,13,1,0,0,
        0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,3,1,
        0,0,0,2,8,13
    ]

class AssignmentParser ( Parser ):

    grammarFileName = "Assignment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "ID", "INT", "NEWLINE" ]

    RULE_assignment = 0
    RULE_prog = 1

    ruleNames =  [ "assignment", "prog" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    ID=3
    INT=4
    NEWLINE=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AssignmentParser.ID, 0)

        def INT(self):
            return self.getToken(AssignmentParser.INT, 0)

        def NEWLINE(self):
            return self.getToken(AssignmentParser.NEWLINE, 0)

        def getRuleIndex(self):
            return AssignmentParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = AssignmentParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(AssignmentParser.ID)
            self.state = 5
            self.match(AssignmentParser.T__0)
            self.state = 6
            self.match(AssignmentParser.INT)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 7
                self.match(AssignmentParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AssignmentParser.EOF, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(AssignmentParser.AssignmentContext,i)


        def getRuleIndex(self):
            return AssignmentParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = AssignmentParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.assignment()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 15
            self.match(AssignmentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





