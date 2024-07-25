Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#---------------------------------numpy------------------------------------
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[4,5,6]])
print(np.diag(arr))
[1 5 6]
#----------------------------------------------------------------------------
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
[2 4]
#------------------------------------random number---------------------------
rand=np.random.randint(0,10,2)
print(rand)
[8 0]
rand=np.random.randint(4)
print(rand)
1
rand=n.random.rand(4)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    rand=n.random.rand(4)
NameError: name 'n' is not defined. Did you mean: 'np'?
rand1=np.random.rand(4)
print(rand1)
[0.04385706 0.7138057  0.04856479 0.87589244]
rand=np.random.rand(2,3)
print(rand)
[[0.85841962 0.80749604 0.1608696 ]
 [0.0525541  0.65841345 0.89206453]]
arr=n.random.randint(0,100,12)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    arr=n.random.randint(0,100,12)
NameError: name 'n' is not defined. Did you mean: 'np'?
arr=np.random.randint(0,100,12)
print(arr)
[87 30 91 21  7 90 44 68  8 52 43 80]
#-----------------------------------------------reshape function--------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
arr=np.array([1,2,3,4,5,60])
arr2=arr.reshape(2,2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    arr2=arr.reshape(2,2)
ValueError: cannot reshape array of size 6 into shape (2,2)
arr=np.random.randint(0,100,12)
print(arr)
[54 96 95 63 43 82 33 57 34 61 68 56]
arr=arr.reshape(4,3)
print(arr)
[[54 96 95]
 [63 43 82]
 [33 57 34]
 [61 68 56]]
print("array values is",arr[0][1])
array values is 96
print("array vales is",arr[1][0])
array vales is 63
print(arr.shape)
(4, 3)
arr=arr.reshape(-1,4)
print(arr)
[[54 96 95 63]
 [43 82 33 57]
 [34 61 68 56]]
arr=arr.reshape(2,-1)
print(arr)
[[54 96 95 63 43 82]
 [33 57 34 61 68 56]]
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------seed function-----------------------------------------------------
np.random.seed(145)
arr=np.random.randint(0,100,12)
print(arr)
[37 86 87 18 90 69  8 53 33 32 40 26]
np.random.seed(111)
arr=n.random.randint(0,100,30).reshape(6,5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    arr=n.random.randint(0,100,30).reshape(6,5)
NameError: name 'n' is not defined. Did you mean: 'np'?
arr=np.random.randint(0,100,30).reshape(6,5)
print(arr)
[[84 84 84 86 19]
 [41 66 82 40 71]
 [57  7 12 10 65]
 [88 28 14 34 21]
 [54 72 37 76 58]
 [12 45 69 78 31]]
print(arr[2:,2:])
[[12 10 65]
 [14 34 21]
 [37 76 58]
 [69 78 31]]
print(arr[3:5,2:4])
[[14 34]
 [37 76]]
#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------slicing-------------------------------------------------------------------------
ar=np.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=ar[4:9]
print("new slicing",slicing)
new slicing [3 4 8 5 6]
print("new array",ar)
new array [   1   20    5    9    3    4    8    5    6    2   25    2 2265    3
   33]
print(type(slicing))
<class 'numpy.ndarray'>
print(type(ar))
<class 'numpy.ndarray'>
slicing[:]=0
print("old slicing",slicing)
old slicing [0 0 0 0 0]
print("old array",ar)
old array [   1   20    5    9    0    0    0    0    0    2   25    2 2265    3
   33]
#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------arange function--------------------------------------------------------------------
ar=np.arange(1,15)
print(ar)
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(ar[ar%2==0])
[ 2  4  6  8 10 12 14]
print(ar[ar%2!=0])
[ 1  3  5  7  9 11 13]
print(ar[ar>8])
[ 9 10 11 12 13 14]
ar[ar%2==0]=0
print(ar))
SyntaxError: unmatched ')'
rint(ar)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    rint(ar)
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(ar)
[ 1  0  3  0  5  0  7  0  9  0 11  0 13  0]
arr=np.range(1,8)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    arr=np.range(1,8)
  File "C:\Python311\Lib\site-packages\numpy\__init__.py", line 347, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'range'. Did you mean: 'arange'?
arr=np.arange(1,8)
                         
print(arr)
                         
[1 2 3 4 5 6 7]
print(arr+2)
                         
[3 4 5 6 7 8 9]
print(arr*2)
                         
[ 2  4  6  8 10 12 14]
print(arr**2)
                         
[ 1  4  9 16 25 36 49]
#---------------------------------------------------------------------------------------------------------------------------------------
                         
#---------------------------------------------------------------------------------------------------------------------------------------
                         
arr=np.array([10,20,30,25,6,2])
                         
print(np.min(arr))
                         
2
print(np.max(arr))
                         
30
print(np.argmin(arr))
                         
5
print(np.argmax(arr))
                         
2
print(np.sqrt(arr))
                         
[3.16227766 4.47213595 5.47722558 5.         2.44948974 1.41421356]
print(n.sin(arr))
                         
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print(n.sin(arr))
NameError: name 'n' is not defined. Did you mean: 'np'?
print(np.sin(arr))
                         
[-0.54402111  0.91294525 -0.98803162 -0.13235175 -0.2794155   0.90929743]
print(np.cos(arr))
                         
[-0.83907153  0.40808206  0.15425145  0.99120281  0.96017029 -0.41614684]


#----------------------------------------------------------------------------------------------------------------------------
                         
#----------------------------------------------------------------------------------------------------------------------------
                         

np.random.seed(122)
                         
mat=np.random.randint(1,21,9).reshape(3,3)
                         
print(mat)
                         
[[16 11 13]
 [17 13 16]
 [ 3 16 11]]
print(np.sum(mat))
                         
116
print(np.cumsum(mat))
                         
[ 16  27  40  57  70  86  89 105 116]
print(np.min(mat))
                         
3
print(np.max(mat))
                         
17
print(np.sum(mat,axis=1))
                         
[40 46 30]
print(np.min(mat,axis=1))
                         
[11 13  3]
print(np.max(mat,axis=1))
                         
[16 17 16]
print(np.cumsum(mat,axis=1))
                         
[[16 27 40]
 [17 30 46]
 [ 3 19 30]]
>>> print(np.sum(mat,axis=0))
...                          
[36 40 40]
>>> print(np.min(mat,axis=0))
...                          
[ 3 11 11]
>>> print(np.max(mat,axis=0))
...                          
[17 16 16]
>>> #---------------------------------------------------------------------------------------------------------------------------------------------
...                          
>>> #_--------------------------------------------------------------------------------------------------------------------------------------------
...                          
>>> mat=np.random.randint(1,21,10)
...                          
>>> np.random.seed(122)
...                          
>>> print(mat)
...                          
[10  7 15  4  5 20 20 14  1 14]
>>> np.random.shuffle(mat)
...                          
>>> print(mat)
...                          
[14  1 14  7 20 15  4  5 10 20]
>>> print(np.unique(mat,return_index=True,return_conts=True))
...                          
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    print(np.unique(mat,return_index=True,return_conts=True))
TypeError: unique() got an unexpected keyword argument 'return_conts'
>>> print(np.unique(mat,return_index=True,return_counts=True))
...                          
(array([ 1,  4,  5,  7, 10, 14, 15, 20]), array([1, 6, 7, 3, 8, 0, 5, 4], dtype=int64), array([1, 1, 1, 1, 1, 2, 1, 2], dtype=int64))
>>> print(n.unique(mat).size)
...                          
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    print(n.unique(mat).size)
NameError: name 'n' is not defined. Did you mean: 'np'?
>>> print(np.unique(mat).size)
...                          
8
