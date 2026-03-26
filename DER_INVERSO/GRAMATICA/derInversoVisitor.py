# Generated from derInverso.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .derInversoParser import derInversoParser
else:
    from derInversoParser import derInversoParser

# This class defines a complete generic visitor for a parse tree produced by derInversoParser.

class derInversoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by derInversoParser#programa.
    def visitPrograma(self, ctx:derInversoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derInversoParser#expresion.
    def visitExpresion(self, ctx:derInversoParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derInversoParser#factor.
    def visitFactor(self, ctx:derInversoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derInversoParser#term.
    def visitTerm(self, ctx:derInversoParser.TermContext):
        return self.visitChildren(ctx)



del derInversoParser