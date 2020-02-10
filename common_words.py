'''
Choose a text file from Project Gutenberg, and create a Python script that reads through it and calculates:

    * The 5 most common words in the text.

    * What percentage of the entire text is taken up by each of those words

   Feel free to do any other analysis or provide any other statistics you find interesting.

Please provide links to the repositories containing your source code, as well as a breakdown of your results for question 2.
'''

import os
from collections import Counter
import pprint

'''
This method prints the instructions to the user and displays the txt files located in the working folder
or sub-folder
'''
def print_instructions():
    '''
    Prompt user on the purpose of this file
    '''
    star = '*'.center(80, '*')
    print(star)
    message = 'Enter the number that corresponds with the .txt file displayed below that'
    print('*' + message.center(78) + '*')
    message = 'you wish to find the 5 most common words.'
    print('*' + message.center(78) + '*')
    message = 'The .txt file must be in the same directory as this python file.'
    print('*' + message.center(78) + '*')
    print(star + '\n')


'''
This method prints all the txt files found in the working folder or sub-folder and allows the user to select which txt
file they would like to use.
'''
def get_txt_file():
    # create a variable that will count the files ending in .txt in the current working directory or sub directories
    count = 0
    # create a list to hold the files ending in .txt in the current working directory or sub directories
    text_files = []
    # iterate through the files in the folder looking for files ending in .txt
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        for file in filenames:
            # find the files ending in .txt
            if file[-4:] == '.txt':
                # print the number and name of each file
                print(str(count + 1) + '. ' + file)
                # add the file to the list
                text_files.append(file)
                # add to the count
                count += 1

    # if the count is zero no txt files were found. exit program so user can add files.
    if count == 0:
        print("No files were found in the working folder or sub folders. The program will now exit.")
        exit()

    # get user's .txt choice
    while True:
        try:
            # ask the user to enter the number choice for the file
            selected_file = int(input("Please enter a number: "))
            # raise IndexError if the users input is less than or equal to zero
            if selected_file <= 0:
                raise IndexError
            # extract that file from the list
            filename = str(text_files[selected_file - 1])
            break
        except ValueError:
            # if user did not enter a number throw error message
            print("That was not a valid number.  Try again...")
        except IndexError:
            # if user entered number out of range of list throw error message
            print('That value was out of range.  please select between 1 and ' + str(count))

    # open the book the user selected
    book = open(filename, encoding="utf8")
    # assign the text in the file to content
    content = book.read()
    # close the book file because it is no longer needed.
    book.close()
    # assign content of the book to a string than split it
    book_string = str(content)
    # create a dictionary where the key is the word in the file and the value is the times it appears

    return book_string


'''
this method creates a dictionary will all of the words in the book and the number of times they are used.
'''
def book_dictionary(book):
    # create a dictionary where the key is the word in the file and the value is the times it appears
    result = {}
    for element in book.split():
        if element not in result:
            result[element] = 1
        else:
            result[element] += 1

    return result


'''
this method creates a dictionary with all the words in the book except for the 100 most common words.
'''
def book_dictionary_uncommon(book):
    common_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with",
                    "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her",
                    "she", "or", "will", "an", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out",
                    "if", "about", "who", "get", "which", "go", "when", "me", "make", "can", "like", "time", "no",
                    "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them",
                    "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
                    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want",
                    "because", "any", "these", "give", "day", "most", "us"}

    # create a dictionary where the key is the word in the file and the value is the times it appears
    result = {}
    for element in book.split():
        if element not in common_words:
            if element not in result:
                result[element] = 1
            else:
                result[element] += 1

    return result

''' Print the table to the user '''
def print_table(title, dict):
    # create a line of stars to delimite the rows of the table
    star = '*'.center(80, '*')
    print(star)

    # print the title of the table
    print('*' + title.center(78) + '*')
    print(star)

    # print the heading of the columns
    print('*' + "Most Common Words".center(25) + '*' + "Times Appeared".center(25) + '*' +
          "Percentage of Book".center(26) + '*')
    print(star)

    # iterate through the dictionary and print the word, amount, and percentage it appeared in the text.
    for key, value in dict.items():
        print('*' + key.center(25) + '*' + str(value).center(25) + '*' +
              (str('{0:.2f}'.format(value / total_words)) + '%').center(26) + '*')
        print(star)

    # print an extra line to leave space between tables.
    print("\n")

''' Main program '''
while True:
    title = ''
    # print the instructions to the user
    print_instructions()

    # get the book the user wants to use
    book = get_txt_file()

    # create a dictionary of the words and times they appear in the book
    words_count = book_dictionary(book)

    # create a dictionary of the words and times they appear in the book
    words_count_lower = book_dictionary(book.lower())

    # check the words again removing the 100 most common words in the english language.
    # also force all words to lowercase.
    words_count_uncommon = book_dictionary_uncommon(book.lower())

    # get a total word count of the book
    total_words = sum(words_count.values())

    # create a dictionary with the top five used words from file
    top_words = dict(Counter(words_count).most_common(5))

    # create a dictionary with the top five used words from file
    top_words_lower = dict(Counter(words_count_lower).most_common(5))

    # create a dictionary with the top five used words from file
    top_uncommon_words_lower = dict(Counter(words_count_uncommon).most_common(5))

    title = "Top 5 words used in the text regardless of capitalization."
    print_table(title, top_words)

    title = "Top 5 words in the text forcing all text to lowercase."
    print_table(title, top_words_lower)

    title = "Top 5 words in the text forced to lowercase and excluding most common words."
    print_table(title, top_uncommon_words_lower)

    # ask the user if they would like to do another book
    while True:
        print('Would you like to do another book? Y/N')
        anotherMadLibs = str(input())
        if anotherMadLibs.upper() == 'N':
            exit()
        elif anotherMadLibs.upper() != 'Y':
            print('Please enter either Y or N')
        else:
            break
