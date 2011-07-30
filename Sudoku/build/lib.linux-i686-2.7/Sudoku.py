"""
Sudoku module.

Module stores Sudoku class.

"""
SUDOKU_SIZE = 9

from curses.ascii import isdigit

    
class Sudoku(object):
	
	def init_from_file(self, filename = "sudoku.txt"):
		"""
		Public method.
		Gets sudoku data from file. By default: sudoku.txt
		"""
		try:
			f = open(filename, "r")
		except (IOError):
			return False
		f.readline()	# skiping first line
		self.__matrix = self.__to_matrix( f.read() )
		f.close()
		return True
	# end

	def __init__(self):
		"""
		Constructor.
		Initialize empty sudoku matrix.
		"""     
		self.__matrix = []      # main sudoku matrix
	# end

	def init_from_string(self, string):
		"""
		Public method.
		Get sudoku data from string.
		"""
		self.__matrix = self.__to_matrix(string);
	# end

	def solve(self):
		"""
		Public method.
		Sudoku solving.
		Returns list of lists whith all posibles solvations.
		"""
		answer = []

		def backtracking(i, j):
			"""Inner method. """
			if j == 9:
				j = 0
				i += 1
				if i == 9:
					answer.append(self.__cpy(self.__matrix))
				else:
					backtracking(i, j)
			else:
				if not self.__matrix[i][j]:
					for value in range(1, SUDOKU_SIZE + 1):
						if self.check(i, j, value):
							self.__matrix[i][j] = value
							backtracking(i, j+1)
							self.__matrix[i][j] = 0
				else:
					backtracking(i, j+1)

		backtracking(0, 0)
		return answer;
	# end

	def check(self, row, collumn, value):
		"""
		Public method.
		Returns true if value is available in particular coordinates,
		else returns false 
		"""
		return  (
				self.__check_row(row, value) and
				self.__check_collumn(collumn, value) and
				self.__check_square(row, collumn, value)
				)
	# end

	def print_sudoku(self):
		"""
		Public method.
		Simple sudoku print for testing.
		"""
		for i in range(SUDOKU_SIZE):
			print self.__matrix[i];

	# end

	def format_sudoku_answer(answer):
		"""
		Public static method
		Print all posible sudoku answers
		"""

		SQ_SIZE = SUDOKU_SIZE / 3
		string = ""
		for i in range(len(answer)):	# number of answers
			for x in range(SQ_SIZE):	
				for y in range(SQ_SIZE):
					for z in range(SQ_SIZE):
						for k in range(SQ_SIZE):
							string += str(answer[i][x*SQ_SIZE + y][z*SQ_SIZE + k])
						string += ' '
					string += "\n"
				string += "\n"
		return string
	# end
	# set print_sudoku_answer method to be static
	format_sudoku_answer = staticmethod(format_sudoku_answer)
	
	def __to_matrix(self, string):
		"""
		Private method.
		Creates main sudoku matrix from string
		Return: main matrix and list of bool's (is currnet element const).
		"""
		matrix = []
		tmp = []
		j = 0
		for i in range(len(string)):
			if isdigit(string[i]):          
				tmp.append(int(string[i]));
				j += 1; 
				if j == SUDOKU_SIZE:            # add line to main matrix
					matrix.append(tmp)
					j = 0
					tmp = []
					if len(matrix) == SUDOKU_SIZE: # main matrix completed
						break;

		return matrix
	# end

	def __cpy(self, array):
		"""
		Private method.
		For deep sudoku matrix copy.
		"""
		new = []
		for i in range(SUDOKU_SIZE):
			new.append(list(array[i]))
		return new
	# end



	def __check_row(self, row, value):
		"""
		Private method.
		Check if value available in a particular row 
		"""
		if row in range(SUDOKU_SIZE):
			for j in range(SUDOKU_SIZE):
				if self.__matrix[row][j] == value:
					return False
		else:
			return False
		return True    # if not failed returns True
	# end

	def __check_collumn(self, collumn, value):
		"""
		Private method.
		Check if value available in a particular collumn
		"""
		if collumn in range(SUDOKU_SIZE):
			for i in range(SUDOKU_SIZE):
				if self.__matrix[i][collumn] == value:
					return False
		else:
			return False
		return True     # if not failed returns True
	# end   


	def __check_square(self, row, collumn, value):
		"""
		Private method.
		Check if value available in a particular square
		"""
		if not (row in range(SUDOKU_SIZE) and collumn in range(SUDOKU_SIZE)):
			return False    

		SIZE    = SUDOKU_SIZE / 3
		ROW     = (row / SIZE)* SIZE
		COLLUMN = (collumn / SIZE)* SIZE

		for i in range(SIZE):
			for j in range(SIZE):
				if self.__matrix[ROW+i][COLLUMN+j] == value:
					return False
		return True		 # if not failed returns True
	# end
# end
