import os
import sys
#Adrian Faircloth
#3-21-22
#Lab 7 Part III

#Gets frequency of words in set of positive movie reviews, prints 100 most common words

#Function for getting words from review file and adding to freq dict
def addWords(filename, word_freq):

'''
Gets text from file, removes nonalpha characters except spaces,
Creates list of words in review, removes stop words or words w/ len < 4.
For each word in resulting list, if word is a key in word_freq, increment value by 1.
Else, add key to word_freq w/ value of 1.
'''

#Building path to reviews folder and list of stop words
	path = os.getcwd() + '/reviews/'
	stopWords = [
		 'this', 'that', 'take', 'want', 'which', 'than', 'then',
		 'will', 'with', 'have', 'after', 'such', 'when', 'some',
		 'them', 'could', 'make', 'though', 'from', 'were', 'also',
		 'into', 'they', 'their', 'there', 'because']

#Opening file from reviews folder
	try:
		infile = open(path + filename, "r")
	except FileNotFoundError:
		print("Error opening file")
		sys.exit()

#Reading in text from review file and closing file
	fileText = infile.read()
	infile.close()

#Getting string of only alphabet chars and spaces from review text and making all words lowercase
	revText = ''.join(ch for ch in fileText if (ch.isalpha() or ch.isspace()))
	revText = revText.lower()

#Tokenizing all words from edited review string
	revWords = revText.split()

#Removing all stop words and words of len < 4
	for word in list(revWords):
		if (word in stopWords or len(word) < 4):
			revWords.remove(word)

#Updating word_freq for each remaining word
#If word is in word_freq, inc. value by 1
#Else, add word to word_freq w/ value of 1
	for word in revWords:
		if (word in word_freq.keys()):
			word_freq[word] += 1
		else:
			word_freq[word] = 1

#Main driver code
def main():
#Initializing word_freq dictionary
	word_freq = {}

#For each file in review folder, if score at end of filename is positive (6 or higher),
#add frequency of each non-stop word into word_freq
	path = os.getcwd() + '/reviews'
	for filename in os.listdir(path):
			if (int(filename[-5]) > 5):
				addWords(filename, word_freq)

#Building list of all words in word_freq sorted in descending order by frequency
	wordList = []
	for word in sorted(word_freq, key=word_freq.get, reverse = True):
		wordList.append(word)

#Printing out top 100 most common words w/ 10 words per line
	print("Top 100 Words Used in Positive Movie Reviews")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	for i in range(0, 10):
		for j in range(0, 10):
			print(wordList[(i * 10) + j], end = '  ')
		print("")

#Running main driver code
main()
