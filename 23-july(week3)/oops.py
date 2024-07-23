Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class student:
    name=""
    age=0
    def study(self):
        print("study 3 hour")

obj=student()
obj.study()
study 3 hour
#------------------------------------------------------------------------------------------------------#
#use of self--------------------------------------------------------------------------------------------
class student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour",self.name)

obj=student()
obj.study()
study 3 hour xyz
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
class student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour")
        sleep()
    def sleep(self):
        print("sleep 1 hour")

obj=student()
obj.study()
study 3 hour
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    obj.study()
  File "<pyshell#28>", line 6, in study
    sleep()
NameError: name 'sleep' is not defined
class student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour")
        self.sleep()
    def sleep(self):
        print("sleep 1 hour")

obj=student()
obj.study()
study 3 hour
sleep 1 hour
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#----------------------------------------inheritance-----------------------------------------------------------------------------
class A:
    def show(self):
        print("this is shoe method")

class B(A):
    pass

class C(B):
    pass

class A:
    def show(self):
        print("this is shoe method")

class b(A):
    pass

class c(A):
    pass


#HYBRID INHERITANCE
KeyboardInterrupt
class A:
    def show(self):
        print("this is shoe method")

CLASS b(A):
    
SyntaxError: invalid syntax
#-----------------------------------------------------------------------------------------------------#
class A:
    def show(self):
        print("this is shoe method")

class B(A):
    def demo(self):
        print("demo method")

class C(A):
    pass

class D(B,C):
    pass

obj=c()
obj.show()
this is shoe method
obj.demo()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    obj.demo()
AttributeError: 'c' object has no attribute 'demo'
#it showed error because siblings me inheritance nhi hoti--------------
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#------------------------------------polymorphism-----------------------------------------------------------
def setdata(id,name):
    print("id,name")

def setdata(id,name,age):
    print("id,name,age")

setdata(101,"sanjay")
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    setdata(101,"sanjay")
TypeError: setdata() missing 1 required positional argument: 'age'
#----------------------------------------------------------------------------------------------------------------------------------------------
def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)
60
sum(10,20,0)
30
#-------------------------------------------------------------method overriding----------------------------------------------------------------#
class bird:
    def intro(self):
        print("there are many types of bird")
    def flight9self):
        
SyntaxError: unmatched ')'
class bird:
    def intro(self):
        print("there are many types of bird")
    def flight(self):
        print("most birds can fly but some can't)
              
SyntaxError: incomplete input
class bird:
    def intro(self):
        print("there are many types of bird")
    def flight(self):
        print("most birds can fly but some can't")

class sparrow(bird):
    def flight(self):
        print("i can fly")

class ostrich(bird):
    def flight(self):
        print("i can't fly)
              
SyntaxError: incomplete input
>>> class bird:
...     def intro(self):
...         print("there are many types of bird")
...     def flight(self):
...         print("most birds can fly but some can't")
... 
... class sparrow(bird):
...     def flight(self):
...         print("i can fly")
... 
... class ostrich(bird):
...     def flight(self):
...         
SyntaxError: invalid syntax
>>> class bird:
...     def intro(self):
...         print("there are many types of bird")
...     def flight(self):
...         print("most birds can fly but some can't")
... 
>>> class sparrow(bird):
...     def flight(self):
...         print("i can fly")
... 
>>> class ostrich(bird):
...     def flight(self):
...         print("i can't fly")
... 
>>> s=ostrich()
>>> s.flight()
i can't fly
>>> #---------------------------------------------------------------------------------------------------------------------------------------
>>> #--------------------------------------------Encapsulation-------------------------------------------------------------------------------
>>> #----------------------------------------------------------------------------------------------------------------------------------------
>>> class A:
...     name="abc"
... 
>>> class B(A):
...     def show(self):
...         print("this is show method",self.name)
... 
>>> obj=B()
>>> obj.show()
this is show method abc
>>> #---------------------------------------------------------------------------------------------------------------------------------------
>>> 
