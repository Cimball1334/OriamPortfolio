# import Project3_Craig_Kimball as py
import Project3_Craig_Kimball as py

file = 'C:\\Users\\kimba\\git\\CollegeClasses\\CollegeClasses\\CollegeClasses\\ClassScripts\\CYSE130\\ProgrammingAssignments\\pa3\\dream_speech.txt'
# file = 'C:\\Users\\kimba\\git\\CollegeClasses\\CollegeClasses\\CollegeClasses\\ClassScripts\\CYSE130\\ProgrammingAssignments\\pa3\\old.txt'
# f = open(file,'r')

text = py.text_from_file(file)
# print(text)

# print("the" in text)

# print(py.remove_punctuation(text))
# print("the" in text)
# print(py.number_of_sentences(text))
dict = py.create_word_dictionary(text)
print('The' in dict)
print(dict['The'])

# print(py.create_word_dictionary(text))
