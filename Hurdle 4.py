def reite():
    turn_left()
    turn_left()
    turn_left()

def jumb():
    turn_left()
    while wall_on_right() :
        move()
    reite()
    move()
    reite()
    move() 
    while front_is_clear() :
        move()
    turn_left()
while not at_goal():
      if front_is_clear():
          move()
      else:
            jumb()
    
      
            










################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
