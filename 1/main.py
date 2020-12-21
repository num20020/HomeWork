import operator
import time
#import functools

# Home work number 1

# function returns list with some degree of numbers, that are in Lst


# old version:

# def Power(Lst, Deg=2):
#     Ret = []
#     for i in Lst:
#         # print(type(i))
#         if type(i) == int:
#             Ret.append(i ** Deg)
#     return Ret

# new version

degrees = {"Square":2,"Cube":3,"Fourth":4}

def repeater(n):
    while True:
        yield n


def power(lst, deg="Square"):
    return list(map(operator.pow,lst,repeater(degrees[deg])))


# old version:

# function check numbers in list for: 1. even 2. odd 3. prime by you choice
# and returns a list of suitable

# def MyFunction(Lst, Choice=1):
#     Ret = []
#     for i in Lst:
#         if Choice == 1:
#             if i % 2 == 0: Ret.append(i)
#         elif Choice == 2:
#             if i % 2 == 1: Ret.append(i)
#         elif Choice == 3:
#             Flag = True
#             for n in range(2,int(i/2)+1):
#                 if i % n == 0:
#                     Flag = False
#                     break
#             if Flag: Ret.append(i)
#     return Ret

# new version

EVEN_ = 1
ODD_ = 2
PRIME_ = 3

def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True



from functools import wraps

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
#        if res < 2: print(res)
        print(res)
        return res
    return wrapper

#function for filtration of list. Result contains the even, odd or prime numbers
#according caller choice

@time_lapse
def my_function(lst, choice = EVEN_):
    ret = []
    if choice == EVEN_:
        ret = filter(lambda x: x % 2 == 0, lst)
    elif choice == ODD_:
        ret = filter(lambda x: x % 2 == 1, lst)
    elif choice == PRIME_:
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
    return fibonation(num-2) + fibonation(num-1)



print(power([1, 2, 3]))
print(power([1, 2, 3], "Cube"))
print(power([1, 2, 3], "Fourth"))


alist = range(1,60)


print("result is: ",list(my_function(alist)))

print("result is:",list(my_function(alist,ODD_)))

print("result is:",list(my_function(alist,PRIME_)))

n = 10
print(f'{n}th fibo number is {fibonation(n)}')