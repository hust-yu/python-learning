# -*- coding: utf-8 -*-
 import math

def quadratic(a,b,c):
    dual=b^2-4*a*c
    if dual<0:
        print('test error')
        return
    else:
        print('test success')
        x1=(-b+math.sqrt(dual))/(2*a)
        x2=(-b-math.sqrt(dual))/(2*a)
        return x1,x2
    pass
print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)=',quadratic(1,3,-4))
