# Generated from langs/CSV/CSV.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete listener for a parse tree produced by CSVParser.
class CSVListener(ParseTreeListener):

    # Enter a parse tree produced by CSVParser#file.
    def enterFile(self, ctx:CSVParser.FileContext):
        pass

    # Exit a parse tree produced by CSVParser#file.
    def exitFile(self, ctx:CSVParser.FileContext):
        pass


    # Enter a parse tree produced by CSVParser#header.
    def enterHeader(self, ctx:CSVParser.HeaderContext):
        pass

    # Exit a parse tree produced by CSVParser#header.
    def exitHeader(self, ctx:CSVParser.HeaderContext):
        pass


    # Enter a parse tree produced by CSVParser#row.
    def enterRow(self, ctx:CSVParser.RowContext):
        pass

    # Exit a parse tree produced by CSVParser#row.
    def exitRow(self, ctx:CSVParser.RowContext):
        pass


    # Enter a parse tree produced by CSVParser#field.
    def enterField(self, ctx:CSVParser.FieldContext):
        pass

    # Exit a parse tree produced by CSVParser#field.
    def exitField(self, ctx:CSVParser.FieldContext):
        pass



del CSVParser