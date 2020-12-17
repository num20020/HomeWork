# Home work number 1

# function returns list with some degree of numbers, that are in Lst

def Power(Lst, Deg=2):
    Ret = []
    for i in Lst:
        # print(type(i))
        if type(i) == int:
            Ret.append(i ** Deg)
    return Ret

# function check numbers in list for: 1. even 2. odd 3. prime by you choice
# and returns a list of suitable

def MyFunction(Lst, Choice=1):
    Ret = []
    for i in Lst:
        if Choice == 1:
            if i % 2 == 0: Ret.append(i)
        elif Choice == 2:
            if i % 2 == 1: Ret.append(i)
        elif Choice == 3:
            Flag = True
            for n in range(2,int(i/2)+1):
                if i % n == 0:
                    Flag = False
                    break
            if Flag: Ret.append(i)
    return Ret

print(Power([1, 'a', 3], 3))
print(Power([1]))
alist =[]
for i in range(1,100):
    alist.append(i)
print(MyFunction(alist,3))

print(MyFunction([3],3))