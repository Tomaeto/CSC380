#Adrian Faircloth
#02/05/22
#Project 1: Game of NIM

#Program for running a game of NIM against an AI with reinforcement learning
#Computer player pulls unsafe states from file and avoids those states, adding more when
#	a state can lead to a logged unsafe state


#Function for running NIM game
def playGame(piles, start):

	#Opening unsafe move file in read+ mode, allows writing to file
	move_file = open("unsafe", "r+")

	#Loop for playing NIM
	#While the piles are not all empty, play game
	while(True):

		allUnsafe = []
		#Getting all unsafe moves from file, moves file pointer to end
		#Builds list of all unsafe states
		for line in move_file:
			allUnsafe.append(line)
	
		#Moving file pointer back to start for writing
		move_file.seek(0)

		#If player chose machine to start, skip player's move once
		if (start == 0):
			start = 1

		#Otherwise, run player's move
		else:

		#Getting user input for pile and amount of tokens to take
			move = input("\nEnter pile letter and number of chips to take: ")
			pile = ord(move[0]) - 65
			take = int(move[2])

		#If user input is invalid, print error message and reprompt user until input is valid
			while (not checkMove(piles, pile, take)):
				print("Letter or number out of range!")
				move = input("\nEnter pile letter and number of chips to take: ")
				pile = ord(move[0]) - 65
				take = int(move[2])

		#Apply player's chosen move
			piles[pile] -= take;

		#Printing updated state of the piles
			print("\nCurrent size of each pile:")
			print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2], "\n")

		#If all piles are empty, player lost, so print message and exit
			if (piles[0] + piles[1] + piles[2] == 0):
					print("You lose!")
					break
		
		#Otherwise, run machine's move

		#Getting list of possible unsafe states from current state
		unsafeList = checkUnsafe(piles, allUnsafe)
		

		#If there are unsafe moves, save new unsafe states and make safe move
		if (len(unsafeList) != 0):
		
			#Adding new unsafe states to list
			allUnsafe = addUnsafe(piles, allUnsafe)
		
			#Overwriting unsafe file w/ updated list of unsafe moves
			for line in allUnsafe:
				move_file.write(line)

			#Resetting file pointer for next read
			move_file.seek(0)

		#Getting computer's move as list containting pile number and take count
		move = []
		move = getCompMove(piles, unsafeList)

		#Printing computer's move
		print("\nI take", move[1], "from pile", chr(move[0] + 65), "\n")
		
		#Playing computer's move
		piles[move[0]] -= move[1]

		#Printing updated piles
		print("\nCurrent size of each pile:")
		print("A:", piles[0], "\tB:", piles[1],"\tC:", piles[2], "\n")

		#If all piles are empty, computer lost, so print message and exit
		if (piles[0] + piles[1] + piles[2] == 0):
			print("You won!!")
			break

#Function for checking if a move is valid
def checkMove(piles, pile, take):

	'''
	If chosen pile and amount to take are in range 
	and not greater than current pile size, return true.
	Else, return false.

	Ensures pile size never becomes < 0.
	'''

	if ( pile in range(0,3) and take in range(1,4) ):
		if (piles[pile] >= take):
			return True
		else:
			return False
	else:
		return False


#Function for finding all unsafe states possible from current state
#Checks if any possible moves result in an unsafe state
#Returns list of all possible unsafe states
def checkUnsafe(piles, unsafe):

	#Initializing empty list for unsafe states
	unsafeList = []

	'''
	For each pile, check each possible move (taking 1 - 3 tokens)
	and check if the resulting state is in the string of unsafe states.
	If yes, add the unsafe state to the list.

	Returned list is used to check if there are any unsafe moves and avoiding
	possible unsafe moves, list is a subset of allUnsafe list and results in faster
	checks for unsafe moves from current state.
	'''

	#Loop for checking possible moves taking from each pile
	for i in range (3, 0, -1):
		for j in range (0, 3):

			#Taking up to 3 tokens from a pile
			nextTake = piles[j] - i

			#If taken amount exceeds pile size, set size to 0
			if (nextTake < 0):
				nextTake = 0

			#Build string for possible next state based on pile taken from
			if (j == 0):
				checkStr = str(nextTake) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"

			elif (j == 1):
				checkStr = str(piles[0]) + " " + str(nextTake) + " " + str(piles[2]) + "\n"

			elif (j == 2):
				checkStr = str(piles[0]) + " " + str(piles[1]) + " " + str(nextTake) + "\n"

			#If next state is in neither the list of all unsafe moves or list of next unsafe moves, add to the latter
			if (unsafe.count(checkStr) > 0 and unsafeList.count(checkStr) == 0):
				unsafeList.append(checkStr)

	#Returning list of possible unsafe states based on current state
	return unsafeList

