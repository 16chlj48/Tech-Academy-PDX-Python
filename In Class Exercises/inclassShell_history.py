Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> print 'hello world'
hello world
>>> print hello

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print hello
NameError: name 'hello' is not defined
>>> j = 50
>>> print j
50
>>> print J

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print J
NameError: name 'J' is not defined
>>> 1 + 1
2
>>> K = 5
>>> print (j+K)
55
>>> 2-1
1
>>> print (j-K)
45
>>> A = "John is happy"
>>> B = 10.75
>>> type(B)
<type 'float'>
>>> jis 50
SyntaxError: invalid syntax
>>> j is 50
True
>>> j is 23
False
>>> j is not 50
False
>>> j is not 33
True
>>> 25>10
True
>>> 10>25
False
>>> 10==9
False
>>> 9==9
True
>>> J=50
>>> j=0
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/experiment.py", line 3, in <module>
    print "J is " +(J+K)
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/experiment.py", line 10, in <module>
    if B==20:
NameError: name 'B' is not defined
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
20 is equal to B
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/experiment.py ============
55
J wins!
20 is equal to B
>>> name = 'Ashley'
>>> print name.lo

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print name.lo
AttributeError: 'str' object has no attribute 'lo'
>>> print name.lower
<built-in method lower of str object at 0x0321AFC0>
>>> print name.lower()
ashley
>>> print name.upper()
ASHLEY
>>> print name
Ashley
>>> name = 'Ashley'.lower()
>>> print name
ashley
>>> print name.capitalize()
Ashley
>>> print name[0]
a
>>> print name[2]
h
>>> listA = ['mother', 'father', '1970', '1965']
>>> print listA[3]
1965
>>> tupA = ("brother" , "sister", "1990", "1992", "1993", "1995")
>>> print tupA[1:4]
('sister', '1990', '1992')
>>> date = "3/13/2017"
>>> split_the_date = date.split("/")
>>> print split_the_date
['3', '13', '2017']
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/dates.py ==============
Month: 12Day: 25Year: 2017
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/dates.py ==============
Month: 12 Day: 25 Year: 2017
>>> Name ="Chlo"
>>> print Name.swapcase()
cHLO
>>> favColor = "   My favoirite color is purple      "
>>> print favColor.strip()
My favoirite color is purple
>>> print favColor
   My favoirite color is purple      
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 1, in <module>
    Decode = O.r.a.n.g.e
NameError: name 'O' is not defined
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['O', 'r', 'a', 'n', 'g', 'e']
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 4, in <module>
    print "My favorite color is " + splitIt[2].Capitalize();
NameError: name 'splitIt' is not defined
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 4, in <module>
    print "My favorite color is " + splitIT[2].Capitalize();
AttributeError: 'str' object has no attribute 'Capitalize'
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is Green
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 7, in <module>
    print "In " + years + " years, it will be " + (currentYear + years)
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 8, in <module>
    print "In " + years + " years, it will be " + futureYear
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 8, in <module>
    print "In " + (years) + " years, it will be " + (futureYear)
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 8, in <module>
    print ("In " + years + " years, it will be " + futureYear)
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 234 years, it will be 2251
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 234 years, it will be the year 2251
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 235 years, it will be the year 2252
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 242 years, it will be the year 2259
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 243 years, it will be the year 2260
This year is a multiple of 10
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
My favorite color is GREEN
In 243 years, it will be the year 2260
This year is a multiple of 10
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
The last color is GREEN
In 243 years, it will be the year 2260
That year is a multiple of 10
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
The last color is GREEN
In 243 years, it will be the year 2260
That year is a multiple of 10
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
The last color is GREEN
In 243 years, it will be the year 2260
That year is a multiple of 10
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
['Orange', 'Red', 'Green']
The last color is GREEN
In 245 years, it will be the year 2262
Just another year
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> Id()
no Python documentation found for 'Id()'


