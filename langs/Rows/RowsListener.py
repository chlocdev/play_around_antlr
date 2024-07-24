# Generated from langs/Rows/Rows.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RowsParser import RowsParser
else:
    from RowsParser import RowsParser

# This class defines a complete listener for a parse tree produced by RowsParser.
class RowsListener(ParseTreeListener):

    # Enter a parse tree produced by RowsParser#file.
    def enterFile(self, ctx:RowsParser.FileContext):
        pass

    # Exit a parse tree produced by RowsParser#file.
    def exitFile(self, ctx:RowsParser.FileContext):
        pass


    # Enter a parse tree produced by RowsParser#row.
    def enterRow(self, ctx:RowsParser.RowContext):
        pass

    # Exit a parse tree produced by RowsParser#row.
    def exitRow(self, ctx:RowsParser.RowContext):
        pass



del RowsParser