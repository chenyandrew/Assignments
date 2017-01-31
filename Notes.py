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
            employee_list = []
            for i in range(num):
                NextList = []
                cubicle_area = 0
                nextLine = file.readline()
                nextLine = nextLine.strip()
                nextLine = nextLine.split()

                count = 0
                for entity in nextLine:
                    if count >= 1:
                        NextList.append(int(entity))
                    else:
                        NextList.append(entity)
                        employee_list.append(entity)
                    count += 1

                for i in range(NextList[2], NextList[4]):
                    for j in range(NextList[1], NextList[3]):
                        if Grid[i][j] != 0:
                            Grid[i][j] = 2
                        else:
                            Grid[i][j] = NextList[0]
                            cubicle_area += 1


            unallocated = 0
            contested = 0
            for i in range(len(Grid)):
                for j in range(len(Grid[i])):
                    if Grid[i][j] == 0:
                        unallocated += 1
                    elif Grid[i][j] == 2:
                        contested += 1
            print("Unallocated", unallocated)
            print("Contested", contested)

            for k in range(len(employee_list)):
                count = 0
                for i in range(len(Grid)):
                    for j in range(len(Grid[i])):
                        if Grid[i][j] == employee_list[k]:
                            count += 1
                print(employee_list[k], count)

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
