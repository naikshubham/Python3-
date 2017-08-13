import turtle

squ=turtle.Turtle()

def square(length,degree):
	for i in range(4):
		squ.forward(length)
		squ.right(degree)

for i in range(0,50):
	square(100,90)
	c_degree=10
	squ.right(c_degree)
turtle.done()
