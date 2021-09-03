Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello World')
Hello World
>>> import turtle
>>> tao = turtle.Turtle()
>>> # T ตัวใหญ่
>>> tao.shape('turtle')
>>> tao.forwar(100)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tao.forwar(100)
AttributeError: 'Turtle' object has no attribute 'forwar'
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.clear()
>>> tao.goto(200, 200)
>>> tao.pensize()
1
>>> tao.pensize(3)
>>> tao.forward(50)
>>> tao.reset()
>>> tao.goto(100,100)
>>> tao.pensize(5)
>>> tao.forward(100)
>>> tao.home()
>>> tao.clear()
>>> for i in range(5):
	print('Hello', i)

	
Hello 0
Hello 1
Hello 2
Hello 3
Hello 4
>>> for i in range(5):
	tao.forward(100)
	tao.left(90)

	
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> tao.clear()
>>> tao.home()
>>> tao.clear()
>>> color = ['red','blue','yellow','green']
>>> type(color)
<class 'list'>
>>> for c in color:
	print(c)
	tao.color(c)
	tao.forword(100)
	tao.left(90)

	
red
Traceback (most recent call last):
  File "<pyshell#42>", line 4, in <module>
    tao.forword(100)
AttributeError: 'Turtle' object has no attribute 'forword'
>>> for c in color:
	print(c)
	tao.color(c)
	tao.forward(100)
	tao.left(90)

	
red
blue
yellow
green
>>> tao.clear()
>>> tao.circle(10)
>>> tao.pensize(1)
>>> tao.circle(100)
>>> tao.clear()
>>> tao.circle(50)
>>> import random
>>> tao.clear()
>>> random.choice(color)
'green'
>>> for i in range(1, 11):
	c = randon.choice(color)
	print(i + ' : ' + c)
	tao.color(c)
	tao.circle(50)
	tao.radians(36)

	
Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    c = randon.choice(color)
NameError: name 'randon' is not defined
>>> for i in range(1, 11):
	c = random.choice(color)
	print(i + ' : ' + c)
	tao.color(c)
	tao.circle(50)
	tao.left(36)

	
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    print(i + ' : ' + c)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(1, 11):
	c = random.choice(color)
	print(str(i) + ' : ' + c)
	tao.color(c)
	tao.circle(50)
	tao.left(36)

	
1 : blue
2 : red
3 : red
4 : yellow
5 : green
6 : blue
7 : red
8 : yellow
9 : yellow
10 : red
>>> for i in range(1, 11):
	c = random.choice(color)
	print(str(i) + ' : ' + c)
	tao.color(c)
	tao.circle(50)
	tao.left(36)

	
1 : red
2 : yellow
3 : red
4 : blue
5 : yellow
6 : green
7 : blue
8 : yellow
9 : red
10 : green
>>> for i in range(1, 11):
	c = random.choice(color)
	print(str(i) + ' : ' + c)
	tao.color(c)
	r = random.randint(50,100)
	print(r)
	tao.circle(r)
	tao.left(36)

	
1 : yellow
64
2 : green
94
3 : yellow
63
4 : green
98
5 : yellow
56
6 : blue
68
7 : yellow
97
8 : red
89
9 : blue
89
10 : blue
57
>>> 