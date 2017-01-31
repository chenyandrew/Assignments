import timeit

def main():


    file = open("sample.in", "r")

    for lines in file:
        NewList = []
        line = lines.strip()
        line = line.split()
        for word in line:
            NewList.append(word)

        if len(NewList) == 2:
            Total = int(NewList[0]) * int(NewList[1])
            print("Total", Total)
            Grid = makeGrid(int(NewList[0]), int(NewList[1]))
        elif len(NewList) == 1:
            num = int(NewList[0])
            stringPrintList = []
            intPrintList = []
            for person in range(num):
                nextLine = file.readline()
                nextLine = nextLine.strip()
                nextLine = nextLine.split()

                for i in range(1,len(nextLine)):
                    nextLine[i] = int(nextLine[i])

                count = 0
                for i in range(nextLine[2], nextLine[4]):
                    for j in range(nextLine[1], nextLine[3]):
                        if Grid[i][j] == 0:
                            Grid[i][j] = nextLine[0]
                            count += 1
                        else:
                            Grid[i][j] = 2
                stringPrintList.append(nextLine[0])
                intPrintList.append(count)
                print(nextLine[0],count)

            extra = ['unallocated','contested']
            for word in extra:
                stringPrintList.append(word)


            unallocated = 0
            contested = 0
            for i in range(len(Grid)):
                for j in range(len(Grid[i])):
                    if Grid[i][j] == 0:
                        unallocated += 1
                    elif Grid[i][j] == 2:
                        contested += 1

            for i in range(len(stringPrintList)):
                print(stringPrintList[i],intPrintList[i])

            print("Unallocated", unallocated)
            print("Contested", contested)
            print(" ")

    file.close()



def makeGrid(x, y):

    Grid = []
    for i in range(y):
        Grid.append([])
    for i in range(len(Grid)):
        for j in range(x):
            Grid[i].append(0)

    return Grid

main()
