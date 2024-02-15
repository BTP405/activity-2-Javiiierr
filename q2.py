import matplotlib.pyplot as plt
import math

def graphSnowfall(t):
    """
    Functionality: Retrives data from text file t to display the information in a bar chart,
                   the file will have a single number on each line representing the amount of snowfall for a given day,
                   each value contributes to a particular 10 cm range
    
    Input Argument: t(txt file) - input file to read from
    Returns: creates plot.png
    """

    # open file, read lines, turn lines into numList
    f = open(t, "r")
    fileline = f.readlines()
    numList = [int(num) for num in fileline]

    xData = []
    yData = []

    # find largest number and generate appropriate ranges, append 0 for each y value
    for i in range(0, math.ceil(max(numList) / 10) * 10, 10):
        if i == 0:
           xData.append(str(i) + "-" + str(i+10))
        else:
            xData.append(str(i+1) + "-" + str(i+10))
        yData.append(0)

    # for each number in the numList, add 1 to the proper index 
    for num in numList:
        yData[((int(num)-1)//10)] += 1
   
    # create graph, lable, and export plot
    plt.bar(xData, yData)
    plt.xlabel("Snowfall(cm)")
    plt.ylabel("Num of Occurences")
    plt.title("Accumulated Snowfall")
    plt.savefig("plot.png")

graphSnowfall("q2.txt")