fileName = "../data-ec/day6-input.csv"

def readAnswers(fileName):
    file = open (fileName)
    lines = file.read().split('\n\n')
    file.close()
    answers = [line.replace('\n', '') for line in lines]
    
    return (answers)

def countAnswers(line):
    numAnswers = len(set(line))

    return (numAnswers)

def main(fileName):
    answers = readAnswers(fileName)
    sumAnswers = 0
    for answer in answers:
        sumAnswers += countAnswers(answer)
    
    print ("Total sum of answers: ", sumAnswers)

if __name__ == "__main__":
    import sys

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day6-input.txt" 

    main(fileName)
