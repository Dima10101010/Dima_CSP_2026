import turtle

screen = turtle.Screen()
screen.bgcolor("green")
screen.setup(600, 500)

player = turtle.Turtle()
player.shape("square")
player.color("black")
player.penup()

screen.mainloop()
