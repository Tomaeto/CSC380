import random
from copy import copy, deepcopy
import sys
import getopt

#Adrian Faircloth
#03-15-22
#CSC380
#Project 2: Game of Life Simulation

#Simulate's Conway's Game of Life, with options for a specified starting grid and generational death toggle

#Class containing ASCII color codes, used for colored printing
class colors:
	red='\033[31m'
	green='\033[32m'
	blue='\033[34m'
	cyan='\033[36m'
	grey='\033[90m'
	yellow='\033[93m'
	end='\033[0m'
	
#Function simulating Game of Life
'''
Game of Life Rules:
	Cells with less than 2 neighbors, more than 3 neighbors, or an age over 10 die.
	Cells with 2 neighbors are stable and retain their current state.
	Cells with 3 neighbors becomes or remains populated.
	If genDeath is set to 0, death due to age does not occur.
	All changes occur simultaneously.
'''
def evoSim(grid, genDeath):
#Copying current grid to apply changes w/o changing main grid
	nextGrid = deepcopy(grid)
	
#Looping through the 2-D grid, checking game rules and changing nextGrid as needed
	for i in range (0, 20):
		for j in range (0, 20):

		#Getting values of neighboring cells and counting number of neighbors
			aroundVals = checkNeighbors(grid, i, j)
			numNeighbors = aroundVals.count(1)

		#Emptying cell and resetting age if it meets death conditions
			if (numNeighbors < 2 or numNeighbors > 3 or (grid[i][j][1] > 10 and genDeath == 1)):
				nextGrid[i][j][0] = 0
				nextGrid[i][j][0] = 0

		#Incrementing age if cell meets stability conditions
			elif (numNeighbors == 2 and grid[i][j][0] == 1):
				nextGrid[i][j][1] += 1

		#Populating and aging if cell meets population condition
			elif (numNeighbors == 3):
				nextGrid[i][j][0] = 1
				nextGrid[i][j][1] += 1

#Copying nextGrid state into main grid to make changes simultaneously and returning new grid state
	grid = deepcopy(nextGrid)
	return grid

#Function for checking neighbors of a given cell
#Returns list of all neighboring cells' population states
def checkNeighbors(grid, row, col):
	neighborVal = []
'''
If a cell is a corner, check its three neighbors.
If a cell is an edge cell, check its five neighbors.
Otherwise, check all eight neighbors.
'''

#Checking top left corner
	if (row == 0 and col == 0):
		neighborVal.extend( [grid[0][1][0], 
				     grid[1][0][0], 
			 	     grid[1][1][0]] )

#Checking top right corner
	elif (row == 0 and col == 19):
		neighborVal.extend( [grid[0][18][0],
				     grid[1][19][0],
				     grid[1][18][0]] )

#Checking bottom left corner
	elif (row == 19 and col == 0):
		neighborVal.extend( [grid[19][1][0],
				     grid[18][0][0],
				     grid[18][1][0]] )

#Checking bottom right corner
	elif (row == 19 and col == 19):
		neighborVal.extend( [grid[19][18][0],
				     grid[18][19][0],
				     grid[18][18][0]] )

#Checking top row
	elif (row == 0):
		neighborVal.extend( [grid[0][col+1][0],
				     grid[0][col-1][0],
				     grid[1][col][0],
				     grid[1][col+1][0],
				     grid[1][col-1][0]] )

#Checking bottom row
	elif (row == 19):
		neighborVal.extend( [grid[19][col+1][0],
				     grid[19][col-1][0],
				     grid[18][col][0],
				     grid[18][col+1][0],
				     grid[18][col-1][0]] )

#Checking left column
	elif (col == 0):
		neighborVal.extend( [grid[row][1][0],
				     grid[row+1][0][0],
				     grid[row+1][1][0],
				     grid[row-1][0][0],
				     grid[row-1][1][0]] )

#Checking right column
	elif (col == 19):
		neighborVal.extend( [grid[row][18][0],
				     grid[row+1][19][0],
				     grid[row+1][18][0],
		 		     grid[row-1][19][0],
				     grid[row-1][18][0]] )

#Checking middle cell
	else:
		neighborVal.extend( [grid[row][col+1][0],
				     grid[row][col-1][0],
				     grid[row-1][col][0],
				     grid[row-1][col+1][0],
				     grid[row-1][col-1][0],
				     grid[row+1][col][0],
				     grid[row+1][col+1][0],
				     grid[row+1][col-1][0]] )

	return neighborVal

