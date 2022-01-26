#################################################################
# FILE : hello_turtle.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that draws a flower bed using module "turtle"
#################################################################
import turtle

def draw_petal():
    """this function draws a single petal"""
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    """this function draws a single flower using the previous function petal 4 times"""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance():
    """this function draws a single flower and moves the turtle without drawing"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    """this function draws a flowerbed using the previous function 3 times."""
    turtle.up()  #these lines adjust the turtle's angle and location so the flowers won't be upsidedown.
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done()

