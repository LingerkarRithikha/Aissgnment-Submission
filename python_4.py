# -*- coding: utf-8 -*-
"""Python 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QBy2Xh1qpU7zQ_g0nZdim_Ydn5QIJPux
"""

#Day 3 Assigment.

#Define a function which will take a number as argument and return its factorial.
#Call the function to print factorial of any number(integer).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a Number to be factorial: "))
print('Factorial of number is:', factorial(n))