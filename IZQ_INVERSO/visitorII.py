from antlr4 import *
from GRAMATICA.izqInversoParser import izqInversoParser
from GRAMATICA.izqInversoVisitor import izqInversoVisitor

class VisitorII(izqInversoVisitor):
    def visitPrograma(self, ctx:izqInversoParser.ProgramaContext):
        return self.visit(ctx.expresion())

    def visitExpresion(self, ctx:izqInversoParser.ExpresionContext):
        if ctx.getChildCount() ==1:
            return self.visit(ctx.factor())
        left = self.visit(ctx.expresion())
        right = self.visit(ctx.factor())
        
        if ctx.MUL():
            return left * right
        else:
            if right == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            result = left / right
    
            if result.is_integer():
                return int(result)
            
            return result

    def visitFactor(self, ctx:izqInversoParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        
        left = self.visit(ctx.factor())
        right = self.visit(ctx.term())
        
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