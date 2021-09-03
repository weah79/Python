Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> friend = ['Prasong','Somsak','Loong']
>>> type(friend)
<class 'list'>
>>> print(friend[0])
Prasong
>>> print(friend[1])
Somsak
>>> print(friend[-1])
Loong
>>> friend.append('Somchai')
>>> print(friend[-1])
Somchai
>>> pet = ('cat','dog')
>>> type(pet)
<class 'tuple'>
>>> print(pet[0])
cat
>>> friend.remove('Prasong')
>>> animal = ('fish','lion','rabbit')
>>> print(animal)
('fish', 'lion', 'rabbit')
>>> frient.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    frient.pop()
NameError: name 'frient' is not defined
>>> friend.pop()
'Somchai'
>>> print(friend)
['Somsak', 'Loong']
>>> friend.pop(0)
'Somsak'
>>> friend.append('Robert')
>>> friend.append('John')
>>> friend.insert(0, 'Wanthong')
>>> print(friend)
['Wanthong', 'Loong', 'Robert', 'John']
>>> friend.insert(1, 'Khun Chang')
>>> print(friend)
['Wanthong', 'Khun Chang', 'Loong', 'Robert', 'John']
>>> friend[2] = 'Uncle'
>>> print(friend)
['Wanthong', 'Khun Chang', 'Uncle', 'Robert', 'John']
>>> del friend[1]
>>> print(friend)
['Wanthong', 'Uncle', 'Robert', 'John']
>>> for f in friend:
	print(f)

	
Wanthong
Uncle
Robert
John
>>> for i,f in enumerate(friend):
	print(i,f)

	
0 Wanthong
1 Uncle
2 Robert
3 John
>>> for i,f in enumerate(friend, start=1):
	print(i,f)

	
1 Wanthong
2 Uncle
3 Robert
4 John
>>> len(friend)
4
>>> ord('ก')
3585
>>> ord('ฮ')
3630
>>> chr(3585)
'ก'
>>> thaichar = []
>>> for i in range(3585,3630):
	thaichar.insert(char(i))

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    thaichar.insert(char(i))
NameError: name 'char' is not defined
>>> for i in range(3585,3630):
	thaichar.insert(chr(i))

	
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    thaichar.insert(chr(i))
TypeError: insert expected 2 arguments, got 1
>>> for i in range(3585,3630):
	print(chr(i))

	
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
ซ
ฌ
ญ
ฎ
ฏ
ฐ
ฑ
ฒ
ณ
ด
ต
ถ
ท
ธ
น
บ
ป
ผ
ฝ
พ
ฟ
ภ
ม
ย
ร
ฤ
ล
ฦ
ว
ศ
ษ
ส
ห
ฬ
อ
>>> for i,f in range(3585,3630):
	print(f, chr(i))

	
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    for i,f in range(3585,3630):
TypeError: cannot unpack non-iterable int object
>>> for i,f in range(3585,3631):
	print(chr(i), f)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for i,f in range(3585,3631):
TypeError: cannot unpack non-iterable int object
>>> for i,f in range(3585,3631):
	print(chr(i))

	
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    for i,f in range(3585,3631):
TypeError: cannot unpack non-iterable int object
>>> for i in range(3585,3631):
	print(chr(i))

	
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
ซ
ฌ
ญ
ฎ
ฏ
ฐ
ฑ
ฒ
ณ
ด
ต
ถ
ท
ธ
น
บ
ป
ผ
ฝ
พ
ฟ
ภ
ม
ย
ร
ฤ
ล
ฦ
ว
ศ
ษ
ส
ห
ฬ
อ
ฮ
>>> for i in range(3585,3631):
	thaichar.append(chr(i))

	
>>> len(thaichar)
46
>>> thaichar.clear()
>>> len(thaichar)
0
>>> for i in range(3585,3631):
	thaichar.append(chr(i))

	
>>> len(thaichar)
46
>>> print(thaichar)
['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
>>> chr(3625)
'ษ'
>>> chr(3622)
'ฦ'
>>> chr(3620)
'ฤ'
>>> thaichar.clear()
>>> for i in range(3585,3631):
	if (i == 3622 || i == 3620)
	{ continue; }
	thaichar.append(chr(i))
	
SyntaxError: invalid syntax
>>> for i in range(3585,3631):
	if (i == 3622 or i == 3620)
	{ continue; }
	thaichar.append(chr(i))
	
SyntaxError: invalid syntax
>>> for i in range(3585,3631):
	if (i == 3622)
	{ continue; }
	thaichar.append(chr(i))
	
SyntaxError: invalid syntax
>>> for i in range(3585,3631):
	if i == 3620 or i == 3622:
	continue
	thaichar.append(chr(i))
	
SyntaxError: expected an indented block
>>> for i in range(3585,3631):
	if i == 3620 or i == 3622:
		continue		
	thaichar.append(chr(i))

	
>>> len(thaichar)
44
>>> print(thaichar)
['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
>>> thaichar.index('ก')
0
>>> days = {'Mon':'จันทร์', 'Tue':'อังคาร', 'Wed':'พุธ'}
>>> from datetime import datetime
>>> dt = datetime.now().strftime('%a')
>>> dt
'Fri'
>>> 