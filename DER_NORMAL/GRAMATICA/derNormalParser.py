# Generated from derNormal.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,32,8,2,1,3,1,3,1,3,3,3,37,8,3,1,3,0,0,4,0,2,4,6,0,0,39,
        0,8,1,0,0,0,2,20,1,0,0,0,4,31,1,0,0,0,6,36,1,0,0,0,8,9,3,2,1,0,9,
        10,5,0,0,1,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,1,0,0,13,14,3,2,1,
        0,14,21,1,0,0,0,15,16,3,4,2,0,16,17,5,2,0,0,17,18,3,2,1,0,18,21,
        1,0,0,0,19,21,3,4,2,0,20,11,1,0,0,0,20,15,1,0,0,0,20,19,1,0,0,0,
        21,3,1,0,0,0,22,23,3,6,3,0,23,24,5,3,0,0,24,25,3,4,2,0,25,32,1,0,
        0,0,26,27,3,6,3,0,27,28,5,4,0,0,28,29,3,4,2,0,29,32,1,0,0,0,30,32,
        3,6,3,0,31,22,1,0,0,0,31,26,1,0,0,0,31,30,1,0,0,0,32,5,1,0,0,0,33,
        37,5,5,0,0,34,35,5,2,0,0,35,37,5,5,0,0,36,33,1,0,0,0,36,34,1,0,0,
        0,37,7,1,0,0,0,3,20,31,36
    ]

class derNormalParser ( Parser ):

    grammarFileName = "derNormal.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "SUM", "RES", "MUL", "DIV", "NUM", "DECIMAL", 
                      "ENTERO", "WS" ]

    RULE_programa = 0
    RULE_expresion = 1
    RULE_factor = 2
    RULE_term = 3

    ruleNames =  [ "programa", "expresion", "factor", "term" ]

    EOF = Token.EOF
    SUM=1
    RES=2
    MUL=3
    DIV=4
    NUM=5
    DECIMAL=6
    ENTERO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(derNormalParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(derNormalParser.EOF, 0)

        def getRuleIndex(self):
            return derNormalParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = derNormalParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expresion()
            self.state = 9
            self.match(derNormalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(derNormalParser.FactorContext,0)


        def SUM(self):
            return self.getToken(derNormalParser.SUM, 0)

        def expresion(self):
            return self.getTypedRuleContext(derNormalParser.ExpresionContext,0)


        def RES(self):
            return self.getToken(derNormalParser.RES, 0)

        def getRuleIndex(self):
            return derNormalParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = derNormalParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.factor()
                self.state = 12
                self.match(derNormalParser.SUM)
                self.state = 13
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.factor()
                self.state = 16
                self.match(derNormalParser.RES)
                self.state = 17
                self.expresion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(derNormalParser.TermContext,0)


        def MUL(self):
            return self.getToken(derNormalParser.MUL, 0)

        def factor(self):
            return self.getTypedRuleContext(derNormalParser.FactorContext,0)


        def DIV(self):
            return self.getToken(derNormalParser.DIV, 0)

        def getRuleIndex(self):
            return derNormalParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = derNormalParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.term()
                self.state = 23
                self.match(derNormalParser.MUL)
                self.state = 24
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.term()
                self.state = 27
                self.match(derNormalParser.DIV)
                self.state = 28
                self.factor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(derNormalParser.NUM, 0)

        def RES(self):
            return self.getToken(derNormalParser.RES, 0)

        def getRuleIndex(self):
            return derNormalParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = derNormalParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(derNormalParser.NUM)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(derNormalParser.RES)
                self.state = 35
                self.match(derNormalParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





