from turtle import *

speed(0.0000000000000000005)

#Grass
bgcolor("green")

shape("turtle")
#Sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

#Sun
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()


#House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "orange") # (stroke, fill)

# castle1
begin_fill()
forward(270)
left(90)
forward(150)
left(90)
forward(270)
left(90)
forward(150)
end_fill()

#castle dor
penup()
goto(-26, -100)
pendown()

right(180)
forward(100)
right(90)
forward(120)
right(90)
forward(100)

#castle dor2
color("chocolate", "brown")
begin_fill()
penup()
goto( 13, -100)
pendown()


left(180)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

#castle saxuravi
penup()
goto(-100, 50)
pendown()

begin_fill()
left(180)
forward(40)

right(90)
forward(35)
right(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
right(90)
forward(40)
right(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
right(90)
forward(40)
right(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
right(90)
forward(35)
right(90)
forward(40)
end_fill()

#dor saxuravi

penup()
goto(-26, 0)
pendown()

begin_fill()
left(180)
forward(26)

right(90)
forward(20)
right(90)
forward(18)
left(90)
forward(26)
left(90)
forward(18)
right(90)
forward(26)

right(90)
forward(18)
left(90)
forward(26)
left(90)
forward(18)
right(90)
forward(20)
right(90)
forward(26)
end_fill()

#shua sveti
penup()
goto(-25,90 )
pendown()

color("chocolate", "orange")
begin_fill()
left(180)
forward(160)
right(90)
forward(120)
right(90)
forward(160)
end_fill()




#shuasvetis roof
penup()
goto(-25, 250)
pendown()
color("chocolate", "brown")
begin_fill()
left(140)
forward(97)
right(102)
forward(97)
end_fill()

#SHUASVETIS NAWILI
penup()
goto(16, 90)
pendown()

color("chocolate", "orange")
begin_fill()
right(40)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
end_fill()

# left sveti
penup()
goto(-100, -100)
pendown()

begin_fill()
left(0.9)
forward(280)
left(91)
forward(120)
left(90)
forward(280)
end_fill()

#left sveti roof



right(140)
forward(1)
left(102)
forward(1)


#right svet
color("chocolate","orange")
penup()
goto( 170, -100)
pendown()
begin_fill()
right(142)
forward(280)
right(90)
forward(120)
right(90)
forward(280)
end_fill()

#right svetis roof
#right svetis roof
color("chocolate", "brown")
penup()
goto(291, 180)
pendown()

begin_fill()
left(90)
forward(30)
left(90)
forward(60)
left(90)

forward(15)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)

left(90)
forward(15)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

#left svet roof

penup()
goto(-95, 180)
pendown()

begin_fill()
forward(30)
left(90)
forward(60)
left(90)
forward(15)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)

left(90)
forward(15)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

#ფანჯარა1
begin_fill()
penup()
goto(70, 150)
pendown()
color( "brown")
right(90)
forward(40)
right (90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()
#circle

penup()
goto(55, 130)
pendown()
begin_fill()
circle(15)
end_fill()

#second windwos
penup()
goto(20, 190)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()
#circle
penup()
goto(5, 210)
pendown()

begin_fill()
circle(15)
end_fill()

#left svet windows
penup()
goto(-120, -20)
pendown()
begin_fill()
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()

#circle
penup()
goto(-135, 0)
pendown()

begin_fill()
circle(15)
end_fill()

#left svet windows
penup()
goto(-175, 100)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()

#circle

penup()
goto(-190, 124)
pendown()

begin_fill()
circle(15)
end_fill()

#right svet windows
penup()
goto( 220, -20)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()

#circle
penup()
goto(205, 0)
pendown()

begin_fill()
circle(15)
end_fill()

#rightsvet windows2

penup()
goto( 270, 100)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()

#circle

penup()
goto( 255, 120)
pendown()

begin_fill()
circle(15)
end_fill()

# flag of goa
color("green")
penup()
goto( -200, 240)
pendown()

left(90)
forward(70)
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)

#GOA
penup()
goto( -190, 285)
pendown()

#G
right(90)
forward(2)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(15)
right(90)
forward(20)
right(90)
forward(15)

#O
color("brown")
penup()
goto( -160, 275)
pendown()

circle(10)

#A
color("green")
penup()
goto( -137, 278)
pendown()

left(60)
forward(25)
right(140)
forward(25)

left(180)
forward(15)
left(100)
forward(10)

#river
color("deepskyblue")
penup()
goto(-400, -170)
pendown()

begin_fill()
left(160)
forward(1000)
right(90)
forward(50)
right(90)
forward(1000)
right(90)
forward(50)
end_fill()





hideturtle()
exitonclick()

