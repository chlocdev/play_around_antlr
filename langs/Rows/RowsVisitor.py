# Generated from langs/Rows/Rows.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RowsParser import RowsParser
else:
    from RowsParser import RowsParser

# This class defines a complete generic visitor for a parse tree produced by RowsParser.

class RowsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RowsParser#file.
    def visitFile(self, ctx:RowsParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RowsParser#row.
    def visitRow(self, ctx:RowsParser.RowContext):
        return self.visitChildren(ctx)



del RowsParser