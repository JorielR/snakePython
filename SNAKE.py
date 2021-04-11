from turtle import *
import time
import random
from random import randint
#randint is an inbuilt function from the random library
delay = .1 # this is to slow the snake since the default movement is very fast
body = [] # setting the variable body to have parameters 
playgame = True
#Lets start by setting up the screen
Screen() # this is a method sed to create a screen from the turtle library.
screensize(-300 , 300)# this method creates the full size of the screen (x,y)
screensize(-300, 300)
title("Joriel's snake game") #the title method allows you to create a title for the program.
bgcolor("grey") # this method is used to create the color for the background.
#setup(width = 300, height = 300)
tracer(0) # (n=None, delay=None). Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update is really performed. (Can be used to accelerate the drawing of complex graphics.) When called without arguments, returns the currently stored value of n. Second argument sets delay value (see delay()).

#Now lets create the Snake
snakeHead = Turtle() # here im assigning the turtle object from the the turtle library to the variable named snakeHead
snakeHead.speed(0) # this is the speed method from the the turtle library. Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning
snakeHead.shape("circle") # this method allows you to create the shape of the turtle. So far there are limited shapes that the library offeres.
snakeHead.color("black") # this color method allows you to color your turtle object to your desired color. To this point, there are limited colors available.
snakeHead.penup()#in the turtle library, turtle objects automaticaly draw as they move. By adding this method, you "pull the pen up," keeping it from drawing when moving.
snakeHead.goto(0, 100) # this method gives your turtle oject (x,y) coordinates for placement
snakeHead.direction = "stop" # this method places your turtle object at a neutral position, keep it from moving at different available directions.




#lets make turtle food for the snake
turtle = Turtle()
turtle.speed(0)
turtle.shape("turtle")
turtle.shapesize(.5,.5,.5) #this method allows for furthers sizing of your turtle object. The parameter are as followed:(stretch_wid=None, stretch_len=None, outline=None)
turtle.color("red")
turtle.penup()
turtle.goto(randint(-300,0), randint(0,300)) # with the randint, the goto method will randomly select where to place the turle object based on the x,y coordinates placed on it's parameters.
turtle.direction = "stop"


# make congratulations word object
def makeCongrats():
    congrats = Turtle()
    congrats.hideturtle() # this method will "hide" the turtle object after creation. In this case, the object was showing unintendedly, this method solved the problem.
    congrats.write("10 points", False, "center",("Arial", 100,"normal")) #this method allows you to use the turtle object and write on screen. Here are the parameters:(arg, move=False, align="left", font=("Arial", 8, "normal"))
    congrats.color("blue")
    #time.sleep(delay)
    congrats.clear() # this method completely clears or deletes your turtle object. In this case, the object is used temporarly, to this method serves well for this purpose.



#Now lets define how the snake should move
#Here we are creating the function five the turtle object instructions on where to move. We do this by using x,y coordinates - as this is how the turle library measures location, distance, and speed.
def movement():
    if snakeHead.direction == "Up":
        y = snakeHead.ycor() # here we are telling python that y will be the variable to move up on the Y axis by using ycor()
        snakeHead.sety(y + 20) #ycor() is a method for the y axis.
    if snakeHead.direction == "Down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)
    if snakeHead.direction == "Left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)#xcor() is a method for the x axis.
    if snakeHead.direction == "Right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)
        
#Here we are creating the move functions in order to assign them to a key. We use logic to dictate which direction each function belongs to.
def moveUp():
    if snakeHead.direction != "Down":
        snakeHead.direction = "Up"
def moveDown():
    if snakeHead.direction != "Up":
        snakeHead.direction = "Down"
def moveLeft():
    if snakeHead.direction != "Right":
        snakeHead.direction = "Left"
def moveRight():
    if snakeHead.direction != "Left":
        snakeHead.direction = "Right"


#to control the snake, python needs to know when a key is struck and what to do with it
listen() # this method is in the turtle library. It is used so that python can "listen" for the key that it's being assigned to. 
onkey(moveUp, "Up") # the onkey method uses these parameters: (function,key assignment)**NOTE*** This method needs to be used AFTER the function has been created. If not, it will not recognize it for assignment.
onkey(moveDown, "Down")#Notice how the turtle library uses the string literal for the arrow keys. In other languages like javascript, a number would be used to reference the specifed key.
onkey(moveLeft, "Left")
onkey(moveRight, "Right")

#lets create the turtle body
    

while playgame == True:
    update() # This performs a turtlescreen update. It's to be used when tracer is turned off.
    
    #to control the snake, python needs to know when a key is struck and what to do with it
    #time.sleep(delay)
    if snakeHead.xcor()> 370 or snakeHead.xcor()< -370 or snakeHead.ycor()> 310 or snakeHead.ycor()< -310:
        snakeHead.goto(0,0)
        snakeHead.direction = "stop"
    # this if statement is to first: create a random location for turtle food object, second, to create new objects a result of it.
    if snakeHead.distance(turtle) < 15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        turtle.goto(x, y)
        makeCongrats()
        newBody = Turtle()
        newBody.speed(0)
        newBody.shape("square")
        newBody.color("black")
        newBody.penup()
        body.append(newBody)
      # this for statment creates the parameters needed for place the new body with the snake head.
      # to do this, we need to create a list of bodies, find the range, and then set them to the proper coordinates. 
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
        
    # Move body 0 to where the head is
    if len(body) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        body[0].goto(x,y)

   
    
    movement()
    time.sleep(delay)
    
mainloop()


