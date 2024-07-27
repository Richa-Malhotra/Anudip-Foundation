Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #-----------------------------------------------------------------
>>> #---------------------where function------------------------------
>>> import numpy as np
>>> arr=np.array([1,2,3,4,5])
>>> arr1=arr.where(arr>3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    arr1=arr.where(arr>3)
AttributeError: 'numpy.ndarray' object has no attribute 'where'
>>> arr1=np.where(arr>3)
>>> print(arr1)
(array([3, 4], dtype=int64),)
>>> #---------------------------------------------------------------------
>>> #---------------------------------------------------------------------
>>> #----------------------transpose function-----------------------------
>>> arr=np.array([[1,2,3],[4,5,6]])
>>> transposed_arr=np.transpose(arr)
>>> print(transposed_arr)
[[1 4]
 [2 5]
 [3 6]]
>>> print(arr)
[[1 2 3]
 [4 5 6]]
>>> #---------------------------------------------------------------------
>>> #---------------------------------------------------------------------
>>> #---------------------mean function-----------------------------------
>>> arr1=np.mean(arr)
>>> print(arr1)
3.5
>>> #----------------------------------------------------------------------
>>> #---------------------------searchsorted function---------------------
>>> sorted_array=np.array([1,3,5,6,7])
>>> index=np.searchsorted(sorted_array,6)
>>> print("index to insert",index)
index to insert 3
>>> #-------------------------------------------------------------------------
>>> #-----------------------------extract function----------------------------
