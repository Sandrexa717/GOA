from turtle import *


#we want to paint a house




#step one:  draw a square


speed(200)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


begin_fill()


forward(200)
left(90)
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)


end_fill()

penup()
goto(200,200)
pendown()


begin_fill()


color("red")
right(150)
forward(200)
left(120)
forward(200)


end_fill()









penup()
goto(60,125)

begin_fill()
pendown()
color("black")


right(60)
forward(40)



right(90)


forward(40)

right(90)


forward(40)

right(90)


forward(40)


penup()


end_fill()

goto(140,125)

begin_fill()

pendown()




left(180)

forward(40)

right(90)

forward(40)

right(90)



forward(40)



right(90)



forward(40)

end_fill()

exitonclick()




