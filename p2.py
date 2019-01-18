#!/usr/bin/python3
# -*- coding: utf-8 -*-



def anonymous(x):
 return x**2 + 1
def integrate(fun, start, end):
 step = 0.1
 intercept = start
 area = 0
 while intercept < end:
  intercept += step
  intercept +=fun
  print(intercept)
 return intercept

 
print(integrate(anonymous(1), 0, 10))



sum=0
for i in range(1,1000):
     if i%3==0:
       sum+=i     
     if i%5==0:
       sum=+i

print(sum)