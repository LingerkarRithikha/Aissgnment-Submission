# -*- coding: utf-8 -*-
"""Python 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wh3iZSvdlv3_AObgCJfHQFfI4E5RM8US
"""

#DAY 5 ASSIGNMENT
#Use filter function to filter out the elements from a list that are divisible by 3 & 5

def fun(n):
  return n % 3 == 0 and n % 5 ==0

li = [30,80,25,90,45,66,15,]

print(list(filter(fun, li)))