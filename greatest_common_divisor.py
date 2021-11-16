# -*- coding: utf-8 -*-
"""
Get the greatest common divisor for two numbers.
"""

class Greatest_Common_Divisor:
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def get_greatest_common_divisor(self, first, second):
        minimum = min(first, second)
        divisor = 1
        for i in range(divisor, minimum + 1):
            if first % i == 0 and second % i == 0:
                divisor = i
                print(f'Divisor = {divisor}')
        print(f'Greatest common divisor = {divisor}')     
        return divisor

# %%
while True:
    try:
        first = int(input('Enter first number >>> '))
        second = int(input('Enter second number >>> '))
        break
    except:
        print('Wrong value.')
        
greatest_common_divisor = Greatest_Common_Divisor(first, second)
greatest_common_divisor.get_greatest_common_divisor(first, second)