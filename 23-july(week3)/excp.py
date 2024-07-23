Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1=int(input("enetr first number"))
enetr first number100
>>> num2=int(input("enter2 number"))
enter2 number0
>>> try:
...     print(num1/num2)
...     print("inside a try")
... 
... 
... except ZeroDivisionError as e:
...     print(e)
... 
division by zero
>>> 
>>> try:
...     print(num1/num2)
...     open("anudip.txt")
... except (ZeroDivisionError,FileNotFoundError):
...     print("something went wrong")
... 
something went wrong
>>> #----------------------------------------------------------------

>>> #-----------------------------------------------------------------
>>> try:
...     print(num1/num2)
...     open("anudip.txt")
... except:
...     print("something went wrong")
... else:
...     print("else block")
... finally:
...     print("finally block")
... 
something went wrong
finally block
