'''
Lecture 5: Conditional Loops
'''


'''
write a program that returns the numbers that are divisible by 7 and multiples of 5 between 1500 and 2700 inclusively
'''

n1 = []
for x in range(1500,2701):
    if(x%7==0) and (x%5 == 0):
        n1.append(str(x))

print('\n',', '.join(n1),'\n\n')

# n2 = [str(x) for x in range(1500,2701) if x % 7 == 0 and x % 5 == 0]
# print(', '.join(n2))


'''
Write a python program that prints each item and its corresponding type from a list
'''
dl = [14,11.2,True,'text',(0,1),[0,1]]
for i in dl:
    print(f"Type of {i} is {type(i)}")

# Example 4:
'''
Write a python program to print the alphabet pattern 'D'
'''

print('\n\n')


str = ''
for r in range(0,7):
    for c in range(0,7):
        if (c == 1 or ((r == 0 or r == 6) and (c > 1 and c <5)) or (c == 5 and r != 0 and r != 6)):
            str+="*"
        else:
            str+= " "
    str+='\n'

print(str,'\n\n') 


'''
Write a python program to calculate a dos age in dog years
For the first 2 years a dog year is 10.5 years while rest is 4
'''

age = 12

if age < 0:
    print('age must be positive')
elif age <= 2:
    print(f'dog is {age*10.5} ears old')
else:
    print(f'dog is {21 + (age-2)*4} years old')


print('\n\n')

'''
Write a python program that accepts a sequence of lines as input
prints the same lines as output in lowercase
Enter blank line to terminate
'''

# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break

# for l in lines:
#     print(l)

# print('\n\n')



'''
Write a program to guess a number between 1 and 9
'''
# import random as rand

# rnd = rand.randint(1,9)
# u = 9
# l = 1
# while True:
#     guess = int(input(f'What is your guess [{l},{u}]'))
#     if guess < rnd:
#         print('too low')
#         l = guess
#     elif guess > rnd:
#         print('too high')
#         u = guess
#     else:
#         print('You got it!')
#         break


# print('\n\n')

'''
Write a python program to get the fibonacci series between 0 and 50
next = sum of before
'''

x,y = 0,1
while y<50:
    print(y)
    x,y = y,x+y

print('\n\n')

'''
Write a program for the washing cycle in your washing machine
'''
x = 1
while(x<=2):
    print(f'cycle num{x}')
    x+= 1
print('done\n\n')

'''
Write a python program to sum the input numbers until an empty number is entered
'''

sum = 0
while True:
    n = input('Enter a num: ')
    if n == '':
        break
    sum+= float(n)

print(sum)