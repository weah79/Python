import turtle
import random

tao = turtle.Turtle()
tao.shape('turtle')
color = ['red','blue','yellow','green','black','pink']
tao.pensize(4)
for i in range(1,11):
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  size = random.randint(50,100)
  c = random.choice(color)
  tao.color(c)
  tao.penup()
  tao.goto(x,y)
  tao.pendown()
  print('รูปที่ : ' + str(i) + ' สี : ' + c + ' ขนาด : ' + str(size))
  for x in range(4):     
    tao.forward(size)
    tao.left(90)
	
