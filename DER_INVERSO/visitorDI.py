from antlr4 import *
from GRAMATICA.derInversoParser import derInversoParser
from GRAMATICA.derInversoVisitor import derInversoVisitor

class VisitorDI(derInversoVisitor):
    def visitPrograma(self, ctx:derInversoParser.ProgramaContext):
        return self.visit(ctx.expresion())

    def visitExpresion(self, ctx:derInversoParser.ExpresionContext):
        if ctx.getChildCount() ==1:
            return self.visit(ctx.factor())
        left = self.visit(ctx.factor())
        right = self.visit(ctx.expresion())
        
        if ctx.MUL():
            return left * right
        else:
            if right == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            result = left / right
    
            if result.is_integer():
                return int(result)
            
            return result

    def visitFactor(self, ctx:derInversoParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        
        if ctx.SUM():
            return left + right
        else:
            return left - right

    def visitTerm(self, ctx):
        text = ctx.NUM().getText()
        
        if '.' in text:
            value = float(text)
        else:
            value = int(text)
        
        if ctx.RES():
            return -value
        else:
            return value