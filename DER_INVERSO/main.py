import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from DER_INVERSO.visitorDI import VisitorDI
from GRAMATICA.derInversoLexer import derInversoLexer
from GRAMATICA.derInversoParser import derInversoParser

def evaluar(expresion):
    input_stream = InputStream(expresion)
    lexer = derInversoLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = derInversoParser(tokens)
    
    tree = parser.programa() 
    
    visitor = VisitorDI()
    return visitor.visit(tree)

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            with open(entrada, 'r') as en:
                datos = en.read().splitlines()
                
                for linea in datos:
                    if linea.strip() == "":
                        continue
                    
                    resultado = evaluar(linea)
                    print(f"{linea} = {resultado}")
        else:
            print("No se detectó archivo de entrada")

    except FileNotFoundError:
        print("No se encontró el archivo")