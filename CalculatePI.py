#  File: CalculatePI.py

#  Description: Calculating PI via dart board

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/12/2016

#  Date Last Modified: 10/13/2016

import math
import random

def computePI (numThrows):

    #counter for darts landing inside the circle
    dart_in = 0
    for i in range(numThrows):

        #random generator for darts shot
        xPos = random.uniform(-1.0, 1.0)
        yPos = random.uniform(-1.0, 1.0)

        #determining if dart landed inside the circle
        distance = math.hypot(xPos, yPos)
        if distance < 1:
            dart_in += 1

    pi = (dart_in * 4)/numThrows

    return pi

def main():

    computations = [100, 1000, 10000, 100000, 1000000, 10000000]
    print("Computation of PI using Random Numbers")
    print(" ")
    for i in computations:
        pi = computePI(i)
        ratchet = round((computePI(i) - math.pi), 6)

        #adjusting calculations to appropriate decimal place
        if len(str(pi)) <= 8:
            pi = format(pi, '.6f')
        if ratchet >= 0:
            ratchet = "+" + str(ratchet)

        #printing the proper formatting, adjusted string formatting to account for spaces
        print('{:<16}'.format("num = " + str(i)),
              '{:<26}'.format("Calculated PI = " + str(pi)),
              "Difference = ", str(ratchet))

    print(" ")
    print("Difference = Calculate PI - math.pi")

main()
