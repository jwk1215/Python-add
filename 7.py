#! /usr/bin/env python

pibo = [1,1]

def pibonacci(pibo):
    for i in range(2,100):
        num = pibo[-1]+pibo[-2]
        pibo.append(num)
    return pibo[-1]

print(pibonacci(pibo))

