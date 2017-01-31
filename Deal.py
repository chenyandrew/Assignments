# File: Deal.py

# Description: Simulating Let's Make A Deal game

# Student Name: Andrew Chen

# Student UT EID: ayc453

# Course Name: CS 303E

# Unique Number: 51200

# Date Created: 10/20/2016

# Date Last Modified: 10/21/2016

import random

def main():

    #prompt user to determine times want to play
    times_play = int(input("Enter number of times you want to play: "))
    print(" ")

    #creating the printed list and centering with appropriate brute forced formatting
    tableview = "Prize      Guess       View    New Guess"
    print(tableview.center(43))

    #referencing variables before assignment
    switch_n_win = 0
    new_guess = 0
    view = 0

    #loop to run each instance of the game
    for i in range(1, times_play + 1):
        player_guess = random.randint(1,3)
        prize_door = random.randint(1,3)

        #nested to determine view by distinguishing itself from prize and guess
        for j in range(1,4):
            if (j == prize_door) or (j == player_guess):
                pass
            else:
                view = j

            #switching and obtaining new guess
            for k in range(1,4):
                if (k == player_guess) or (k == view):
                    pass
                else:
                    new_guess = k
        #count to find times won by switching
        if (prize_door == new_guess):
            switch_n_win += 1

        #printing each instance with brute-forced appropriate spacing
        print("   ", prize_door, "        ", player_guess,
              "        ", view, "        ", new_guess)

    #formulas to find probability to win by switching
    win_by_switch = format((switch_n_win / times_play), '.2f')
    win_by_not = format((1 - (switch_n_win / times_play)), '.2f')

    print(" ")
    print("Probability of winning if you switch =", win_by_switch)
    print("Probability of winning if you do not switch =", win_by_not)

main()

