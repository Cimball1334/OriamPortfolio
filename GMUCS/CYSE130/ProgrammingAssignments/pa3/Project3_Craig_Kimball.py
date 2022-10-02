# Authour: Craig Kimball
# Date: 12/06/2021
# CYSE Programming assignment 3

#GMU HONOR CODE

#To promote a stronger sense of mutual responsibility, respect, trust, and fairness among all
#members of the George Mason University Community and with the desire for greater academic
#and personal achievement, we, the student members of the university community, have set for
#This Honor Code: Student Members of the George Mason University community pledge not to 
#cheat, plagiarize, steal, or lie in matters related to academic work.

"""
function text_from_file takes in a string f, the location of a .txt file
and returns a string containg the contents of that file
"""
def text_from_file(f):
    with open(f, 'r') as file:
        text = file.readlines()
        return ''.join(text)

"""
Function remove_punctuation take in a string of text s
Returns the string (s) without any punction as defined by the list
New String replaces each punctuation with ''
"""
def remove_punctuation(s):
    for c in [",",";",":",".","?","!","[","]","*","(",")","-","'",'"']:
        # print(c)
        s = s.replace(c,'')
    return s

"""
Function number_of_sentences takes in a string s
Returns the number of sentences the string contains
"""
def number_of_sentences(s):
    # return s.count('.') + s.count('?') + s.count('!')
    count = 0
    for c in s:
        if c in ['.','?','!']:
            count += 1
    return count

"""
Function create_word_dictionary takes in a string s
Creates a dictionary of every unique word in the sentence and the value is the number of times it appears
Formats the Key values to be Uppercase first letter
Return Dictionary
"""
def create_word_dictionary(s):
    s.upper()
    dict = {}
    #manipulates the imut string into a way hat can be easily utilized
    lst = remove_punctuation(s).replace(' ','\n').split('\n')
    while '' in lst:
        lst.remove('')
    
    
    for w in lst:
        key = w[0:1].upper()+w[1:].lower()
        if key in dict:
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1

    return dict
"""
this segment of code checks to see if the call to Project3_Craig_Kimball.py is a import, or ran locally
This allows for code to be isolated to the module alone
"""
if __name__ == "__main__":
    #this code only runs in the module

    #file path on my local computer
    # file = 'C:\\Users\\kimba\\git\\CollegeClasses\\CollegeClasses\\CollegeClasses\\ClassScripts\\CYSE130\\ProgrammingAssignments\\pa3\\dream_speech.txt'
    
    #generic file path assuming directory is matching
    file = 'dream_speech.txt'

    text = text_from_file(file)

    lst = remove_punctuation(text).replace(' ','\n').split('\n')
    while '' in lst:
        lst.remove('')

    #varaibles for use in string formating
    sentences = number_of_sentences(text)
    words = len(lst)
    dict = create_word_dictionary(text)
    dict = sorted(dict.items(), key = lambda item: item[1], reverse=True)
    unique = len(dict)



    print('Number of sentences: {}\nNumber of words: {}\nNumber of unique words: {}\nThe 15 most common words:'.format(sentences,words,unique))
    for i in range(15):
        print('{} {}'.format(dict[i][1],dict[i][0]))