# Generated from derNormal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .derNormalParser import derNormalParser
else:
    from derNormalParser import derNormalParser

# This class defines a complete generic visitor for a parse tree produced by derNormalParser.

class derNormalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by derNormalParser#programa.
    def visitPrograma(self, ctx:derNormalParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derNormalParser#expresion.
    def visitExpresion(self, ctx:derNormalParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derNormalParser#factor.
    def visitFactor(self, ctx:derNormalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by derNormalParser#term.
    def visitTerm(self, ctx:derNormalParser.TermContext):
        return self.visitChildren(ctx)



del derNormalParser