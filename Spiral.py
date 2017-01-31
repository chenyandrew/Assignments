#  File: Spiral.py

#  Description: finding 3x3 grid of number in a spiral grid

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/20/2016

#  Date Last Modified: 11/21/2016

def createSpiral(num):

    if num == 1:
        return [[1]]
    else:

        # recursive functions for each layer of the square
        spiral = createSpiral(num-2)

        # creating the grid and filling in 0's
        spiral.append([0 for i in range(num)])
        spiral.insert(0,[0 for i in range(num)])
        for i in range(1,num-1):
            spiral[i].append(0)
            spiral[i].insert(0,0)

        # replacing the 0's with the appropriate numbers based on position
        for i in range(num-1):
            spiral[0][num-1-i] = (num**2) - (0*(num-1)) - i
            spiral[i][0] = (num**2) - (1*(num-1)) - i
            spiral[num-1][i] = (num**2) - (2*(num-1)) - i
            spiral[num-1-i][num-1] = (num**2) - (3*(num-1)) - i
        return spiral

def main():

    # prompting user for inputs
    dim = int(input("Enter Dimension: "))
    num = int(input("Enter the number in spiral: "))
    print(" ")

    # error checking for even number dimension, number on edge,
    # or out of range of grid
    if dim % 2 == 0:
        dim = dim + 1
    if num in range(((dim**2)-(((dim-1)*4)-1)), dim**2 + 1):
        print("Number on Outer Edge")
        return
    if num > (dim**2):
        print("Number not in Range")
        return

    # calling function to create spiral based on dimensions
    spiral = createSpiral(dim)
    for i in range(len(spiral)):
        print(spiral[i])
    # finding the position and row the number is in
    for i in range(len(spiral)):
        if num in spiral[i]:
            position = spiral[i].index(num)
            tier = i

    # creating 3x3 grid for answer
    answer = []
    for i in range(3):

        # appending each layer of the 3x3 to the answer array
        answer.append(spiral[tier-1+i][position-1:position+2])

    # printing out the 3 lists in the 3x3 format
    for i in range(len(answer)):
        print(answer[i])

main()
