import turtle
i = 4
square = "square"
circle = "circle"
triangle = "triangle"

def draw_shape(shape):
    window = turtle.Screen()
    window.bgcolor("red")
    if shape == "square":
        brad = turtle.Turtle()
        brad.shape("circle")
        brad.color("blue")
        brad.speed(3)
        for i in range(4):
            brad.forward(100)
            brad.right(90)
    elif shape == "circle":
        angie = turtle.Turtle()
        angie.shape("arrow")
        angie.color("blue")
        angie.speed(2)
        angie.circle(100)
    elif shape == "triangle":
        tom = turtle.Turtle()
        tom.shape("square")
        tom.color("green")
        tom.speed(5)
        tom.forward(100)
        tom.right(90)
        tom.forward(100)
        tom.right(135)
        tom.forward(100 * 1.41421356237)
        tom.right(135)
    else:
        window.exit()

    window.exitonclick()


draw_shape(triangle)
