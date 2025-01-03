from turtle import Turtle

STARTINT_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.goto(STARTINT_POSITION)
    self.setheading(90)
  
  def go_up(self):
    self.forward(MOVE_DISTANCE)