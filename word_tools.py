#do we have to open file at the beginning of each function
#or is there an order to how we should test the program
#for example, if we wanted to exploreWord, then do we have to learnFile first
#or is there a default file that we upload to the actual program

"""
Program: word_tools.py

The purpose of this program is to allow the user to input a set of words (both 
manually and via file input) and then to search within that space of words for
single-insertion, single-deletion, single-substitution, and anagram
adjacencies. Further, the user can provide two words and search for a word
ladder (a series of single-substitution steps) that connects them.
"""

import re   # re.sub needed when processing input files
import os   # os.path.exists needed when checking for input files

# the set of known words is a global in this program, as nearly every function
#   interacts with it

def main():
    """Takes user input and executes it until receiving the QUIT command."""
    while True:
        userInput = input(">> ")
        upperTokens = userInput.upper()
        inputTokens = upperTokens.split(" ")
        command = inputTokens[0]
        
        if command == "QUIT":
            print("")
            break
            
        elif command == "LEARNFILE":
            inputFilePath = inputTokens[1]
            learnFileWords(inputFilePath)
        
            
        elif command == "LEARN":
            newWordList = inputTokens[1:]
            learnWords(newWordList)
                
        elif command == "FORGET":
            unwantedWordList = inputTokens[1:]
            unlearnWords(unwantedWordList)
            
        elif command == "EXPLORE":
            searchWord = inputTokens[1]
            exploreWord(searchWord)
            
                    

        elif command == "LADDER":
            word1 = inputTokens[1]
            word2 = inputTokens[2]
            findLadder(word1,word2)
            
        else:
            print(f"I don't know the command {command}.")
            printHelp()
            
def printHelp():
    """Prints all commands the program's prompt recognizes. Should be called when the user provides an invalid command."""
    print("I understand the following commands:")
    print("QUIT: Exit the program")
    print("LEARNFILE [filepath]: Add every word in the file at [filepath] to my known words.")
    print("LEARN [word] [word] ...: Add one or more specified words to my known words.")
    print("FORGET [word] [word] ...: Remove one or more specified words from my known words.")
    print("EXPLORE [word]: List all known words separated from [word] by one insertion, deletion, substitution, or by rearrangement.")
    print("LADDER [word1] [word2]: Find a word ladder (of length up to 8) connecting two words, using only single-letter substitutions.")

def learnFileWords(inputFilePath):
    """
    *Opens a file
    *For each line:
        *Substitutes all groupings of one or more hyphens with a single space
        *Substitutes all groupings of one or more spaces or tab characters with a single space
        *Substitutes all remaining characters that are not letters or spaces with an empty string
        *Adds all space-separated words to a set of words found in the file
    *Adds all words found in the file to the list of known words, reporting how many were already known
    """
    if os.path.exists(inputFilePath):
        print(f"File {inputFilePath} found.")
        fin = open(inputFilePath, "r")
        nextLine = fin.readline()
        newWordsCounter = 0
        while nextLine:
            oneLine = re.sub("[\n\t\- ]+", " ", nextLine.upper())
            twoLine = re.sub("[^A-Za-z ]", "", oneLine)
            threeLine = twoLine.split(" ")
            while("" in threeLine):
                threeLine.remove("")
            for i in range(len(threeLine)):
                if threeLine[i] not in knownWords:
                    knownWords.add(threeLine[i])
                    newWordsCounter += 1
            nextLine = fin.readline()
        print((str(newWordsCounter - (newWordsCounter - len(knownWords)))) + f" words in {inputFilePath}")
        print(f"{newWordsCounter} previously unknown")
                    
    else:
        print(f"No file {inputFilePath} found.")
    

def learnWords(newWordList):
    """Takes in a list of words and either adds each one to the list of known
    words or reports that it's already known."""
    for i in range(len(newWordList)):
        if newWordList[i] not in knownWords:
            print(f"\"{newWordList[i]}\" learned.")
            knownWords.add(newWordList[i])
        else:
            print(f"I already know the word \"{newWordList[i]}\"")
    

def unlearnWords(unwantedWordList):
    """Takes in a list of words and either removes each one from the list of
    known words or reports that it was already absent."""
    for i in range(len(unwantedWordList)):
        if unwantedWordList[i] not in knownWords:
            print(f"I don't know the word \"{unwantedWordList[i]}\".")
        else:
            knownWords.discard(unwantedWordList[i])
            print(f"\"{unwantedWordList[i]}\" unlearned.")

def substitutionNeighbors(searchWord):
    """Takes in a word and returns the set of all known words that are a single
    letter substitution away from it."""
    potentialWords = []
    actualWords = set()
    for char in range(65, 91):
        for i in range(len(searchWord)):
            newWord = searchWord[:i] + chr(char) + searchWord[i+1:]
            if newWord != searchWord:
                potentialWords.append(newWord)
        for i in range(len(potentialWords)):
            if potentialWords[i] in knownWords:
                actualWords.add(potentialWords[i])
    return actualWords
  
        
    

