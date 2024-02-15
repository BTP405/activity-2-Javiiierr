def wordCount(t):
    """
    Functionality: Retrives data in a text file to return a dictionary, 
                   the keys are the unique words in the file,
                   the vlaues are a list of line numbers the keys are found in
    
    Input Argument: t(txt file) - input file to read from
    Returns: The dictionary
    """

    # open file and create variables
    f = open(t, "r")
    fileLines = f.readlines()
    linePosition = 0
    wordList = []
    positionList = []

    # loop through each line in the file
    for line in fileLines:
        # update the line position and split the line into words
        linePosition += 1
        lineArr = line.split()
        
        # for each word
        for word in lineArr:
            # add to wordList if it is not already there and create a respsective empty array in positionList
            if word not in wordList:
                wordList.append(word)
                positionList.append([])
            # if the line position is not the respective array for the current word, add it
            if linePosition not in positionList[wordList.index(word)]:
                positionList[wordList.index(word)].append(linePosition)
        
    # close the file and return a dictionary from the 2 lists
    f.close()
    return dict(zip(wordList, positionList))

print(wordCount("q3.txt"))