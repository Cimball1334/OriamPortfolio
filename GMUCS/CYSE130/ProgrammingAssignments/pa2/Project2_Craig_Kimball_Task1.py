# Authour: Craig Kimball
# Date: 11/3/2021
# CYSE Programming assignment 2


#GMU HONOR CODE

#To promote a stronger sense of mutual responsibility, respect, trust, and fairness among all
#members of the George Mason University Community and with the desire for greater academic
#and personal achievement, we, the student members of the university community, have set for
#This Honor Code: Student Members of the George Mason University community pledge not to 
#cheat, plagiarize, steal, or lie in matters related to academic work.

import turtle
from random import *
from turtle import *



turtle.setup(600, 600)  # set the size of the window with TurtleScreen
turtle.title('Project Sample - Turtle Art')

penup()
goto(-140,140) #positioning the pen

for sp in range(15): #loop for creating the lines labelled with numbers
  speed(10)
 #setting the speed
  write(sp)
 #writing the int
  right(90)
 #setting right at 90 degrees
  forward(10)
 #forward at 10 units
  pendown()
 #ready to draw
  forward(150)
 #forward at 150 units
  penup()
 #not ready to draw
  backward(160)
 #back at 160 units
  left(90)
 #left set at 90 degrees
  forward(20)
 #forward at 20 units
 
penup()
goto(-150,100)
for i in range(4):
    pendown()
    forward(300)
    backward(300)
    right(90)
    penup()
    forward(30)
    left(90)


turtle1 = Turtle() #creating  turtle
turtle1.color('green') #setting the color to green for the turtle
turtle1.shape('turtle') #setting the shape
turtle1.penup() #not ready to draw
turtle1.goto(-160,115) #positioning the turtle
turtle1.pendown() #ready todraw

turtle2 = Turtle() #creating  turtle
turtle2.color('blue') #setting the color to green for the turtle
turtle2.shape('turtle') #setting the shape
turtle2.penup() #not ready to draw
turtle2.goto(-160,85) #positioning the turtle
turtle2.pendown() #ready todraw

turtle3 = Turtle() #creating  turtle
turtle3.color('orange') #setting the color to green for the turtle
turtle3.shape('turtle') #setting the shape
turtle3.penup() #not ready to draw
turtle3.goto(-160,55) #positioning the turtle
turtle3.pendown() #ready todraw

turtle4 = Turtle() #creating  turtle
turtle4.color('red') #setting the color to green for the turtle
turtle4.shape('turtle') #setting the shape
turtle4.penup() #not ready to draw
turtle4.goto(-160,25) #positioning the turtle
turtle4.pendown() #ready todraw

turtle5 = Turtle() #creating  turtle
turtle5.color('black') #setting the color to green for the turtle
turtle5.shape('turtle') #setting the shape
turtle5.penup() #not ready to draw
turtle5.goto(-160,-5) #positioning the turtle
turtle5.pendown() #ready todraw

turtles = [turtle1,turtle2,turtle3,turtle4,turtle5]
raceWon = False
winner = ''

for turn in range(100): #loop for the race
  turtle1.forward(randint(1,5)) #setting the speed randomly with the "random" module
  turtle2.forward(randint(1,5))
  turtle3.forward(randint(1,5))
  turtle4.forward(randint(1,5))
  turtle5.forward(randint(1,5))
  
  
  for t in turtles:#loops to check each individual turtle object
      if t.xcor() >= 150 and not raceWon: #testing to see if the current turtle position is past finish line and someone else hasnt already won
          raceWon = True#flip flag state
          
          winner = t.pencolor()#getting the color of the turtle that won

if(raceWon):#checks to make sure a turtle crossed the line
    file = open('raceWinners.txt','r')#open a file to save the current text
    text_to_write = file.read().split('\n')#saves text in an array by line
    
    for i in text_to_write:
        if i[0:len(winner)].lower()== winner:#checks for what element of the list is the specific turtle that won
            # print(text_to_write)
            new = i[0:len(winner)+2] + str(int(i[-1])+1)#string manipulation to increment a string number by 1
            text_to_write[text_to_write.index(i)] = new # setting the index to the new element
            # print(text_to_write)
            
    file.close() #closes readable file
    file = open('raceWinners.txt','w')#open file for writing and clears it
    
    for i in range(len(text_to_write)):#loops through each element of the previous file, including the incremented new winner
        # print(text_to_write[i])
        file.write(text_to_write[i])#writes each element
        if i < 4:
            file.write('\n')#adds a new line break between each one
        
    file.close()#closes file


turtle.done()