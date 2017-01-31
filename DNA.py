#  File: DNA.py

#  Description: Finding longest common sequence between a pair of DNA strands

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/25/2016

#  Date Last Modified: 10/27/2016

def main():
    print(" ")
    print("Longest Common Sequences")
    print(" ")
    #open the file of choice for reading
    dna_file = open("dna.txt", "r")

    #reading each line to determine number of pairs

    pairs = dna_file.readline()
    pairs = pairs.strip()
    pairs = int(pairs)


    #read each pair of strand
    for i in range(pairs):

        st1 = dna_file.readline()
        st2 = dna_file.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        #order strands by size
        if len(st1) > len(st2):
            dna1 = st1
            dna2 = st2
        else:
            dna1 = st2
            dna2 = st1

        # grabbing each substring in lesser dna strand
        wnd = len(dna2)

        #set flag to break when longest sequence is found
        found = False

        #counter and list made to keep track of substrings in main string
        count = 0
        matched = []

        #window truncation with each loop run
        while (wnd > 1):

            #shifting the window
            start_idx = 0
            while (start_idx + wnd) <= len(dna1):
                substring = dna1[start_idx:start_idx + wnd]

                #check if it is in dna2
                for j in range(len(dna2)):
                    if (substring == dna2[j:j+wnd]):
                        matched.append(substring)
                        count += 1
                        found = True
                start_idx += 1

            #decrease size of wnd
            if found:
                break
            else:
                wnd -= 1

        #setting num to print proper string
        num = str(i + 1)
        num = num + ":"

        #printing the results with proper spacing to match required format
        if matched == []:
            print("Pair", num, "No Common Sequence Found")
        else:
            print("Pair", num, matched[0])

        for j in range(1, len(matched)):
            print("        " + matched[j])
        print(" ")

    dna_file.close()

main()

