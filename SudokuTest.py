#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       SudokuTest.py
#       
#       Copyright 2011 zee <zee@zee-Extensa-5635Z>
#       
#       2011-07-30
from Sudoku import Sudoku

SUDOKU = """
003 070 900
200 308 600
075 902 010

050 000 243
002 834 500
437 000 090

020 109 430
004 705 002
006 020 702
"""

def main():
	s = Sudoku()
	s.init_from_string(SUDOKU)
	
	s.print_sudoku()

	Sudoku.print_sudoku_answer( s.solve() )
	return 0

if __name__ == '__main__':
	main()

