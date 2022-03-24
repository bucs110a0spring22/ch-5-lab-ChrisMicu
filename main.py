'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################


#Part A
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
    The function draws a square for the window
    args: (myturtle, width, top_left_x, top_left_y)
    return: none
    '''

  myturtle.pu()
  myturtle.goto(top_left_x,top_left_y)
  myturtle.pd() 
  sides= 4
  width=2
  angle= 360/sides
  for i in range(4):
    myturtle.forward(width)
    myturtle.right(angle)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.pu()
  myturtle.goto(x_start, y_start)
  myturtle.pd()
  myturtle.goto(x_end, y_end)
  '''
    The function draws the x and y axis of the dartboard
    args: (myturtle, x_start, y_start, x_end, y_end) 
    return: none
    '''

def drawCircle(myturtle=None, radius=0):
  myturtle.pu()
  myturtle.goto(0, -1) 
  myturtle.pd()
  myturtle.circle(radius, steps=100)
  '''
    The function draws a circle for the dartboard
    args: (myturtle, radius)
    return: none
    '''

def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates(-1,-1,1,1)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, 1, 0, -1)
  drawCircle(myturtle, 1)
  '''
    The function sets up the dartboard
    args: (myscreen, myturtle)
    return: none
    '''

def throwDart(myturtle=None):
    x= random.uniform(-1, 1)
    y= random.uniform(-1, 1)
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.dot()
    if (isInCircle(myturtle,x,y)):
      myturtle.goto(x , y)
      myturtle.dot('blue')
      return True
    else:
      myturtle.goto(x , y)
      myturtle.dot('red')
      return False
''' 
The function throws darts 
args: (myturtle)
return: none
'''
#Part B 
def playDarts(myturtle=None):
  playerOne = 0
  playerTwo = 0

  for i in range(10):
    throwDart(myturtle)
    if (isInCircle(myturtle, 0, 0, 1) == True):
      playerOne += 1
      print("player 1 scores")
    throwDart(myturtle)
    if (isInCircle(myturtle, 0, 0, 1) == True):
      playerTwo += 1
      print("player 2 scores")

    print("player one's score is " + str(playerOne))
    print("player two's score is " + str(playerTwo))

  if (playerOne > playerTwo):
    print ("Player One Wins!")
  elif (playerTwo > playerOne):
    print ("Player Two Wins!")
  else:
    print ("It's a TIE!")
'''
The function throws darts for 2 players, keeps track of scores, and   decides the winner
args: (myturtle)
return: Player One Wins! Player Two Wins! It's a TIE!
'''

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  distance = myturtle.distance(circle_center_x, circle_center_y)
  if (distance <= radius):
      return True
  else:
      return False

  '''
    The function measures the distance of the dart to the center
    args: (myturtle, circle_center_x, circle_center_y)
    return: True or False
    '''

#Part C
def montePi(myturtle=None, num_darts=0):
  inside_count= 0
  for i in range(num_darts):
    throwDart(myturtle)
    if (isInCircle(myturtle, 0, 0, 1) == True):
      inside_count += 1 
  pi = (inside_count/num_darts) * 4 
  return pi
'''
The function divides numbers of darts by number of darts and multiplies it by 4 to get an approximation of pi
args: (myturtle)
return: pi
'''
   

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
  
    
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
   
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
  