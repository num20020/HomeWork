# Home work number 1

import operator
import time
from functools import wraps

EVEN = 1
ODD = 2
PRIME = 3

degrees = {"Square":2,"Cube":3,"Fourth":4}

def repeater(n):
    while True:
        yield n

# function returns list with some degree of numbers, that are in Lst

def power(lst, deg="Square"):
    return list(map(operator.pow,lst,repeater(degrees[deg])))

def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

#decorator for measuring time lapse of func

def time_lapse(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        beg = time.perf_counter()
        res = func(*args, **kwargs)
        beg = (time.perf_counter()-beg)*1000000
        print(f'time lapse of {func.__name__:} is {beg:.4f} microseconds')
        return res
    return wrapper

#decorator for tracing of recursion

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print_(args[0],"----")
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapper

#function for filtration of list. Result contains the even, odd or prime numbers
#according caller choice

@time_lapse
def my_function(lst, choice = EVEN):
    ret = []
    if choice == EVEN:
        ret = filter(lambda x: x % 2 == 0, lst)
    elif choice == ODD:
        ret = filter(lambda x: x % 2 == 1, lst)
    elif choice == PRIME:
        ret = filter(is_prime, lst)
    return ret

def print_(*args,**kwargs):
    return print(*args,**kwargs,end=' ')

#calculating fibo numbers with recursion

#@time_lapse
@trace
def fibonation(num):
    num=int(num)
    if num<2:
        return num
    return fibonation(num-1)+fibonation(num-2)

if __name__ == "__main__":

    print(power([1, 2, 3]))
    print(power([1, 2, 3], "Cube"))
    print(power([1, 2, 3], "Fourth"))

    alist = range(1,60)

    print("result is: ",list(my_function(alist)))
    print("result is:",list(my_function(alist,ODD)))
    print("result is:",list(my_function(alist,PRIME)))

    n = 10
    print(f'{n}th fibo number is {fibonation(n)}')