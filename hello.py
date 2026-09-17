from turtle import Turtle,Screen
import random


window=Screen()
window.setup(width=800,height=800)
window.bgcolor("black")

sam = Turtle()
sam.shape("turtle")
sam.color("white")
sam.pensize(5)
sam.speed("fast")





tom = Turtle()
tom.shape("square")
tom.color("orange")
tom.pensize(5)
tom.speed("fastest")
 

angle = [0.90,180,270]
dis = [20,30,40,50,60,70,80,90,100]
loop_count = [5,15,20,25]

def draw_random(turtle_name):
    for _ in range(random.choice(loop_count)):
        turtle_name.forward(random.choice(dis))
        turtle_name.left(random.choice(angle))
draw_random(tom)
draw_random(sam)

for _ in range(20):
    tom.circle(100)
    tom.left(360 / 20)
    

window.exitonclick()