help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> Id()

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Id()
NameError: name 'Id' is not defined
>>> A Id()
SyntaxError: invalid syntax
>>> Id(A)

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    Id(A)
NameError: name 'Id' is not defined
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
Input a number of years5
['Orange', 'Red', 'Green']
The last color is GREEN

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/myFirst.py", line 7, in <module>
    futureYear = currentYear+years
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
Input a number of years6
['Orange', 'Red', 'Green']
The last color is GREEN
In 6 years, it will be the year 2023
Just another year
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
Input a number of years: 99999
['Orange', 'Red', 'Green']
The last color is GREEN
In 99999 years, it will be the year 102016
Just another year
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
Input a number of years: 9088
In 9088 years, it will be the year 11105
Just another year
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/myFirst.py =============
Input a number of years: 66
In 66 years, it will be the year 2083
Just another year
>>> A=10
>>> if A != 5:
	print "not ="

	
not =
>>> 
>>> 
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/nameComp.py =============
Hello Jack
>>> 
============= RESTART: C:/Users/Janko/Desktop/Python/nameComp.py =============
You are not Jack
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/playAgain.py ============
Play Again
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/playAgain.py ============
Please enter Yes or No
>>> if A != 5:
	print "not ="

	

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    if A != 5:
NameError: name 'A' is not defined
>>> if A != 5:
	print "not ="

	

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    if A != 5:
NameError: name 'A' is not defined
>>> print 'hello world'
hello world
>>> print helloif A != 5:
	print "not ="
	
SyntaxError: invalid syntax
>>> 
>>> 99999
99999
>>> 
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/playAgain.py ============
Play Again
>>> 
=============== RESTART: C:/Users/Janko/Desktop/Python/sib.py ===============

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/sib.py", line 1, in <module>
    Str = int(rawInput("How many siblings do you have"))
NameError: name 'rawInput' is not defined
>>> 
=============== RESTART: C:/Users/Janko/Desktop/Python/sib.py ===============

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/sib.py", line 1, in <module>
    Str = int(raw_Input("How many siblings do you have"))
NameError: name 'raw_Input' is not defined
>>> 
=============== RESTART: C:/Users/Janko/Desktop/Python/sib.py ===============
How many siblings do you have5
Not too many
>>> 
=============== RESTART: C:/Users/Janko/Desktop/Python/sib.py ===============
How many siblings do you have? 6
Not too many
>>> 
=============== RESTART: C:/Users/Janko/Desktop/Python/sib.py ===============
How many siblings do you have? 7
Lots of people!
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/countLoop.py ============
1
2
3
4
5
6
7
8
9
10
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/countLoop.py ============
10
9
8
7
6
5
4
3
2
1
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/countLoop.py ============
10
8
6
4
2
>>> 
============ RESTART: C:/Users/Janko/Desktop/Python/whileLoop.py ============
1
2
3
4
5
6
7
8
9
10
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============

Traceback (most recent call last):
  File "C:/Users/Janko/Desktop/Python/bands.py", line 1, in <module>
    Name_of_list = [item1, item2]
NameError: name 'item1' is not defined
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
['The Beatles', 'The Rolling Stones', 'Led Zeppelin', 'Jimmy Hendrix']
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
The Beatles is an awesome band
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
The Beatles is an awesome band!
['The Beatles', 'The Rolling Stones', 'Led Zeppelin', 'Jimmy Hendrix', 'The Temptations']
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
The Beatles is an awesome band!
['The Beatles', 'The Rolling Stones', 'Led Zeppelin', 'Jimmy Hendrix', 'The Temptations']
['The Beatles', 'The Rolling Stones', 'James Brown', 'Jimmy Hendrix', 'The Temptations']
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/bands.py ==============
The Beatles are a great band!
The Rolling Stones are a great band!
White Stripes are a great band!
The Jets are a great band!
>>> 
============== RESTART: C:/Users/Janko/Desktop/Python/powers.py ==============
9765625
10000000000
576650390625
10240000000000
95367431640625
>>> 
========== RESTART: C:/Users/Janko/Desktop/Python/bdayDictionary.py ==========
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
>>> 
========== RESTART: C:/Users/Janko/Desktop/Python/bdayDictionary.py ==========
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
>>> 
========== RESTART: C:/Users/Janko/Desktop/Python/bdayDictionary.py ==========
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
{'Kelly': 'May 1955', 'Sarah': 'November 1980', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
>>> 
========== RESTART: C:/Users/Janko/Desktop/Python/bdayDictionary.py ==========
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
{'Kelly': 'May 1955', 'Sarah': 'November 1980', 'Maxine': 'March 1962', 'Violet': 'January 1948', 'Emily': 'June 1950'}
Kelly's Birthday is May 1955
>>> 
