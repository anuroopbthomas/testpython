import turtle

square = "square"
circle = "circle"
triangle = "triangle"
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(other_turtle):
    other_turtle.forward(100)
    other_turtle.right(90)
    other_turtle.forward(100)
    other_turtle.right(135)
    other_turtle.forward(100 * 1.41421356237)
    other_turtle.right(135)

def draw_circlewithsquare(brad):
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("blue")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")



    at = turtle.Turtle()
    at.right(90)
    at.forward(200)
    at.backward(200)
    at.left(90)
    at.forward(100)
    at.right(90)
    at.forward(100)
    at.right(90)
    at.forward(100)
    at.backward(100)
    at.left(90)
    at.forward(100)
    at.backward(200)
    at.left(90)

    at.penup()
    at.forward(50)
    at.pendown()
    at.forward(100)
    at.backward(50)
    at.right(90)
    at.forward(200)
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.speed(2)
    #angie.circle(100)

    #tom = turtle.Turtle()
    #tom.shape("square")
    #tom.color("green")
    #tom.speed(5)
    #draw_triangle(tom)

    window.exitonclick()


draw_art()
