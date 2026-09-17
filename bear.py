from turtle import Turtle, Screen
window = Screen()


window.bgcolor("black")
window.setup(width=900, height=900)

sam = Turtle()
sam.color("white")
sam.shape("turtle")
sam.pensize(3)
sam.speed("fastest")


def draw_circeles():
    sam.penup()
    for _ in range(20):
      
      
      sam.goto(-300, -300)
      sam.pendown()
      sam.circle(50)
      sam.left(360/20)

  



    
def draw_squares():
   sam.penup()
   
   for _ in range(20)   :
      sam.goto(0,0)  
      sam.pendown()
      for _ in range(4):
         sam.left(-90)
         sam.forward(50)
         

      sam.left(360/20)  

def draw_triangles():
   sam.penup()
   for _ in range(20):
      
      sam.goto(300, 300)
      sam.pendown()
      for _ in range(3):
         sam.left(120)
         sam.forward(50)
      sam.left(360/20)

draw_circeles()
draw_squares()    
draw_triangles()

window.exitonclick()