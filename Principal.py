#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []

    # Tokenize and reload of the buffer
    for i in Buffer.load_buffer():
        t, lex, lin, col = Analyzer.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    print('\nRecognize Tokens: ', token)

