from antlr4 import *
from GRAMATICA.derNormalParser import derNormalParser
from GRAMATICA.derNormalVisitor import derNormalVisitor

class VisitorDN(derNormalVisitor):
    def visitPrograma(self, ctx:derNormalParser.ProgramaContext):
        return self.visit(ctx.expresion())

    def visitExpresion(self, ctx:derNormalParser.ExpresionContext):
        print(f"visitExpresion childCount={ctx.getChildCount()} texto='{ctx.getText()}'")
    
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        
        left = self.visit(ctx.factor())
        right = self.visit(ctx.expresion())
        
        print(f"  left={left}, right={right}")
        
        if ctx.SUM():
            return left + right
        else:
            return left - right

    def visitFactor(self, ctx:derNormalParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        
        left = self.visit(ctx.term())
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