#Function for printing grid state
def printGrid(grid):
'''
Prints state of each cell in 2D grid
If population value is 1, print blue X representing populated cell
Otherwise, print grey dot representing empty cell
'''
	for i in range (0, 20):
		for j in range (0, 20):
			if (grid[i][j][0] == 1):
				print(colors.blue + 'X' + colors.end, end=' ')
			else:
				print(colors.grey + '.' + colors.end, end=' ')
#Printing empty lines for formatting
		print('')
	print('')

#Function for randomizing grid
def randGrid(grid):	
'''
Randomly generates a grid state, with every
cell given a 50/50 chance of being populated or not
'''
	for i in range (0, 20):
		for j in range (0, 20):
			grid[i][j][0] = random.randint(0, 1)	
			if (grid[i][j][0] == 1):
				grid[i][j][1] = 1

#Function for getting grid state from file
def getGrid(grid, arg):
'''
Gets text grid from file, removes spaces and newlines,
and sets each grid state based on each character.


If any character in text grid is not '0' or 'X', or file name is invalid, prints error and exits.
'''

#Opening input file for reading, printing error and exiting if file not found
	try:
		infile = open(arg, 'r')
	except FileNotFoundError: 
		print("Error opening input file")
		sys.exit()

#Getting grid from input file, closing file, and removing whitespace and newlines
	txtGrid = infile.read()
	infile.close()
	txtGrid = txtGrid.replace(" ", '')
	txtGrid = txtGrid.replace ("\n", '')

#Setting each cell in 2D grid based on characters in text grid
#Uses txtIndex to iterate through text grid
	txtIndex = 0
	for i in range (0, 20):
		for j in range (0, 20):
			char = txtGrid[txtIndex]
			txtIndex += 1
			if (char == "0"):
				grid[i][j][0] = 0
			elif (char == "X"):
				grid[i][j][0] = 1
			else:
				print("Error parsing input file")
				sys.exit()
	
#Function for printing help menu
def printHelp():
	print(colors.green + "\n--help\tDisplay this command block."
	     		   + "\n-f\tUse provided file for grid generation instead of randomized grid." 
			   + "\n-g\tClassic version of Conway's Game, disables generational death"+ colors.end)

#Function for printing start menu
def printMenu():
	print(colors.cyan + "Artificial Simulation of The Game of Life\n" + colors.end +
		"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") 
	print(colors.green + "\nEach cell with zero or one neighbor dies by loneliness.\n" 
			    + "\nEach cell with two neighbors is stable, and does not change.\n"
			    + "\nEach cell with three neighbors will either be populated or survive.\n"
			    + "\nEach cell with four or more neighbors dies by overpopulation.\n"
			    + "\nEach cell that ages over ten generations dies.\n" + colors.end)

#Main driver code
def main(argv):
#Creating empty 20 x 20 grid of 2-element lists
#Each list contains field for population status and organism age
	grid = [[ [0, 0] for i in range (0,20)] for j in range (0,20)]

#Setting generational death, defaults to 'on'
	genDeath = 1

#Otherwise, get options from command line and perform associated tasks
'''
Valid command line options:
-g	disables generational death
-f	gets initial grid from given file
--help  prints help menu
'''
	else:

	#Getting command-line options, if invalid options are given print error and exit
		try:
			opts, args = getopt.getopt(argv, "f:g", "help")

		except getopt.GetoptError:
			print("Invalid command-line option, use --help")
			sys.exit()
	
	#Performing associated task for each option
		for opt, arg in opts:
			if (opt == '-g'):
				genDeath = 0

			if (opt == '--help'):
				printHelp()

			elif (opt == '-f'):
				getGrid(grid, arg)

		#If '-f' is not given, randomize grid
			else:
				randGrid(grid)

#Printing start menu and getting input for number of generations
	printMenu()
	
	numGens = input(colors.red + "How many generations would you like to simulate? (min 0) " + colors.end)

#Printing initial colony state	
	print(colors.cyan + "\nInitial colony prior to evolution" + colors.end)
	print("**************************************")
	printGrid(grid)

#Simulated input number of generations and printing status of each	
	x = 1	
	while (x <= int(numGens)):
		grid = evoSim(grid, genDeath)
		print(colors.cyan + "Colony after " + colors.yellow + str(x) + colors.cyan + " generation(s)" + colors.end)
		print("****************************************\n")
		printGrid(grid)
		x += 1

#Running main driver code
main(sys.argv[1:])
