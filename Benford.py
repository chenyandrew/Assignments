#  File: Benford.py

#  Description: proving Benford's law in Census 2009

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/23/2016

#  Date Last Modified: 11/24/2016

def main():

    # create an empty dictionary
    pop_freq = {}

    # open file for reading
    in_file = open ("Census_2009.txt", "r")


    # read the header and ignore
    header = in_file.readline()

    total = 0
    # read subsequent lines
    for line in in_file:

        line = line.strip()
        pop_data = line.split()

        # get the last element that is the population number
        pop_num = pop_data[-1]

        key = int(pop_num[0])
        if (key in pop_freq):
            cvalue = pop_freq[key]
            pop_freq[key] = cvalue + 1
        else:
            pop_freq[key] = 1

        total += 1

    # close the file
    in_file.close()

    # write out the results
    # printing out proper spacing
    print('{0: <7}'.format("Digit"),
          '{0: <7}'.format("Count"),
          "%")

    # printing out the dictionary entries for frequency
    # relative frequency achieved by key-value by total
    for key in pop_freq:
        percentage = "{:.1%}".format(pop_freq[key] / total)
        print('{0: <7}'.format(key),
              '{0: <7}'.format(pop_freq[key]),
              percentage)



main()