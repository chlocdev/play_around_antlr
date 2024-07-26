# Generated from langs/CSV/CSV.g4 by ANTLR 4.13.1
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
        4,1,6,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,0,
        12,0,14,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,2,3,2,29,8,2,1,2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,4,5,
        33,0,8,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,32,1,0,0,0,8,12,3,2,1,
        0,9,11,3,4,2,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,
        0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,3,4,2,0,18,3,1,0,0,0,19,24,3,6,3,0,20,21,5,1,0,0,21,23,3,6,3,
        0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,28,
        1,0,0,0,26,24,1,0,0,0,27,29,5,2,0,0,28,27,1,0,0,0,28,29,1,0,0,0,
        29,30,1,0,0,0,30,31,5,3,0,0,31,5,1,0,0,0,32,33,7,0,0,0,33,7,1,0,
        0,0,3,12,24,28
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\\r'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "QUOTED_TEXT", "WS" ]

    RULE_file = 0
    RULE_header = 1
    RULE_row = 2
    RULE_field = 3

    ruleNames =  [ "file", "header", "row", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TEXT=4
    QUOTED_TEXT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(CSVParser.HeaderContext,0)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = CSVParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.header()
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 9
                self.row()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(CSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = CSVParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.field()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.match(CSVParser.T__0)
                self.state = 21
                self.field()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 27
                self.match(CSVParser.T__1)


            self.state = 30
            self.match(CSVParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def QUOTED_TEXT(self):
            return self.getToken(CSVParser.QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





