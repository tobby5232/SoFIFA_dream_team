#Football Formation Challenge - www.101computing.net/football-formation/
import pitch
import turtle
from random import randint

#A Procedure to draw a player at the given position
def drawPlayer(color,x,y,label,number,card):
  screen = turtle.Screen()
  screen.tracer(0)
  myPen = turtle.Turtle()
  myPen.hideturtle()
  myPen.penup()
  myPen.goto(x,y)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(15)
  myPen.end_fill()
  screen.tracer(1)  
  myPen.penup()
  myPen.goto(x,y-10)
  myPen.color("black")
  myPen.write(label, align='center', font=('courier', 8))
  myPen.goto(x,y+10)
  card = randint(1,6)
  if card == 1:
    myPen.color("red")
  if card == 2:
    myPen.color("yellow")
  else:
    myPen.color("black")
  myPen.write(number, align='center', font=('Times New Roman', 12, 'bold'))
  
#MAIN PROGRAM STARTS HERE
pitch.drawPitch()

drawPlayer("blue",0,-180, "Goal Keeper", 1, "red") 
drawPlayer("purple",-50,-120,"Center Back", 3, "red") 
drawPlayer("purple",50,-120,"Center Back", 4, "red") 
drawPlayer("purple", -100, -80, "Left Back", 2, "red") 
drawPlayer("purple", 100, -80, "Right Back", 5, "red")
drawPlayer("white", 0, -65, "Holding Mid", 6, "red")
drawPlayer("white", -50, -15, "Attacking Mid", 7, "red")
drawPlayer("white", 50, -15, "Attacking Mid", 8, "red")
drawPlayer("orange", -100, 45, "Outside Mid", 9, "red")
drawPlayer("orange", 100, 45, "Outside Mid", 10, "red")
drawPlayer("hot pink", 0, 80, "Forward", 11, "red")
# drawPlayer("yellow",0,-250, "Substution1", 1, "red") 
turtle.done()
