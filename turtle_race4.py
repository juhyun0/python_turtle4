import turtle
>>> import random
>>> screen=turtle.Screen()
>>> image1="/home/daum/juhyun/3.gif"
>>> image2="/home/daum/juhyun/4.gif"
>>> image3="/home/daum/juhyun/5.gif"
>>> 
>>> screen.addshape(image1)
>>> screen.addshape(image2)
>>> screen.addshape(image3)

t1=turtle.Turtle()
t1.shape(image1)
t1.pensize(5)
t1.penup()
t1.goto(-400,0)


t2=turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-100,0)

t3=turtle.Turtle()
t3.shape(image3)
t3.pensize(5)
t3.penup()
t3.goto(150,0)

t1.pendown()
t2.pendown()
t3.pendown()

for i in range(100):
	d1=random.randint(1,60)
	d2=random.randint(1,60)
	d3=random.randint(1,60)
	t1.forward(d1)
	if t1.goto(-100,0):
		break
	t2.forward(d2)
	if t2.goto(150,0):
		break
	t3.forward(d3)
	

