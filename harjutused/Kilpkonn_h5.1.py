import turtle
# Alari Laine
# 26.11.23
# Kujund 14


aken = turtle.Screen()
aken.setup()
aken.title("Kujund 14")

piim = turtle.Turtle()
piim.speed(10)


for i in range(0,4):
    piim.fd(200)
    piim.lt(90)


for i in range(0,8):
    piim.penup()
    piim.goto(100,100)
    piim.pendown()
    piim.rt(10)
    piim.penup()
    piim.fd(100)
    piim.pendown()
    piim.rt(90)
    piim.fd(100)
    piim.rt(90)
    piim.fd(200)
    piim.rt(90)
    piim.fd(200)
    piim.rt(90)
    piim.fd(200)
    piim.rt(90)
    piim.fd(100)

turtle.exitonclick()