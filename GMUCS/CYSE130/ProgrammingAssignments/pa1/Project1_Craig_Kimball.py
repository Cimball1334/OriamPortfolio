# Authour: Craig Kimball
# Date: 10/12/2021
# CYSE Programming assignment 1

#GMU HONOR CODE

#To promote a stronger sense of mutual responsibility, respect, trust, and fairness among all
#members of the George Mason University Community and with the desire for greater academic
#and personal achievement, we, the student members of the university community, have set for
#This Honor Code: Student Members of the George Mason University community pledge not to 
#cheat, plagiarize, steal, or lie in matters related to academic work.


import math
from math import sqrt
import time
from openpyxl.reader.excel import load_workbook
from xlrd.biffh import WBKBLOBAL


method_one_list = []
method_two_list = []
method_three_list = []
method_four_list = []

start_time = 0.0

method_one_time = 0.0
method_two_time = 0.0
method_three_time = 0.0
method_four_time = 0.0


#method one, checks if there is any remainder between 2 and num
#if theres a remainder the number is prime, if not it is composite
def prime_test_one(num):
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False
            
    return prime

#method two, checks if there is any remainder between 2 and n/2
#if there is a remainder the number is prime, else composite
def prime_test_two(num):
    prime = True
    for i in range(2,int(num/2)+1):
        if num%i == 0:
            prime = False
    
    return prime

#method three, checks if there is any remainder between 2 and sqrt(num)
#if there is a remainder the number is prime, else composite
def prime_test_three(num):
    prime = True
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            prime = False
    return prime

#method four, checks if there is any remainder between a prime number within 2 and sqrt(num)
#if there is a remainder the number is prime, else composite
def prime_test_four(num):
    primes_less_than = [] 
    prime = True
    # print('++++++++++',num)
    
    for i in method_one_list[1:]:
        if i <= sqrt(num):
            # print(i,num%i)
            if num%i == 0:
                prime = False
    
    
    return prime


#the following blocks of code all use their respected method to calculate all prime numbers between 1 and 100 inclusive
start_time = time.time()
for i in range(1,101):
    if prime_test_one(i):
        method_one_list.append(i)
method_one_time = time.time() - start_time


start_time = time.time()
for i in range(1,101):
    if prime_test_two(i):
        method_two_list.append(i)
method_two_time = time.time() - start_time


start_time = time.time()
for i in range(1,101):
    if prime_test_three(i):
        method_three_list.append(i)
method_three_time  = time.time() - start_time


start_time = time.time()
for i in range(1,101):
    if prime_test_four(i):
        method_four_list.append(i)
method_four_time = time.time() - start_time

#==============================================
#Part Two: Evaluation of methods
#==============================================
# Method one: 
# I liked this method as it is the most abstract representation of what a prime number is. 
# It is the most simple interpretation and is therefore easy to understand as a human interpreter. 
# I do not like this method since it requires the largest number of iterations to calculate each number.
#
# Method Two:
# In contrast to method one, method two cuts the number of iterations down in half immediately.
# This reduces the number of calculations the computer needs to make and therefore is more efficient.
# It works on the principal that products come in pairs and only one of the multiplicands needs to be tested.
#
# I dont have any issues with this method directly.
#
# Method Three:
# this method runs the minimum number of iterations to evaluate a method and therefore is my favorite. 
# This checks, on average, a minimum number of values and therefore takes the least computation.
# The only issue I could come up with is the complexity of calculations and external packages used. 
# The function did not save time in comparison to others and isnt worth the additional calculations to me
#
# Method Four:
# In my opinion this is the worst method for calculating a prime number, becasue it needs prime numbers in order to do so.
# Because of this, you either need to call a list of prime numbers like I chose, or exponentialy increase the number of calculation you need to do.
# Although i was unable to see a decrease in efficiency due to the power of my machine, I can imagine this method taking much longer on slower machines.
print('++++++++++++++','Part One, Calculating Prime Numbers','++++++++++++++','\n',sep='\n')
print('Method one returns: {} and took {} seconds\nMethod two returns: {} and took {} seconds \nMethod three returns: {} and took {} seconds \nMethod four returns: {} and took {} seconds'.format(method_one_list,method_one_time,method_two_list,method_two_time,method_three_list,method_three_time,method_four_list,method_four_time))
print('\n','++++++++++++++','Part Two, Calculating Aggregate Grades from Excel ','++++++++++++++','\n',sep='\n')

import xlrd
import xlwt
from xlutils.copy import copy


xls = 'CYST003.xls'
wb = xlrd.open_workbook(xls)
sheet = wb.sheet_by_index(0)

work = copy(wb)
w_sheet = work.get_sheet(0)
for i in range(9):
    w_sheet.write(0,i,sheet.cell_value(0,i),xlwt.easyxf('font: bold 1'))
w_sheet.write(0,9,'Score',xlwt.easyxf('font: bold 1'))
w_sheet.write(0,10,'Grade',xlwt.easyxf('font: bold 1'))

def get_score(row):
    # Homework Assignments are 60% of grade
    # Midterm is 20% of grade
    # Final Exam is 20% of grade
    
    hw_total  = (sheet.cell_value(row,2)*10+sheet.cell_value(row,3)*10+sheet.cell_value(row,4)*10+sheet.cell_value(row,5)*10+sheet.cell_value(row,6)*10)/5
    mid = sheet.cell_value(row,7)
    final = sheet.cell_value(row,8)
    
    #pretty sure this is wrong
    return (hw_total * 0.6) + (mid * 0.2) + (final * 0.2)

def get_grade(score):
    return 'A' if score >= 94 else 'A-' if score >= 90 else 'B+' if score >=86 else 'B' if score >=83 else 'B-' if score >= 80 else 'C+' if score>= 76 else 'C' if  score >= 73 else 'C-' if score >= 70 else 'D+' if score >= 66 else 'D' if score >= 63 else 'D-' if score >=60 else 'F'
#for every row that is a student

for i in range(1,sheet.nrows):
    score = get_score(i)
    grade = get_grade(score) 
    #section to add score and grade to sheet 
    
    w_sheet.write(i,9,score)
    w_sheet.write(i,10,grade)
    
    

    print("{} {}: score = {:.2f}, grade = {}".format(sheet.cell_value(i,1),sheet.cell_value(i,0),score,grade))
    
#This is the new sheet that has the score and grade calculated. I could not get permisions to overwrite the current file.

work.save('NewSheet.xls')

    
    
    
    
    
    
    
    
    
    
    
    