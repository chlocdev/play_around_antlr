# Generated from langs/Assignment/Assignment.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AssignmentParser import AssignmentParser
else:
    from AssignmentParser import AssignmentParser

# This class defines a complete listener for a parse tree produced by AssignmentParser.
class AssignmentListener(ParseTreeListener):

    # Enter a parse tree produced by AssignmentParser#assignment.
    def enterAssignment(self, ctx:AssignmentParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AssignmentParser#assignment.
    def exitAssignment(self, ctx:AssignmentParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AssignmentParser#prog.
    def enterProg(self, ctx:AssignmentParser.ProgContext):
        pass

    # Exit a parse tree produced by AssignmentParser#prog.
    def exitProg(self, ctx:AssignmentParser.ProgContext):
        pass



del AssignmentParser