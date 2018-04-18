#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math

def quadratic(a,b,c):
    if not isinstance(a and b and c,(int,float)):
        raise TypeError('bad operand type')
    drt=b*b-4*a*c
    if drt < 0:
        print('无解')
    elif drt == 0:
        x = -b/2/a
        return x
    else:
        x1=(-b+math.sqrt(drt))/(2*a)
        x2=(-b-math.sqrt(drt))/(2*a)
        return x1,x2
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功') 