#Function for adding unsafe states to list of unsafe moves			
def addUnsafe(piles, unsafe):
	
	'''
	For each pile, build string of possible previous states (adding 1 to 3 to each).
	These are also unsafe states, so add them to unsafe list if they are not in that list.
	State strings end w/ '\n' so state file contains line breaks for reading in states by line.
	Return sorted unsafe list for overwriting unsafe state file.
	'''
	
	#Adding current pile state to list if it is not in list already
	#Current state should only be in list if there were no safe moves to make
	unsafeMove = str(piles[0]) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"

	if (unsafe.count(unsafeMove) == 0):
		unsafe.append(unsafeMove)

	#Loop for adding each possible previous state to unsafe list
	for i in range (1, 4):
		for j in range (0, 3):
			#Adding b/w 1 and 3 to a pile
			prevState = piles[j] + i

			#Building string for possible previous state based on pile added to
			if (j == 0):
				unsafeMove = str(prevState) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"

			elif (j == 1):
				unsafeMove = str(piles[0]) + " " + str(prevState) + " " + str(piles[2]) + "\n"

			elif (j == 2):
				unsafeMove = str(piles[0]) + " " + str(piles[1]) + " " + str(prevState) + "\n"

			#If previous state is not in unsafe list, add it to list
			if (unsafe.count(unsafeMove) == 0):
				unsafe.append(unsafeMove)

	#Sorting list of unsafe moves and returning
	unsafe.sort()
	return unsafe

#Function for determining computer player's move
def getCompMove(piles, unsafeList):
	
	'''
	For each pile, check if taking up to three tokens is a valid move.
	If the unsafeList is empty, add pile num and take num to move and return.
	If unsafeList is not empty, build string for possible next pile state based on
	the pile comp is trying to take from and check if that string is in unsafeList.
	If no, move is safe, so add pile num and take num to move and return.

	If no safe moves are found, simply find a viable move and return,
	'''
	#Initializing list for storing computer's chosen pile and take size
	move = []

	#Loop for checking for safe move with given unsafe move list
	for i in range (3, 0, -1):
		for j in range (0, 3):

			#If move is not valid, pass this run of the loop
			if (not checkMove(piles, j, i)):
				pass
			else:
				#If unsafeList is empty, move is safe, so return pile num and take num
				if (len(unsafeList) == 0):
					move.append(j)
					move.append(i)
					return move
				else:

				#If unsafe list is not empty, create str for possible next state
					if (j == 0):			
						nextState = str(piles[0] - i) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"

					elif (j == 1):
						nextState = str(piles[0]) + " " + str(piles[1] - i) + " " + str(piles[2]) + "\n"

					elif (j == 2):
						nextState = str(piles[0]) + " " + str(piles[1]) + " " + str(piles[2] - i) + "\n"

				#If next state is not in unsafe list, return pile num and take num
					if (unsafeList.count(nextState) == 0):
						move.append(j)
						move.append(i)
						return move

	#Loop for just finding a valid move if no safe moves were found
	for i in range(3, 0, -1):
		for j in range(0, 3):
			if (checkMove(piles, j, i)):
				move.append(j)
				move.append(i)
				return move
#Main driver code
def main():

	#Getting user input for starting pile sizes
	sizes = input("Enter initial sizes for piles A B C: ")

	#Creating list of ints from user input
	piles = list( map(int, sizes.split(' ')) )

	while (piles[0] < 1 or piles[1] < 1 or piles[2] < 1):
		print("Invalid starting pile sizes")
		sizes = input("Enter initial sizes for piles A B C: ")
		piles = list( map(int, sizes.split(' ')) )

	#Printing initial pile sizes
	print("\nSize of each pile initially")
	print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2])

	#Getting user input for starting player
	start = int( input(("\nType 0 if the MACHINE starts, or 1 if YOU start: ")) )

	#Running game
	playGame(piles, start)

#Running program	
main()
