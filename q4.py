def statDec(func):
    """
    Functionality: decorator to print line information
    
    Input Argument: func(function) - function to be decorated
    Returns: inner function
    """
    def inner(t):
        # Execute function and retrieve list of fileLines
        fileLines = func(t)
        # Iterate over each line and print data
        for line in fileLines:
            # use comprehension to create the list of numebrs for each line
            numList = [int(num) for num in line.split()]
            # Print statistics for the current line
            print("Numbers read:", numList)
            print("Count of numbers read:", len(numList))
            print("Average of numbers:", sum(numList) / len(numList))
            print("Maximum number:", max(numList), "\n")
    return inner

@statDec
def printStats(t):
    """
    Functionality: Retrieves data from text file t to read lines of numbers,
                   for each line read this function will call decorator function statDec which prints line information
    
    Input Argument: t(txt file) - input file to read from
    Returns: list of lines read from the file
    """

    # open the file, get file lines, close file and return file lines
    f = open(t, "r")
    fileLines = f.readlines()
    f.close()
    return fileLines

printStats("q4.txt")
