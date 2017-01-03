#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:55:17 2017

@author: christophergreen
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""



import math;

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def list_primes(max):
    primes=[]; 
    j=2
    while j<=max:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;

primes=list_primes(2000000);
i=0;
tot=0;
while i<len(primes):
    tot+=primes[i];
    i+=1;
print(tot);  #--> 142913828922  CORRECT