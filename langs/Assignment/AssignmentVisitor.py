# Generated from langs/Assignment/Assignment.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AssignmentParser import AssignmentParser
else:
    from AssignmentParser import AssignmentParser

# This class defines a complete generic visitor for a parse tree produced by AssignmentParser.

class AssignmentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssignmentParser#assignment.
    def visitAssignment(self, ctx:AssignmentParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentParser#prog.
    def visitProg(self, ctx:AssignmentParser.ProgContext):
        return self.visitChildren(ctx)



del AssignmentParser