def insertionNeighbors(searchWord):
    """Takes in a word and returns the set of all known words that are a single
    letter insertion away from it."""
    potentialWords = []
    actualWords = set()
    for char in range(65, 91):
        for i in range(len(searchWord)):
            newWord = searchWord[:i] + chr(char) + searchWord[i:]
            potentialWords.append(newWord)
        for i in range(len(potentialWords)):
            if potentialWords[i] in knownWords:
                actualWords.add(potentialWords[i])
    return actualWords

def deletionNeighbors(searchWord):
    """Takes in a word and returns the set of all known words that are a single
    letter deletion away from it."""
    potentialWords = []
    actualWords = set()
    for i in range(len(searchWord)):
        newWord = searchWord[:i] + searchWord[i+1:]
        potentialWords.append(newWord)
    for i in range(len(potentialWords)):
            if potentialWords[i] in knownWords:
                actualWords.add(potentialWords[i])
    return actualWords

def letterBag(word):
    """Takes in a word and returns a dictionary indicating how many times each
    letter occurs in the word."""
    bag = dict()
    for letter in word:
        if letter not in bag:
            bag[letter] = 1
        else:
            bag[letter] += 1
    return bag


def anagrams(searchWord):
    """Takes in a word and returns the set of all (other) known words that can
    be produced by rearranging its letters. 
    
    Unlike the substitutionNeighbors, insertionNeighbors, and deletionNeighbors
    functions, this function does this by searching the space of known words
    for things that happen to have the property of being an anagram of the
    searchWord, rather than generating the set of words that have the property
    of being an anagram and then checking to see which ones are known words."""
    actualWords = set()
    word = searchWord
    originalDict = letterBag(word)
    for word in knownWords:
        comparedDict = letterBag(word)
        if comparedDict == originalDict and word != searchWord:
            actualWords.add(word)
    return actualWords
    

def exploreWord(searchWord):
    """Takes in a word and, by calling other functions, finds all known words
    which are an insertion, deletion, substitution, or rearrangement away.
    Prints all words in each of these sets."""
    print("Insertions:")
    insertionNeighbors(searchWord)
    for words in insertionNeighbors(searchWord):
        print (words)
    print("\nDeletions:")
    deletionNeighbors(searchWord)
    for words in deletionNeighbors(searchWord):
        print (words)
    print("\nReplacements:")
    substitutionNeighbors(searchWord)
    for words in substitutionNeighbors(searchWord):
        print (words)
    print("\nAnagrams:")
    anagrams(searchWord)
    for words in anagrams(searchWord):
        print (words)

def findLadder(word1,word2):
    """Takes in two words and attempts to find and print a "ladder" of
    single-letter substitutions that connects the two through the space
    of known words. Stops after finding minimum-length paths or after not
    finding any paths of length 8 or less."""
    paths1 = [[word1]]
    paths2 = [[word2]]
    
    full_paths = __findPaths__(paths1,paths2)
    print(f"Ladders {word1}>{word2}")
    for path in full_paths:
        print(">".join(path))

def __findPaths__(paths1,paths2,wordsTraversed1=set(),wordsTraversed2=set(),depth=0,maxDepth=8):
    """Helper function for findLadder."""
    # check if we have a connected path
    fullPaths = []
    for path1 in paths1:
        for path2 in paths2:
            # if the word at the end of a left-side path is equal to the word at the end of a right-side path
            if path1[-1] == path2[-1]:
                # ...flip around the right-side path and connect them as a complete path
                fullPaths.append(path1 + path2[::-1][1:])
    # if we found any complete paths at this depth
    if len(fullPaths) > 0:
        # return all of them, we're done
        return fullPaths
    
    # if we've gone to the maximum depth we're willing to
    if depth > maxDepth:
        # return an empty list, we're done
        return []
        
    # if we're reached this point, we have to expand one of our two word-shells by 1
    
    print(f"Expanding to depth {depth}")
    
    # if it's an even-numbered iteration...
    if depth % 2 == 0:
        # ...expand the shell around word1
        selectedPaths = paths1
        selectedWordsTraversed = wordsTraversed1
    # if it's an odd-numbered iteration...
    else:
        # ...expand the shell around word2
        selectedPaths = paths2
        selectedWordsTraversed = wordsTraversed2
    
    newPaths = []
    newWordsTraversed = set()
    for path in selectedPaths:
        lastWord = path[-1]
        # use substitutionNeighbors to find next steps for each word at the end of the
        #   half-paths we're expanding
        for adjacentWord in substitutionNeighbors(lastWord) - selectedWordsTraversed:
            newPaths.append(path + [adjacentWord])
            newWordsTraversed.add(adjacentWord)
    
    # if it's an even-numbered iteration...
    if depth % 2 == 0:
        # ...store our results back in the left word-shell
        paths1 = newPaths
        wordsTraversed1 = wordsTraversed1 | newWordsTraversed
    # if it's an odd-numbered iteration...
    else:
        # ...store our results back in the right word-shell
        paths2 = newPaths
        wordsTraversed2 = wordsTraversed2 | newWordsTraversed
    
    # make a recursive call to this function, with the expanded shell and our "depth"
    #   variable increased by one 
    return __findPaths__(paths1,paths2,wordsTraversed1,wordsTraversed2,depth+1,maxDepth)
    

if __name__ == "__main__":
    main()
