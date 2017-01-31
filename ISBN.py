#  File: ISBN.py

#  Description: ISBN validator

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/30/2016

#  Date Last Modified: 10/31/2016

def main():

    #open the file to read and the file to write
    isbnfile = open("isbn.txt", "r")
    isbnout = open("isbnOut.txt", "w")

    #counting the number of lines
    lines = len(isbnfile.readlines())

    #starting list count over
    isbnfile.seek(0)

    #performing loop for each line
    for i in range(lines):

        #setting lists to perform parital sums onto
        nums_add = []
        sum1list = []
        sum2list = []

        #counters to accumulate sum
        summation1 = 0
        summation2 = 0

        #reading line per iteration of loop
        text = isbnfile.readline()
        text = text.strip()

        #storing original list for proper format onto new text file
        origtext = text

        #considering both 'X' and 'x' cases as well as replacing hyphens with spaces
        text = text.upper()
        text = text.replace("-", "")

        #appending each index of the string to the list
        for j in range(len(text)):
            if text[j] in "0123456789":
                nums_add.append(text[j])

            #changing X to 10 if present in the end for list to sum partially
            if text[j] == "X":
                nums_add.append(10)

        #calling method to determine if the ISBN is in consideration for valid ISBN
        if is_valid(text):
            for k in range(len(nums_add)):
                summation1 += int(nums_add[k])
                sum1list.append(summation1)
            for h in range(len(sum1list)):
                summation2 += int(sum1list[h])
                sum2list.append(summation2)

            #determining if ISBN is valid
            if int(sum2list[-1]) % 11 == 0:
                isbnout.write(origtext + "  valid" + "\n")
            else:
                isbnout.write(origtext + "  invalid" + "\n")
        else:
            isbnout.write(origtext + "  invalid" + "\n")


    #completion of closing the file to read and the file to write
    isbnout.close()
    isbnfile.close()


#determining whether the length of the list is potentially a valid ISBN
def is_valid(text):

    if len(text) != 10:
        return False

    # X can only be present at the end IF at all present
    if "X" in text[0:-1]:
        return False
    else:
        return True



main()



