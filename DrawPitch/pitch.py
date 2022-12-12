import turtle

def drawPitch():
  GREEN="#149118"
  screen = turtle.Screen()
  screen.tracer(0)
  screen.bgcolor(GREEN)
  
  myBrush = turtle.Turtle()
  myBrush.width(1)
  myBrush.hideturtle()
  
  myBrush.speed(0)
  myBrush.color("#FFFFFF")
  
  #Outer lines
  myBrush.penup()
  myBrush.goto(-140,195)
  myBrush.pendown()
  myBrush.goto(140,195)
  myBrush.goto(140,-195)
  myBrush.goto(-140,-195)
  myBrush.goto(-140,195)
  
  #Penalty Box - Top
  myBrush.penup()
  myBrush.goto(0,115)
  myBrush.pendown()
  myBrush.circle(40)
  myBrush.penup()
  myBrush.goto(-80,195)
  myBrush.pendown()
  myBrush.fillcolor(GREEN)
  myBrush.begin_fill()
  myBrush.goto(80,195)
  myBrush.goto(80,140)
  myBrush.goto(-80,140)
  myBrush.goto(-80,195)  
  myBrush.end_fill()
 
  #Penalty Box - Bottom 
  myBrush.penup()
  myBrush.goto(0,-195)
  myBrush.pendown()
  myBrush.circle(40)
  myBrush.penup()
  myBrush.goto(-80,-195)
  myBrush.pendown()
  myBrush.fillcolor(GREEN)
  myBrush.begin_fill()
  myBrush.goto(80,-195)
  myBrush.goto(80,-140)
  myBrush.goto(-80,-140)
  myBrush.goto(-80,-195)  
  myBrush.end_fill()

  # Goal Box - Bottom
  myBrush.penup()
  myBrush.goto(40,-195)
  myBrush.pendown()
  myBrush.goto(40,-170)
  myBrush.goto(-40,-170)
  myBrush.goto(-40,-195)  

  # Goal Box - Top
  myBrush.penup()
  myBrush.goto(40,195)
  myBrush.pendown()
  myBrush.goto(40,170)
  myBrush.goto(-40,170)
  myBrush.goto(-40,195)     
  
  #Halfway Line
  myBrush.penup()
  myBrush.goto(-140,0)
  myBrush.pendown()
  myBrush.goto(140,0)
  
  #Central Circle
  myBrush.penup()
  myBrush.goto(0,-40)
  myBrush.pendown()
  myBrush.circle(40)
  
  screen.tracer(1)  