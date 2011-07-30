#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       SudokuSolver.py
#       
#       Copyright 2011 zee <zygis.gg@gmail.com>
#       
#       2011-07-30

# This constant is used when option flag is -e or -c.
SUDOKU = """	
015 000 090
092 453 007
060 080 500

700 510 480
050 308 020
084 029 005

008 060 070
100 297 350
070 000 260
"""


import time
from sys import argv
from Sudoku import Sudoku


# FLAGS
HELP		= ("help", "h")

FROM_FILE_TO_FILE 		= "f" 
FROM_CONST_TO_FILE 		= "c"
FROM_FILE_TO_DISLAY 	= "d"
FROM_CONST_TO_DISPALY 	= "e"

def display_help ():
	print """
Usage: python SudokuSolver.py [option] [source_file] [destination_file]\n
	-help, -h        	: display help info
	-f                	: sudoku source is file sudoku.txt, destination file is answer.txt
	-f [filename1] [filename2] : sudoku source is file named [filename1], destination file is [filename2]
	-c [filename]     	: sudoku source is const SUDOKU from file SudokuSolver.py (read README) answer is in [filename]
	-c	             	: sudoku source is const SUDOKU from file SudokuSolver.py (read README) answer is in answer.txt
	-d [filename]      	: sudoku source file is [filename], answer is displayed in console
	-d 	              	: sudoku source file is sudoku.txt, answer is displayed in console
	-e                	: sudoku source is const SUDOKU from file SudokuSolver.py (read README) answer is displayed in console
	"""
		
def main():
	
	num_of_flags = len(argv) -1
	
	sudoku = Sudoku();
	
	if num_of_flags > 0:
		
		if '-' in argv[1]:		# is correct flag
			flag = argv[1]
			flag = flag[1:]
			
			if FROM_FILE_TO_FILE == flag:		# flag -f
				if num_of_flags > 2:
					if  not sudoku.init_from_file(argv[2]):
						exit("File " + argv[2] + " not exist.")
					try:
						f = open(argv[3], "w")
					except(IOError):
						exit("File error.")					
				else:
					if  not sudoku.init_from_file():
						exit("File sudoku.txt not exist.");
					try:
						f = open("answer.txt", "w")
					except(IOError):
						exit("File error.")
				st = time.time()
				answer = Sudoku.format_sudoku_answer( sudoku.solve() )
				f.write(answer)
				print "Time elapsed: {0} s. ".format(time.time() - st)	
				
			elif FROM_CONST_TO_FILE == flag:  	# flag -c
				sudoku.init_from_string(SUDOKU)
				st = time.time()
				answer = Sudoku.format_sudoku_answer( sudoku.solve() )
				if num_of_flags > 1:
					try:
						f = open(argv[2], "w")
					except(IOError):
						exit("File error.")
				else:
					try:
						f = open("answer.txt", "w")
					except(IOError):
						exit("File error.")
				f.write(answer)
				print "Time elapsed: {0} s. ".format(time.time() - st)	
				
			elif FROM_FILE_TO_DISLAY == flag:		# flag -d
				if num_of_flags > 1:
					if  not sudoku.init_from_file(argv[2]):
						exit("File " + argv[2] + " not exist.");
				else:
					if  not sudoku.init_from_file():
						exit("File sudoku.txt not exist.");
				st = time.time()
				answer = Sudoku.format_sudoku_answer( sudoku.solve() )
				print "ANSWER:\n", answer
				print "Time elapsed: {0} s. ".format(time.time() - st)

			elif FROM_CONST_TO_DISPALY == flag:		# flag -e
				sudoku.init_from_string(SUDOKU)
				st = time.time()
				answer = Sudoku.format_sudoku_answer( sudoku.solve() )
				print "ANSWER:\n", answer
				print "Time elapsed: {0} s. ".format(time.time() - st)
				
			elif HELP[0] == flag or HELP[1] == flag:
				display_help();
			else:
				exit("Incorect flag. Use SudokuSolver.py -help")
		else:
				exit("Incorect flag. Use SudokuSolver.py -help")
	else:
		if not sudoku.init_from_file():
			exit("File sudoku.txt not exist.");
		try:
			f = open("answer.txt", "w")
		except(IOError):
			exit("File error.")
		st = time.time()
		answer = Sudoku.format_sudoku_answer( sudoku.solve() )
		f.write(answer)
		print "Time elapsed: {0} s. ".format(time.time() - st)	
	return 0

if __name__ == '__main__':
	main()

