def readAnswersPartA(fileName):
    file = open (fileName)
    lines = file.read().split('\n\n')
    file.close()
    answers = [line.replace('\n', '') for line in lines]
    
    return (answers)


def countAnswers(line):
    numAnswers = len(set(line))

    return (numAnswers)


def solvePartB(fileName):
    file = open (fileName)
    lines = file.read().split('\n')
    file.close()

    sumAnswers = 0
    end = len(lines)
    previousString = set(lines[0])
    
    for i in range(end-1):
        nextString = set(lines[i+1])

        if nextString:
            previousString = previousString.intersection(nextString)
        else:
            sumAnswers += len(previousString)
            previousString = set(lines[i+2])
        
    sumAnswers += len(previousString)
    
    return (sumAnswers)
       

def main(fileName):
    answers = readAnswersPartA(fileName)
    sumAnswers = 0
    for answer in answers:
        sumAnswers += countAnswers(answer)

    print ("Total sum of answers, part a: ", sumAnswers)
    
    answerB = solvePartB(fileName)
    print ("Total sum of answers, part b: ", answerB)

if __name__ == "__main__":
    import sys

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day6-input.txt" 

    main(fileName)
