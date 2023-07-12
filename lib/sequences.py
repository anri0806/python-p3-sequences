#!/usr/bin/env python3

def print_fibonacci(length):
    pass 

    # Base case - if length is 0 or 1 => [] or [0]
    # i = 1, while i is smaller than length
    # Fn = Fn-1 + Fn-2
    
    fibo = [0, 1]

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(fibo)
    else:
        i = 2
        
        while i < length:
            num = fibo[i - 1] + fibo[i - 2]
            fibo.append(num)
            i += 1
            
        print(fibo)
