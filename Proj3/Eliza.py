import random
#Adrian Faircloth
#4-6-22
#Eliza the Chatbot
#Chatbot that takes user input and responds based on keywords
#Utilizes simple form of natural language processing

#Class for chatbot
class Dialogue:
#Initialization function
	def __init__(self, filename):
	#Var for keyword/response filename
		self.filename = filename
	#Dictionary for storing key-response sets in one-to-many relation
		self.responseDict = {}
	#Var for storing raw input string in case response needs part of input
		self.rawInstring = ""
	#Set of key phrases for checking in input
		self.keyPhrases = {
				   "i'm",
				   "what's up",
				   "i feel",
				   "i think",
				   "i am",
				   "i hate"
				  }
	#Set of stopwords to remove from input string
		self.stopWords = {
				  "this",
				  "that",
				  "take",
				  "want",
				  "which",
				  "then",
				  "than",
				  "will",
				  "with",
				  "have",
				  "after",
				  "such",
				  "when",
				  "some",
				  "them",
				  "could",
				  "make",
				  "through",
				  "from",
				  "where",
				  "also",
				  "into",
				  "they",
				  "their",
				  "there",
				  "they're",
				  "because"
				 }

#Function for getting keywords and responses from input file

#After '#' line is found, next line is keyword, and each line after
#until '#' is a response.
#Gets keyword as string and responses as list, stored as key-value pair in dictionary.
#For responses w/ multiple keywords, splits each keyword into separate
#entry in dictionary.

	def getKeysAndResponses(self):

	#Reading input file line-by-line
		infile = open(self.filename, 'r')
		textLines = infile.readlines()
		infile.close()

	#Initializing response list	
		responses = []
	
		while (textLines):
		#Getting first keyword from top of file & stripping newline/whitespace	
			key = textLines.pop(0).strip('\n')
			key = key.strip()	

		#While top line is not '#', line is response, so pop and add to response list
			while (textLines[0] != "#\n"):
				responses.insert(0, textLines.pop(0).strip('\n').strip())
	
		#If keyword line has multiple keys separated by '|', make dict entry for each subkey
			if (key.rfind('|') != -1):
				subkeys = key.split('|')
				for subkey in subkeys:
					self.responseDict.update( {subkey : responses.copy()} )
		#Else make single entry for keyword
			else:
				self.responseDict.update( {key : responses.copy()} )

		#Clear response list and pop '#' line to reset for next run of loop
			responses.clear()
			textLines.pop(0)

#Function for cleaning input string
#Removes non alphanumeric characters besides spaces, and removes stopwords
	def cleanString(self, instring):

	#Removes every non-alphanumeric and non-space character
		for char in instring:
			if ((char.isalnum() or char.isspace()) == False):
				instring = instring.replace(char, "")

		#Storing input string w/ extra characters removed, still has stopwords
			self.rawInstring = instring
	
	#Getting list of words in input string
		inwords = instring.split()

	#Removind words from input string if they are stopwords
		for word in inwords:
			if word in self.stopWords:
				instring = instring.replace(word, "")
				instring.strip()
		return instring

#Function for getting clean user input
#Gets input in lowercase and cleans input string
	def getInput(self):

	#Getting input from user and setting to lowercase
		instring = input("- ")	
		instring = instring.lower()
	
	#Calling cleanString method to remove certain characters/stopwords
		instring = self.cleanString(instring)
		return instring

#Function for getting first keyword/keyphrase from input string
#First, gets first singular keyword
#Next, checks for keyphrase & overrides keyword if found at earlier index than first keyword
	def getKeyword(self, instring):

	#Initializing keyword to 'no match' keyword
		keyword = "__NO_MATCH__"

	#Getting list of words in input string
		inwords = instring.split()

	#Initializing keyword index to large value in case no singular keyword is found
		keyIndex = 9999
	#If a word from input string is a response key, store word & index and break loop
		for word in inwords:
			if word in self.responseDict.keys():
				keyword = word
				keyIndex = instring.index(word)
				break

	#If a keyphrase is found in the input string, store phrase and break loop
	#Keyphrase will override previous keyword if found at index earlier in string than found keyword
		for key in self.keyPhrases:
			if key in instring and instring.index(key) < keyIndex:
				keyword = key
				break
		
		return keyword		

#Function for getting random response from list tied to keyword
#If response requires part of user input, pull from rawInstring
	def getResponse(self, keyword):

	#Gettting list of relevant responses from dictionary
		responseList = self.responseDict[keyword]

	#Choosing random response from response list
		response = random.choice(responseList)

	#If response contains an asterisk, replace w/ part of user input after keyword
		if (response.find('*') != -1):

		#Splitting raw user input at keyword
			insplit = self.rawInstring.split(keyword)

		#Getting part of input after keyword and stripping whitespace
			deepPart = insplit[1].strip()

		#Replacing asterisk with deep part of user input
			response = response.replace('*', deepPart)
		return response
		
	 
#Main driver code
#Runs chatbot indefinitely until 'bye' keyword is found
def main():

#Initializing Dialogue object w/ filename for dialogue text
	filename = 'dialogue.txt'
	dialog = Dialogue(filename)

#Building key-response dictionary from file
	dialog.getKeysAndResponses()

#Infinite loop until 'bye' keyword is found

#Gets user input
#Parses out non-alnum characters/stopwords
#Finds first keyword/keyphrase
#If keyword is 'bye' then exit
#Selects random associated response & prints


	while (True):

	#Getting cleaned user input
		inp = dialog.getInput()

	#Getting keyword from input
		keyword = dialog.getKeyword(inp)

	#If keyword is 'bye' break loop
		if (keyword == "bye"):
			break
	#If not, print response and repeat
		print(dialog.getResponse(keyword))

#Running main driver code
main()
