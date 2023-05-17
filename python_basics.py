Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class
SyntaxError: invalid syntax

x = input('Enter value of x:')
Enter value of x:10

def arithmetic_operat():
    x = input('Enter value of x')
    y = input('Enter value of y')
    z = x + y
    print('Value of z is:',z)
    a = input('Enter value of a:')
    b = input('Enter value of b:')
    c = a * b
    print('The value of a multiplication b is:',c)
    print('Divide')
    d = input('Enter value of d:')
    e = input('Enter value of e:')
    f = d / e
    print('Value after e divided by d is:',f)
    print('floor Divide')
    g = input('Enter value of g:')
    h = input('Enter value of h:')
    i = g % h
    print('Value of h floor divide g is:',i)
    print('Subtraction')
    j = input('Enter value of j:')
    k = input('Enter value of k:')
    l = j - k
    print('Value after k subtracted from j is:',l)
    print('Thanks for using Arithmetic Program :) :)')

    
arithmetic_operat()
Enter value of x10
Enter value of y20
Value of z is: 1020
Enter value of a:10
Enter value of b:20
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    arithmetic_operat()
  File "<pyshell#29>", line 8, in arithmetic_operat
    c = a * b
TypeError: can't multiply sequence by non-int of type 'str'

def arithmetic_operat():
    x = input(int('Enter value of x'))
    y = input(int('Enter value of y'))
    z = x + y
    print('Value of z is:',z)
    a = input(int('Enter value of a:'))
    b = input(int('Enter value of b:'))
    c = a * b
    print('The value of a multiplication b is:',c)
    print('Divide')
    d = input(int('Enter value of d:'))
    e = input(int('Enter value of e:'))
    f = d / e
    print('Value after e divided by d is:',f)
    print('floor Divide')
    g = input(int('Enter value of g:'))
    h = input(int('Enter value of h:'))
    i = g % h
    print('Value of h floor divide g is:',i)
    print('Subtraction')
    j = input(int('Enter value of j:'))
    k = input(int('Enter value of k:'))
    l = j - k
    print('Value after k subtracted from j is:',l)
    print('Thanks for using Arithmetic Program :) :)')

    
arithmetic_operat()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    arithmetic_operat()
  File "<pyshell#33>", line 2, in arithmetic_operat
    x = input(int('Enter value of x'))
ValueError: invalid literal for int() with base 10: 'Enter value of x'

def arithmetic_operat():
    x = int(input('Enter value of x'))
    y = int(input('Enter value of y'))
    z = x + y
    print('Value of z is:',z)
    a = int(input('Enter value of a:'))
    b = int(input('Enter value of b:'))
...     c = a * b
...     print('The value of a multiplication b is:',c)
...     print('Divide')
...     d = int(input('Enter value of d:'))
...     e = int(input('Enter value of e:'))
...     f = d / e
...     print('Value after e divided by d is:',f)
...     print('floor Divide')
...     g = int(input('Enter value of g:'))
...     h = int(input('Enter value of h:'))
...     i = g % h
...     print('Value of h floor divide g is:',i)
...     print('Subtraction')
...     j = int(input('Enter value of j:'))
...     k = int(input('Enter value of k:'))
...     l = j - k
...     print('Value after k subtracted from j is:',l)
...     print('Thanks for using Arithmetic Program :) :)')
... 
...     
>>> arithmetic_operat()
Enter value of x10
Enter value of y20
Value of z is: 30
Enter value of a:10
Enter value of b:20
The value of a multiplication b is: 200
Divide
Enter value of d:45
Enter value of e:5
Value after e divided by d is: 9.0
floor Divide
Enter value of g:1024
Enter value of h:64
Value of h floor divide g is: 0
Subtraction
Enter value of j:2048
Enter value of k:1024
Value after k subtracted from j is: 1024
Thanks for using Arithmetic Program :) :)

def function_2():
    a = 10
    x = 4
    b = 20
    c = 30
    value = 0
    value = (a * (x*x)) + (b * x) + c
    print('value of ax*x+bx+c is:',value)

function_2()








    

