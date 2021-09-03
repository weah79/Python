import turtle
import random

tao = turtle.Turtle()
tao.shape('turtle')
color = ['red','blue','yellow','green','black','pink']

for i in range(1, 11):
	c = random.choice(color)
	print(str(i) + ' : ' + c)
	tao.color(c)
	r = random.randint(50,100)
	print(r)
	tao.circle(r)
	tao.left(36)
	


