#  File: CreditCard.py

#  Description: credit card validator based on Luhn's test

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 512000

#  Date Created: 11/16/2016

#  Date Last Modified: 11/17/2016

def main():

    # taking in creditcard number as an int
    creditcard = int(input("Enter 15 or 16-digit credit card number: "))

    creditcard = str(creditcard)
    number = len(creditcard)

    # calling for card test, card type, and printing error/validity
    if number == 15 or number == 16:
        if is_valid(creditcard):
            print(" ")
            print(cc_type(creditcard))
        else:
            print(" ")
            print("Invalid credit card number")
    else:
        print(" ")
        print(error_message(number))

# This function checks if a credit card number is valid
def is_valid(cc_num):

    # lists for the Luhn's test
    cc_test = []
    cc_test2 = []

    # creating range
    number = len(cc_num)

    # appending to the lists to get ready for summation
    if number == 16:
        for i in range(number):
            if (i % 2 == 0) or (i == 0):
                cc_test.append(2 * int(cc_num[i]))
            else:
                cc_test.append(int(cc_num[i]))
        for j in range(number):
            if cc_test[j] > 9:
                cc_test2.append(cc_test[j] - 9)
            else:
                cc_test2.append(cc_test[j])
    if number == 15:
        for i in range(number):
            if i % 2 != 0:
                cc_test.append(2 * int(cc_num[i]))
            else:
                cc_test.append(int(cc_num[i]))
        for j in range(number):
            if cc_test[j] > 9:
                cc_test2.append(cc_test[j] - 9)
            else:
                cc_test2.append(cc_test[j])

    # summation for Luhn's test
    totalsum = sum(cc_test2)

    # cc_num validity based on Luhn's test
    if totalsum % 10 == 0:
        return True
    else:
        return False

# This function returns the type of credit card
def cc_type(cc_num):

    # lists used to condense some of the MII
    AmEx = ["34", "37"]
    MasterCard = ["51", "52", "53", "54", "55"]

    if cc_num[0:2] in AmEx:
        return "Valid American Express credit card number"
    if cc_num[0:4] == "6011" or cc_num[0:3] == "644" or cc_num[0:2] == "65":
        return "Valid Discover credit card number"
    if cc_num[0:2] in MasterCard:
        return "Valid MasterCard credit card number"
    if cc_num[0] == "4":
        return "Valid Visa credit card number"
    else:
        return "Valid credit card card number"

# error message as a return statement
def error_message(cc_num):

    if cc_num != 15 or cc_num != 16:
        return "Not a 15 or 16-digit number"

main()