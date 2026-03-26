# Generated from izqInverso.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .izqInversoParser import izqInversoParser
else:
    from izqInversoParser import izqInversoParser

# This class defines a complete generic visitor for a parse tree produced by izqInversoParser.

class izqInversoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by izqInversoParser#programa.
    def visitPrograma(self, ctx:izqInversoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqInversoParser#expresion.
    def visitExpresion(self, ctx:izqInversoParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqInversoParser#factor.
    def visitFactor(self, ctx:izqInversoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqInversoParser#term.
    def visitTerm(self, ctx:izqInversoParser.TermContext):
        return self.visitChildren(ctx)



del izqInversoParser