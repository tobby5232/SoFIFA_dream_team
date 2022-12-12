#Football Formation Challenge - www.101computing.net/football-formation/
import pitch
import WhoScorePlayer
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

drawPlayer("blue",0,-180, WhoScorePlayer.goalKeeper, 1, "red") 
drawPlayer("purple",-50,-120,WhoScorePlayer.Defender[3], 3, "red") 
drawPlayer("purple",50,-120,WhoScorePlayer.Defender[1], 4, "red") 
drawPlayer("purple", -100, -80, WhoScorePlayer.Defender[2], 2, "red") 
drawPlayer("purple", 100, -80, WhoScorePlayer.Defender[0], 5, "red")
drawPlayer("white", 0, -65, WhoScorePlayer.Midfielder[0], 6, "red")
drawPlayer("white", -50, -15, WhoScorePlayer.Midfielder[1], 7, "red")
drawPlayer("white", 50, -15, WhoScorePlayer.Midfielder[2], 8, "red")
drawPlayer("orange", -100, 45, WhoScorePlayer.Forward[0], 9, "red")
drawPlayer("orange", 100, 45, WhoScorePlayer.Forward[1], 10, "red")
drawPlayer("hot pink", 0, 80, WhoScorePlayer.Forward[2], 11, "red")
turtle.done()

