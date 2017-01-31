#  File: Books.py

#  Description: word frequency comparison between two books

#  Student Name: Andrew Chen

#  Student UT EID: ayc453

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/30/2016

#  Date Last Modified: 12/02/2016

# Create word dictionary from the comprehensive word list
word_dict = {}

def create_word_dict ():

    dict = open("words.txt", "r")

    for lines in dict:
        line = dict.readline()
        line = line.strip()

        if line in word_dict:
            word_dict[line] = word_dict[line] + 1
        else:
            word_dict[line] = 1

    dict.close()


# Removes punctuation marks from a string
def parseString (st):

    newSt = str(st).replace("'s", " ")

    s = ""
    for ch in newSt:
        if ch.isalpha() or ch.isspace():
            s += ch
        if ch == "'":
            s += ch
        else:
            s += ""

    return s

# Returns a dictionary of words and their frequencies
def getWordFreq (file):

    book = open(file, "r", encoding = "utf8")

    # setting the lists and counters
    CapitalWords = {}
    freqWord = {}
    total = 0

    # running through each word in each line
    for lines in book:
        line = lines.strip()
        line = parseString(line)
        list_words = line.split()

        # editting into dictionaries
        for word in list_words:
            total += 1

            #accounting for names and places etc
            if word[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if word in freqWord:
                    freqWord[word] = freqWord[word] + 1
                else:
                    freqWord[word] = 1
            if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if word in CapitalWords:
                    CapitalWords[word] = CapitalWords[word] + 1
                else:
                    CapitalWords[word] = 1

    # putting everything capital word that is in the scrabble dictionary into the freqdictionary
    for key in CapitalWords:
        if (key.lower() not in freqWord):
            if key.lower() in word_dict:
                if key in freqWord:
                    freqWord[key] = freqWord[key] + 1
                else:
                    freqWord[key] = 1

    return freqWord

# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):

    # book 1 variables and counters
    distinctWords_1 = 0
    total_1 = 0
    authorSet1 = set()
    for key in freq1:
        distinctWords_1 += 1
        total_1 += freq1[key]
        authorSet1.add(key.lower())

    # book 2 variables and counters
    distinctWords_2 = 0
    total_2 = 0
    authorSet2 = set()
    for key in freq2:
        distinctWords_2 += 1
        total_2 += freq2[key]
        authorSet2.add(key.lower())

    # calculations for each book
    Ratio_1 = distinctWords_1 / total_1

    Ratio_2 = distinctWords_2 / total_2

    # comparison between authors
    Author_1_not_2 = authorSet1 - authorSet2
    Author_2_not_1 = authorSet2 - authorSet1

    # calculations for relative frequency
    relative_tot1 = 0
    relativeCount1 = 0
    for key in Author_1_not_2:
        relativeCount1 += 1
        if key.lower() in freq1:
            relative_tot1 += freq1[key]

    relative_tot2 = 0
    relativeCount2 = 0
    for key in Author_2_not_1:
        relativeCount2 += 1
        if key.lower() in freq2:
            relative_tot2 += freq2[key]

    # printing the target output
    print(author1)
    print("Total distinct words =", distinctWords_1)
    print("Total words (including duplicates) =", total_1)
    print("Ratio (% of total distinct words to total words) =", "{:.2%}".format(Ratio_1))
    print(" ")
    print(author2)
    print("Total distinct words =", distinctWords_2)
    print("Total words (including duplicates) =", total_2)
    print("Ratio (% of total distinct words to total words) =", "{:.2%}".format(Ratio_2))
    print(" ")
    print(author1, "used", relativeCount1, "words that", author2, "did not use.")
    print("Relative frequency of words used by", author1, "not in common with", author1, "=", "{:.2%}".format(relative_tot1 / total_1))
    print(" ")
    print(author2, "used", relativeCount2, "words that", author1, "did not use.")
    print("Relative frequency of words used by", author2, "not in common with", author2, "=", "{:.2%}".format(relative_tot2 / total_2))


def main():

    # Create word dictionary from comprehensive word list
    create_word_dict()

    # Enter names of the two books in electronic form
    book1 = input ("Enter name of first book: ")
    book2 = input ("Enter name of second book: ")
    print(" ")


    # Enter names of the two authors
    author1 = input ("Enter last name of first author: ")
    author2 = input ("Enter last name of second author: ")
    print(" ")

    # Get the frequency of words used by the two authors
    wordFreq1 = getWordFreq(book1)
    wordFreq2 = getWordFreq(book2)

    # Compare the relative frequency of uncommon words used
    # by the two authors
    wordComparison (author1, wordFreq1, author2, wordFreq2)

main()