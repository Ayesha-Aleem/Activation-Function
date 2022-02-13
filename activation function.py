# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:13:03 2021

@author: HP
"""
import numpy as np
class Neuron():
    def __init__(self,no_of_input):
        self.bias=0.04
        self.weights=[0.2,1,0.4]
    def predict(self, input1, input2,input3):
        summations=input1*self.weights[0]+input2*self.weights[1]+input3*self.weights[2]+self.bias
        return summations
    def sig(self,x):
        c=1/(1 + np.exp(-x))
        return c
x1=128
x2=0
x3=64
x4=35
x5=71
x6=92
x7=21
x8=20
x9=0
a=21
b=0.6
c=0.3
neuron= Neuron(2)
decision= neuron.predict(x1,x2,x3)
print("the decision is:", (decision))
a=decision;
print("After sigmoid function:",neuron.sig(a))
if(a>=1):
    print("The color is blue");
else:
    print("The color is green")

decision1=neuron.predict(x4,x5,x6)
print("the decision is:", (decision1))
b=decision1;
print("After sigmoid function:",neuron.sig(b))
if(b<=0.5):
    print("The color is blue");
else:
    print("The color is green")

decision2=neuron.predict(x7,x8,x9)
print("the decision is:", (decision2))
c=decision2;
print("After sigmoid function:",neuron.sig(c))
if(c<=0.5):
    print("The color is blue");
else:
    print("The color is green")
    
decision3=neuron.predict(a,b,c)
print("the decision is:", (decision3))
q=decision2;
print("After sigmoid function:",neuron.sig(q))
if(q<=0.5):
    print("The color is blue");
else:
    print("The color is green")
