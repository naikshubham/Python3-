import turtle
spiral=turtle.Turtle()
count=0
for i in range(57):
	spiral.forward(i*5)
	spiral.right(144)
	if(count%2 == 0):
		spiral.pencolor("blue")
	if(count%2!=0):
		spiral.pencolor("red")
	count=count+1
turtle.done()
