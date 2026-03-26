import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from IZQ_INVERSO.visitorII import VisitorII
from GRAMATICA.izqInversoLexer import izqInversoLexer
from GRAMATICA.izqInversoParser import izqInversoParser

def evaluar(expresion):
    input_stream = InputStream(expresion)
    lexer = izqInversoLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = izqInversoParser(tokens)
    
    tree = parser.programa() 
    
    visitor = VisitorII()
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