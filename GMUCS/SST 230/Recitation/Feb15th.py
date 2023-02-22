'''
Lecture 4: Strings
'''


print('\n\nString Formatting:')
age = 40
sib = 3
str = "my age is {}, my name is John, I have {} siblings"
print(str.format(age,sib))
str = "my age is {1}, my name is John, I have {0} siblings"
print(str.format(sib,age))



print('\n\nEscape Characters:')
print('it\'s alright')
print('\\ slash \\')
print('Hello,\nWorld!')
print('\110\145\154\154\157')
print('\x48\x65\x6c\x6c\x6f')



print('\n\nString Comparisons:')
str1 = "Hello, World!"
str2 = "I love Python."
str3 = "Hello, World!"

print(str1 == str2)
print(str1 == str2)

if str1 <= str2:
    print(str1, ' is smaller than ' , str2)
if str2 >= str3:
    print(str2, ' is bigger than ' , str3)
if str1 == str3:
    print(str1 , ' is equal to ' , str3)



print('\n\nCase Sensitivity:')
s1 = 'String'
s2 = 'String'
s3 = 'string'

if s1.casefold() == s3.casefold():
    print(s1.casefold())
    print(s3.casefold())
    print('s1, s3 equal case-insensitive')
if s2.upper() == s3.upper():
    print(s2.upper())
    print(s3.upper())
    print('s2, s3 equal case-insensitive')



print('\n\nIndex, Slicing, Splitting:')
str = "This is an example of a random string for slicing"
print(str[0:10])
print(str[-11:])
print(str[::2])

print(str.split())
print(str.split()[4])
print([(str[i:i+5]) for i in range(0,len(str),5)])



print('\n\nCharacter Checking:')
str = "Learning"
print(str.isalpha())
str = "Learning python"
print(str.isalpha())
print(str.islower())
print(str.upper().isupper())
print(str.istitle())
str = 'Learning Python'
print(str.istitle())



print('\n\nStripping Strings:')
str = "     string      "
print(str.strip())
str = '.....string.....'
print(str.lstrip('.'))
print(str.rstrip('.'))
